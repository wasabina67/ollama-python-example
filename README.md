# ollama-python-example
Ollama Python example

## Setup

### CPU only

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

```bash
docker exec -it ollama /bin/bash
```

```bash
ollama pull llama3.1
```

## Run

```bash
python run.py
```
