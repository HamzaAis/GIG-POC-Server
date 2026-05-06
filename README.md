# AI Server

A self-hosted AI stack running on a single NVIDIA RTX A5000 (24GB).

## Services

| Service | Port | Model | Purpose |
|---|---|---|---|
| `qwen3-4b-text` | 8040 | Qwen3-4B-Q4_K_M | Text-to-text chat (thinking mode) |
| `qwen2-5-vl` | 8050 | Qwen2.5-VL-7B-Q4_K_M | Vision + text chat |
| `clip-embeddings` | 8060 | CLIP ViT-B/32 | Text & image embeddings |

---

## Text Chat (Qwen3-4B) — Port 8040

### Basic chat
```bash
curl http://localhost:8040/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-4b",
    "messages": [
      {"role": "user", "content": "Hello, who are you?"}
    ]
  }'
```

### With system prompt
```bash
curl http://localhost:8040/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-4b",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Explain how transformers work in one paragraph."}
    ],
    "temperature": 0.7,
    "max_tokens": 512
  }'
```

### Disable thinking mode (faster responses)
```bash
curl http://localhost:8040/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-4b",
    "messages": [
      {"role": "user", "content": "What is 2+2?"}
    ],
    "thinking": false
  }'
```

### Streaming
```bash
curl http://localhost:8040/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-4b",
    "messages": [
      {"role": "user", "content": "Write a short poem about the sea."}
    ],
    "stream": true
  }'
```

---

## Vision + Text Chat (Qwen2.5-VL) — Port 8050

### Text only
```bash
curl http://localhost:8050/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-vl",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }'
```

### Image + text (base64)
```bash
# First encode your image
IMAGE_B64=$(base64 -w 0 /path/to/image.jpg)

curl http://localhost:8050/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"qwen2.5-vl\",
    \"messages\": [
      {
        \"role\": \"user\",
        \"content\": [
          {
            \"type\": \"image_url\",
            \"image_url\": {\"url\": \"data:image/jpeg;base64,${IMAGE_B64}\"}
          },
          {
            \"type\": \"text\",
            \"text\": \"Describe what you see in this image.\"
          }
        ]
      }
    ]
  }"
```

### Image + text (URL)
```bash
curl http://localhost:8050/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-vl",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image_url",
            "image_url": {"url": "https://example.com/image.jpg"}
          },
          {
            "type": "text",
            "text": "What is in this image?"
          }
        ]
      }
    ]
  }'
```

---

## Embeddings (CLIP ViT-B/32) — Port 8060

### Text embedding
```bash
curl http://localhost:8060/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/clip-vit-base-patch32",
    "input": "a photo of a cat"
  }'
```

### Batch text embeddings
```bash
curl http://localhost:8060/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/clip-vit-base-patch32",
    "input": ["a photo of a cat", "a photo of a dog", "a sunny beach"]
  }'
```

### Image embedding (base64)
```bash
IMAGE_B64=$(base64 -w 0 /path/to/image.jpg)

curl http://localhost:8060/embeddings_image \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"openai/clip-vit-base-patch32\",
    \"input\": [\"data:image/jpeg;base64,${IMAGE_B64}\"]
  }"
```

---

## Health Checks

```bash
curl http://localhost:8040/health   # Qwen3-4B text
curl http://localhost:8050/health   # Qwen2.5-VL vision
curl http://localhost:8060/health   # CLIP embeddings
```

---

## Management

```bash
# Start all services
docker compose up -d

# Stop all services
docker compose down

# View logs
docker compose logs -f

# Download / update models
uv run download.py
```
