import ollama
try:
    models = ollama.list()
    print("Ollama list output type:", type(models))
    print("Ollama list output:", models)
    if 'models' in models:
        print("First model keys:", models['models'][0].keys() if models['models'] else "No models found")
except Exception as e:
    print(f"Error: {e}")
