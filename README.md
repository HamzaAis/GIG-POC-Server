# Text embedding
POST http://localhost:8060/embeddings
{"model": "openai/clip-vit-base-patch32", "input": "your text"}

# Image embedding
POST http://localhost:8060/embeddings_image  
{"model": "openai/clip-vit-base-patch32", "input": ["data:image/jpeg;base64,{b64}"]}

# Chat (text only)
POST http://localhost:8050/v1/chat/completions
{"model": "qwen/qwen2.5-vl", "messages": [...]}

# Chat with image (base64)
POST http://localhost:8050/v1/chat/completions
{"model": "qwen/qwen2.5-vl", "messages": [{"role": "user", "content": [
    {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,{b64}"}},
    {"type": "text", "text": "your question"}
]}]}



