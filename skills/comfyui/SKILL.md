# ComfyUI API - Image Generation

**Base URL:** https://lavinia-translatable-pseudomedievally.ngrok-free.dev

## What It Does

Generate images using ComfyUI AuraFlow/Turbo model with Qwen CLIP.

## Workflow

```
CLIPLoader (qwen_3_4b.safetensors)
    ↓
CLIPTextEncode (prompt)
    ↓
UNETLoader (zImageTurboQuantized) → ModelSamplingAuraFlow (shift=3)
    ↓
EmptySD3LatentImage (512x512)
    ↓
KSampler (steps=9, cfg=1, res_multistep)
    ↓
VAELoader + VAEDecode
    ↓
SaveImage / SaveImageWebsocket
```

## Usage

### Generate Image

```bash
python3 tools/comfyui_cli.py generate "your prompt here" --seed [optional]
```

Returns:
- Image URL (if accessible via public endpoint)
- Or image saved to workspace

### Check Status

```bash
python3 tools/comfyui_cli.py status [prompt_id]
```

## Parameters

- **Prompt:** Text description (required)
- **Seed:** Optional random seed (default: random)
- **Steps:** Sampling steps (default: 9)
- **CFG:** Classifier-free guidance (default: 1)
- **Width/Height:** Image size (default: 512x512)

## API Endpoints

- POST /prompt - Submit workflow
- GET /history/{prompt_id} - Check status
- GET /view?filename=X - Retrieve image
- GET /queue - Check queue status

## Notes

- Model is fast (9 steps for quality)
- Supports prompt tweaking via CLIP text encode
- Images saved with prefix "ComfyUI"
