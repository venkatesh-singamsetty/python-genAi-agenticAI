## Workshop: Langchain Langgraph Langsmith

https://www.youtube.com/watch?v=za04rNvpHgY&t=2497s

https://www.langchain.com/

https://docs.langchain.com/oss/python/langchain/overview

https://openrouter.ai/

https://groq.com/
  https://console.groq.com/keys
    api key -> langsmith-workshop -> xxxxx
    https://console.groq.com/playground -> pick model -> llama-3.3-70b-versatile

https://docs.langchain.com/oss/python/integrations/providers/groq

https://colab.research.google.com/
https://colab.research.google.com/drive/1JXfx3hhnSZtP4cnrNrptlmjGIMmUsKgD#scrollTo=2NtgyheHQW1v
```
pip install langchain-groq
```

import langchain.groq

```
from langchain_groq import ChatGroq
```

chatgroq is a method to access the llm model using api key
chatgroq(api key, model name, temper)

https://docs.langchain.com/oss/python/integrations/chat/groq
```
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    # other params...
)
```

```
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key="xxxxx",
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=50
)
```

```
llm.invoke('who are the top 5 crickers in India?')
```

```
llm.invoke('who are the top 5 crickers in India?').content
```

```
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key="xxxxx",
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None
)
```

```
print(llm.invoke('who are the top 5 crickers in India?').content)
```

StrOutputParser in langchain -> https://reference.langchain.com/python/langchain_core/output_parsers/
install -> langchain-core
```
pip install langchain-core

dir(langchain_core)

import langchain_core

dir(langchain_core)

from langchain_core.output_parsers import StrOutputParser
```

```
from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key="xxxxx",
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None
)

parser=StrOutputParser()
chain=llm|parser
response=chain.invoke('tell about a poem on kid')
print(response)
```

https://smith.langchain.com/

https://smith.langchain.com/o/def1b265-9a57-4722-81b6-4bec086fd20f?paginationModel=%7B%22pageIndex%22%3A0%2C%22pageSize%22%3A5%7D

https://smith.langchain.com/o/def1b265-9a57-4722-81b6-4bec086fd20f/settings/apikeys
langsmith-workshop -> yyyyy

```
LANGCHAIN_API_KEY="yyyyy"
LANGCHAIN_PROJECT="workshop-dec"
```

```
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["LANGSMITH_API_KEY"]='yyyyy'
os.environ["LANGSMITH_PROJECT"]='workshop-dec'
os.environ["LANGSMITH_TRACING"]='true'

llm = ChatGroq(
    api_key="xxxxx",
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None
)

parser=StrOutputParser()
chain=llm|parser
response=chain.invoke('tell about a poem on kid')
print(response)
```
