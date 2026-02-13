# 🎨 Z-Image Turbo - Przewodnik Tekstu/Watermarków

**Wersja dokumentacji:** 2026-02-09

---

## 📋 Podsumowanie problemu

**Problem:**
- Z-Image Turbo lokalnie generuje obrazy z tekstem/watermarkami
- Użytkownik chce workflow do generowania czystych obrazów
- Standardowe negative prompty nie działają

**Przyczyny:**
1. Model nie wspiera standardowych negative promptów
2. Tagi w promptie są interpretowane jako treść (nie jako wykluczenia)
3. Watermarki w wielu modelach są domyślane

---

## ✅ Rozwiązania

### Metoda 1: Proper Prompt Engineering (Najprostsza!)

**ZASADA:**
- Długa naturalna lista zamiast tagów
- Wszystkie wykluczenia na końcu promptu
- Precyzyjny opis oświetlenia i kompozycji

**Przykład CZYSTEGO PROMPTU:**
```
Pozytywny:
"A cinematic sunset over a mountain lake at dawn, fog rolling over the water, dramatic sky with warm colors. Golden hour sun positioned behind the subject, creating warm rim light and a glowing effect through hair. Soft bokeh effect on the water surface. The lighting creates a dreamy, nostalgic atmosphere. Shot on Leica M6 with Kodak Portra 400 film grain aesthetic. High contrast between the warm sunset light and the cool shadows of the distant peaks."

Negatywny:
"no text overlay, no watermark, no signature, no logo, no captions, no signage, no symbols, no letters, no typography, no words on the image. Pure visual scene. Clean natural landscape. No text elements whatsoever. No readable marks of any kind. Pure image-only composition."
```

---

### Metoda 2: ComfyUI Workflow z Positive + Negative Prompts

**Przykład workflow:**
```
1. Z-Image Turbo Text Encoder → Qwen
2. Negative Prompt (nie puste!):
   - "no text, no watermark, no signature, no logo"
3. KSampler: ddim/kl_optimal lub seeds_3/beta
4. Steps: 8
5. CFG: 1.0
6. Resolution: 1024x1024
```

**Ważne:** Negative prompt w workflow w Z-Image Turbo jest **TAKI SAM jak zwykły prompt** - dodaj go jako osobny input!

---

### Metoda 3: "Empty Latent" (Najnowocześniejsza!)

**Koncepcja:** 
Z-Image Turbo ma specjificzny negatywny input. Jakość pusty lub z minimalną treścią ("text", "") model ignoruje go jako "brak czegoś"

**Użycie:**
```json
{
  "empty_negative": ["text", "watermark", "signature"]
}
```

---

### Metoda 4: Prompt Enhancement przez AI

**Opis:** Użyj ChatGPT lub Gemini do rozwinięcia promptu

**Zasada:**
```
Prompt podstawowy: "Beautiful woman, sunset, beach"
Wzmiana AI: "Dopisz opis z wywołanymi detalami o oświetleniu, kompozycji, nastroju i stylu fotograficznym. Dodaj ekskluzje na końcu: no text overlay, no watermark, clean pure image."
```

---

### Metoda 5: Post-Processing (Opcjonalne)

Jeśli nadal generujesz tekstu:
1. **Inpainting** w Photoshop/GIMP
2. **Post-processing** w ComfyUI:
   - Użyj VAE Decode dla lepszej jakości
   - Zastosuj 2x upscaling
   - Włącz "text output" (jeśli chcesz tekst na obrazie)

---

### Metoda 6: Zmiana modelu (Najnowocześniejsza!)

**Opcje:**
- Użyj model bez "Z-Image" w nazwie (np. zImage-base lub in-house training)
- Rozważ FLUX 1.1 - jest bez problemów z tekstem
- Rozważ Stable Diffusion 3 - ale potrzebuje więcej VRAM

---

## 🛠️ Zalecenia dla komfortu

### Dla początkujących:
1. **Trzymaj się Settings Core:**
   - Steps: 8
   - CFG: 1.0
   - Sampler: ddim/kl_optimal
   - Resolution: 1024x1024

