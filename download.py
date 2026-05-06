from huggingface_hub import hf_hub_download
import os

# Configuration for the models
models_to_download = [
    {
        'repo_id': 'unsloth/Qwen2.5-VL-7B-Instruct-GGUF',
        'files': ['Qwen2.5-VL-7B-Instruct-Q4_K_M.gguf', 'mmproj-BF16.gguf'],
        'local_dir': '/home/paperspace/ai-server/models/qwen2.5-vl-7b'
    },
    {
        'repo_id': 'openai/clip-vit-base-patch32',
        'files': ['config.json', 'pytorch_model.bin', 'preprocessor_config.json', 'vocab.json'],
        'local_dir': '/home/paperspace/ai-server/models/clip-vit-base-patch32'
    }
]

for model in models_to_download:
    os.makedirs(model['local_dir'], exist_ok=True)
    print(f"\nChecking repository: {model['repo_id']}")
    
    for f in model['files']:
        dest = os.path.join(model['local_dir'], f)
        
        if os.path.exists(dest):
            print(f'  Already exists, skipping: {f}')
        else:
            print(f'  Downloading: {f}...')
            hf_hub_download(
                repo_id=model['repo_id'],
                filename=f,
                local_dir=model['local_dir']
            )

print('\nAll downloads complete!')
