#!/usr/bin/env python3
"""ComfyUI API Client for Image Generation"""

import json
import random
import time
import sys
import os
from urllib.request import Request, urlopen
from urllib.error import URLError

# Base URL
BASE_URL = os.environ.get("COMFYUI_BASE_URL", "https://lavinia-translatable-pseudomedievally.ngrok-free.dev")

# Base workflow from ComfyUI export
BASE_WORKFLOW = {
    "39": {
        "inputs": {"clip_name": "qwen_3_4b.safetensors", "type": "lumina2", "device": "default"},
        "class_type": "CLIPLoader",
        "_meta": {"title": "Load CLIP"}
    },
    "40": {
        "inputs": {"vae_name": "ae.safetensors"},
        "class_type": "VAELoader",
        "_meta": {"title": "Load VAE"}
    },
    "41": {
        "inputs": {"width": 512, "height": 512, "batch_size": 1},
        "class_type": "EmptySD3LatentImage",
        "_meta": {"title": "EmptySD3LatentImage"}
    },
    "42": {
        "inputs": {"conditioning": ["45", 0]},
        "class_type": "ConditioningZeroOut",
        "_meta": {"title": "ConditioningZeroOut"}
    },
    "43": {
        "inputs": {"samples": ["44", 0], "vae": ["40", 0]},
        "class_type": "VAEDecode",
        "_meta": {"title": "VAE Decode"}
    },
    "44": {
        "inputs": {
            "seed": 0,  # Will be replaced
            "steps": 9,
            "cfg": 1,
            "sampler_name": "res_multistep",
            "scheduler": "simple",
            "denoise": 1,
            "model": ["47", 0],
            "positive": ["45", 0],
            "negative": ["42", 0],
            "latent_image": ["41", 0]
        },
        "class_type": "KSampler",
        "_meta": {"title": "KSampler"}
    },
    "45": {
        "inputs": {
            "text": "prompt here",  # Will be replaced
            "clip": ["39", 0]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {"title": "CLIP Text Encode (Prompt)"}
    },
    "46": {
        "inputs": {
            "unet_name": "zImageTurboQuantized_fp8ScaledE4m3fnKJ.safetensors",
            "weight_dtype": "default"
        },
        "class_type": "UNETLoader",
        "_meta": {"title": "Load Diffusion Model"}
    },
    "47": {
        "inputs": {"shift": 3, "model": ["46", 0]},
        "class_type": "ModelSamplingAuraFlow",
        "_meta": {"title": "ModelSamplingAuraFlow"}
    },
    "64": {
        "inputs": {"images": ["43", 0]},
        "class_type": "SaveImageWebsocket",
        "_meta": {"title": "SaveImageWebsocket"}
    },
    "65": {
        "inputs": {"filename_prefix": "ComfyUI", "images": ["43", 0]},
        "class_type": "SaveImage",
        "_meta": {"title": "Save Image"}
    }
}


def api_post(endpoint: str, data: dict = None) -> dict:
    """POST request to ComfyUI API"""
    url = f"{BASE_URL}{endpoint}"
    req_data = json.dumps(data).encode() if data else None
    req = Request(url, data=req_data, headers={"Content-Type": "application/json"})

    try:
        with urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except URLError as e:
        print(f"ERROR: API request failed: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON response: {e}")
        sys.exit(1)


def api_get(endpoint: str) -> dict:
    """GET request to ComfyUI API"""
    url = f"{BASE_URL}{endpoint}"
    req = Request(url, headers={"Content-Type": "application/json"})

    try:
        with urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except URLError as e:
        print(f"ERROR: API request failed: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON response: {e}")
        sys.exit(1)


def generate(prompt: str, seed: int = None, steps: int = 9, cfg: float = 1.0,
             width: int = 512, height: int = 512) -> str:
    """Generate image with given prompt"""
    # Clone workflow
    workflow = json.loads(json.dumps(BASE_WORKFLOW))

    # Update prompt
    workflow["45"]["inputs"]["text"] = prompt

    # Update seed
    workflow["44"]["inputs"]["seed"] = seed if seed is not None else random.randint(0, 2**63)

    # Update parameters
    workflow["44"]["inputs"]["steps"] = steps
    workflow["44"]["inputs"]["cfg"] = cfg
    workflow["41"]["inputs"]["width"] = width
    workflow["41"]["inputs"]["height"] = height

    # Submit workflow
    response = api_post("/prompt", {"prompt": workflow})
    prompt_id = response.get("prompt_id")

    if not prompt_id:
        print("ERROR: No prompt_id in response")
        sys.exit(1)

    # Wait for completion
    print(f"Generating image (prompt_id: {prompt_id})...")

    max_wait = 300  # 5 minutes max
    start_time = time.time()

    while True:
        if time.time() - start_time > max_wait:
            print("ERROR: Generation timeout")
            sys.exit(1)

        history = api_get(f"/history/{prompt_id}")

        if prompt_id in history:
            # Check if complete
            output = history[prompt_id].get("outputs", {})

            if "65" in output:  # SaveImage node
                images = output["65"].get("images", [])
                if images:
                    image_info = images[0]
                    filename = image_info.get("filename")
                    subfolder = image_info.get("subfolder", "")
                    image_type = image_info.get("type", "output")

                    # Build URL
                    url_parts = []
                    if subfolder:
                        url_parts.append(f"subfolder={subfolder}")
                    url_parts.append(f"type={image_type}")
                    url_parts.append(f"filename={filename}")

                    image_url = f"{BASE_URL}/view?{'&'.join(url_parts)}"

                    print(f"OK: Image generated")
                    print(f"  filename: {filename}")
                    print(f"  url: {image_url}")
                    print(f"  seed: {workflow['44']['inputs']['seed']}")

                    return image_url

        time.sleep(2)


def status(prompt_id: str):
    """Check status of a generation"""
    history = api_get(f"/history/{prompt_id}")

    if prompt_id in history:
        data = history[prompt_id]
        status_str = data.get("status", {}).get("status_str", "unknown")
        outputs = data.get("outputs", {})

        print(f"Status: {status_str}")

        if "65" in outputs:
            images = outputs["65"].get("images", [])
            print(f"Images: {len(images)}")
            for img in images:
                print(f"  - {img.get('filename')}")
    else:
        print(f"No history for prompt_id: {prompt_id}")


def queue():
    """Check queue status"""
    info = api_get("/queue")

    running = info.get("queue_running", [])
    pending = info.get("queue_pending", [])

    print(f"Running: {len(running)}")
    for item in running:
        print(f"  - {item}")

    print(f"Pending: {len(pending)}")
    for item in pending:
        print(f"  - {item}")


def main():
    if len(sys.argv) < 2:
        print("Usage: comfyui_cli.py <command> [args]")
        print("Commands:")
        print("  generate <prompt> [--seed N] [--steps N] [--cfg N] [--width N] [--height N]")
        print("  status <prompt_id>")
        print("  queue")
        sys.exit(1)

    command = sys.argv[1]

    if command == "generate":
        if len(sys.argv) < 3:
            print("ERROR: prompt required")
            sys.exit(1)

        prompt = sys.argv[2]
        seed = None
        steps = 9
        cfg = 1.0
        width = 512
        height = 512

        # Parse args
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--seed" and i + 1 < len(sys.argv):
                seed = int(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] == "--steps" and i + 1 < len(sys.argv):
                steps = int(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] == "--cfg" and i + 1 < len(sys.argv):
                cfg = float(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] == "--width" and i + 1 < len(sys.argv):
                width = int(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] == "--height" and i + 1 < len(sys.argv):
                height = int(sys.argv[i + 1])
                i += 2
            else:
                i += 1

        generate(prompt, seed, steps, cfg, width, height)

    elif command == "status":
        if len(sys.argv) < 3:
            print("ERROR: prompt_id required")
            sys.exit(1)
        status(sys.argv[2])

    elif command == "queue":
        queue()

    else:
        print(f"ERROR: Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