2. **Trenuj prompt engineering:**
   - Używaj pełne zdania, nie tagi
   - Dodawaj obszerne opisy (3-5 zdań)

### Dla zaawansowanych:

1. **Workflow ComfyUI:**
   - Import workflow z "Z-Image Turbo Text Encoder" + "Empty Latent"
   - Dostosuj Negative Prompt jako osobny input
   - Użyj VAE Decode dla lepszej jakości

2. **Post-processing:**
   - Inpainting w GIMP/Photoshop
   - Użyj 2x upscaling w ComfyUI
   - Zastosuj denoising dla usunięcia artefaktów

3. **Monitoring:**
   - Sprawdź czy model generuje tekst
   - Jeśli tak → zastosuj "Empty Latent"
   - W przeciwnym razie → post-processing

---

## 🎯 Szybkie startowe (przygotowe do wypróbowania)

### Start 1: Simple Negative
```
Prompt: "A beautiful portrait of a woman in soft lighting"
Negative: "no text, no watermark, no signature, no logo"
Steps: 8, CFG: 1.0
Sampler: euler
Resolution: 1024x1024
```

### Start 2: Detailed Prompt
```
Pozytywny:
"A close-up realistic photograph of a young woman with long, black hair in a well-lit elevator. She is styled in a cute, playful way, wearing a black floral off-the-shoulder crop top and dark denim jeans. She tilts her head and makes a pout/kissing face at the camera. Her dark gray smartphone, held in her right hand, covers a small part of her face. High quality 8K resolution. Soft studio lighting. Shallow depth of field. Neutral background. Cinematic style. Professional makeup. Natural skin texture. Catchlight in eyes."

Negative: "no text overlay, no watermark, no signature, no logo, no captions, no symbols, no letters, no typography, no words on the image. Pure visual scene. Clean natural portrait. No text elements whatsoever. No readable marks of any kind. Pure image-only composition."

Steps: 8, CFG: 1.0
Sampler: ddim/kl_optimal
Resolution: 1024x1024
```

### Start 3: Landscape
```
Pozytywny:
"A breathtaking mountain landscape at golden hour with soft morning light. Rolling hills covered in vibrant wildflowers. Crystal clear lake reflecting the sky. Dense forest in the distance with morning mist rising between the trees. Peaceful, serene atmosphere. High quality. Natural lighting. Cinematic composition. Wide angle. Colorful and vibrant."

Negative: "no text overlay, no watermark, no signature, no logo, no captions, no signage, no symbols, no letters, no typography, no words on the image. Pure visual scene. Clean natural landscape. No text elements whatsoever. No readable marks of any kind. Pure image-only composition."

Steps: 8, CFG: 1.0
Sampler: ddim/kl_optimal
Resolution: 1024x1024
```

---

## 🔍 Diagnostyka

### Jeśli nadal generuje tekst:
1. Sprawdź czy w promptie masz słowa kluczowe
2. Użyj `no text` jako część opisu, nie jako osobny negative
3. Sprawdź czy nie przypadkowo używasz cudzysłowów w promptie

### Jeśli obrazy są "plastikowe":
1. Zmniejsz rozdzielczość do 512x512
2. Sprawdź czy CFG nie jest za wysokie
3. Sprawdź czy steps nie są za duże

### Jeśli są artefakty:
1. Zmniejsz liczbę LoRA
2. Zmień sampler na ddim/kl_optimal
3. Sprawdź czy używasz poprawnego VAE
4. Zmniejsz rozdzielczość

---

## 📊 Podsumowanie

| Metoda | Skuteczność | Złożoność |
|--------|------------|-----------|--------------|
| **1. Prompt Engineering** | ⭐⭐⭐⭐ | ⭐⭐ |
| **2. ComfyUI Workflow** | ⭐⭐⭐ | ⭐⭐ |
| **3. Empty Latent** | ⭐⭐ | ⭐ |
| **4. Post-processing** | ⭐⭐ | ⭐ |
| **5. Prompt Enhancement** | ⭐⭐ | ⭐ |
| **6. Zmiana modelu** | ⭐⭐ | ⭐ |

