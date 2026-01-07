### OLAMA

llm -> paid, free

openai -> chatgpt

olama lets you run llm's locally

https://ollama.com/ -> Download and install ollama

models -> https://ollama.com/search -> https://ollama.com/library/gemma3 -> gemma3:270m

```bash
ollama --help

ollama ls

ollama pull gemma3:270m

ollama ls

ollama run gemma3:270m
>>> 10 points about roles and responsibility of genai developer in organization
>>> Do you have access for local path?

ollama pull deepseek-r1:1.5b

ollama run deepseek-r1:1.5b
>>> Do you have access for local path?
```

```bash
python3.12 -m venv .venv
source .venv/bin/activate

python3.12 -m pip install streamlit

python3.12 -m pip install ollama

python3.12 -m streamlit run app.py
```
