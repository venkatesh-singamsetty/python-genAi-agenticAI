## Project
https://github.com/kodigitaccount/EDA_INTEGRATION_LLM

```bash
cd EDA_INTEGRATION_LLM/EDA_LLM_Integration

# work on code.ipynb

python3.12 -m venv .venv
source .venv/bin/activate
python3.12 -m pip install --upgrade pip

python3.12 -m pip install gradio pandas matplotlib seaborn ollama

python3.12 -m gradio app.py
```