---

## 🚀 Natychmiast działania

### Spróbuj teraz:

1. **Poczekaj co generuje**
2. **Użyj Prompt Start 1** (Simple Negative)
3. **Sprawdź czy obraz jest czysty**

### Jeśli działa → Rozwijaj workflow
- Post-processing w ComfyUI
- Dodaj nowe filtry post-processingu

### Jeśli nie działa → Diagnostyka
1. Sprawdź ustawienia Core (8 steps, CFG 1.0)
2. Spróbuj inny sampler (seeds_3/beta)
3. Sprawdź czy model jest odpowiedni

---

## 💡 Gotowy link do workflow ComfyUI

**Workflow JSON (do skopiowania):**
```json
{
  "last_node_id": 10,
  "last_link_id": 15,
  "nodes": [
    {
      "id": 1,
      "type": "CheckpointLoaderSimple",
      "title": "Load Z-Image Turbo",
      "properties": {
        "Node name for S&R": "CheckpointLoaderSimple"
      },
      "widgets_values": [ "z_image_turbo_bf16.safetensors" ],
      "outputs": [
        { "name": "MODEL", "type": "MODEL", "links": [ 1 ] },
        { "name": "CLIP", "type": "CLIP", "links": [ 2 ] }
      ],
      "pos": [ 50, 50 ]
    },
    {
      "id": 2,
      "type": "CLIPTextEncode",
      "title": "Prompt (Qwen Encoded)",
      "widgets_values": [ "cinematic photo, 8k, highly detailed..." ],
      "inputs": [ { "name": "clip", "type": "CLIP", "link": 2 } ],
      "outputs": [
        { "name": "CONDITIONING", "type": "CONDITIONING", "links": [ 4 ] }
      ],
      "pos": [ 400, 250 ]
    },
    {
      "id": 3,
      "type": "CLIPTextEncode",
      "title": "Empty Latent (No Negative)",
      "widgets_values": [ "" ],
      "inputs": [ { "name": "clip", "type": "CLIP", "link": 3 } ],
      "outputs": [
        { "name": "CONDITIONING", "type": "CONDITIONING", "links": [ 5 ] }
      ],
      "pos": [ 400, 250 ]
    },
    {
      "id": 4,
      "type": "KSampler",
      "title": "8-Step Sampler",
      "widgets_values": [ 266481289456, "fixed", 8, 1.0, "euler_ancestral", "sgm_uniform" ],
      "inputs": [
        { "name": "model", "type": "MODEL", "link": 1 },
        { "name": "positive", "type": "CONDITIONING", "link": 4 },
        { "name": "negative", "type": "CONDITIONING", "link": 5 },
        { "name": "latent_image", "type": "LATENT", "link": 6 }
      ],
      "outputs": [
        { "name": "LATENT", "type": "LATENT", "links": [ 7 ] }
      ],
      "pos": [ 500, 450 ]
    },
    {
      "id": 5,
      "type": "EmptyLatentImage",
      "title": "Empty Latent (No Negative)",
      "widgets_values": [ "" ],
      "inputs": [
        { "name": "samples", "type": "LATENT", "link": 7 }
      ],
      "outputs": [
        { "name": "IMAGE", "type": "IMAGE", "links": [ 8 ] }
      ],
      "pos": [ 800, 100 ]
    },
    {
      "id": 6,
      "type": "VAEDecode",
      "title": "VAE Decode",
      "inputs": [ { "name": "samples", "type": "LATENT", "link": 7 },
        { "name": "vae", "type": "VAE", "link": 3 }
      ],
      "outputs": [
        { "name": "IMAGE", "type": "IMAGE", "links": [ 8 ] }
      ],
      "pos": [ 900, 900 ]
    }
  ]
}
```

---

**Uwaga:** Ten workflow jest podstawą. Rozwij go według potrzeb!

🦊 **Powodzenia!**
