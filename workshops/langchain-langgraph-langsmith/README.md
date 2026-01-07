# LangChain · LangGraph · LangSmith Workshop Notes

These notes summarize a hands-on workshop covering **LangChain**,
**LangGraph**, and **LangSmith**, using **Groq LLMs**.

------------------------------------------------------------------------

## Overview

-   **LangChain**: Framework for building LLM-powered applications
-   **LangGraph**: Graph-based, stateful orchestration for agents and
    workflows
-   **LangSmith**: Tracing, debugging, and observability for LLM apps
-   **Groq**: High-speed inference for open-source LLMs

------------------------------------------------------------------------

## Useful Links

-   LangChain: https://www.langchain.com/
-   LangChain Docs:
    https://docs.langchain.com/oss/python/langchain/overview
-   Groq: https://groq.com/
-   Groq Console: https://console.groq.com/keys
-   LangSmith: https://smith.langchain.com/
-   Workshop Video: https://www.youtube.com/watch?v=za04rNvpHgY

------------------------------------------------------------------------

## Environment Setup

``` bash
pip install langchain-groq langchain-core
```

------------------------------------------------------------------------

## Using Groq with LangChain

### Import

``` python
from langchain_groq import ChatGroq
```

### Initialize LLM

``` python
llm = ChatGroq(
    api_key="groc_xxxx",
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=50
)
```

### Invoke Model

``` python
llm.invoke("Who are the top 5 cricketers in India?").content
```

------------------------------------------------------------------------

## Output Parsing

``` python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
chain = llm | parser

response = chain.invoke("Write a short poem for kids")
print(response)
```

------------------------------------------------------------------------

## LangSmith Tracing

### Set Environment Variables

``` python
import os

os.environ["LANGSMITH_API_KEY"] = "langsmith_xxxx"
os.environ["LANGSMITH_PROJECT"] = "workshop-dec"
os.environ["LANGSMITH_TRACING"] = "true"
```

### Traced Chain Execution

``` python
chain.invoke("Explain LangChain in simple terms")
```

All executions appear in the LangSmith dashboard.

------------------------------------------------------------------------

## LangGraph (Concept)

-   Enables multi-step, stateful workflows
-   Supports loops, retries, and agent coordination
-   Ideal for complex agent systems

------------------------------------------------------------------------

## Architecture

    User Prompt
       ↓
    Groq LLM (ChatGroq)
       ↓
    Output Parser
       ↓
    LangSmith (Tracing)

------------------------------------------------------------------------

## Key Takeaways

-   Use **LangChain** to compose LLM logic
-   Use **Groq** for fast inference
-   Use **LangSmith** for debugging and monitoring
-   Use **LangGraph** for advanced agent workflows

------------------------------------------------------------------------
