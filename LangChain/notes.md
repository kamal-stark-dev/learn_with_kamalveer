## What problem does LangChain solve?
Imagine you have an LLM.
```py
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is LangChain?"
)

print(response.text)
```

This works, but real AI apps need much more:
- Chat history
- Memory
- RAG (Retrieval Augmented Generation)
- Tool calling
- Agents
- Structured outputs
- Multiple LLM providers 
- Streaming
- Chain of operations
- Vector databases

*Without LangChain*:
```
user_input > retrieve docs > format prompt > call llm > parse output > save memory > call tools > return response
```

We have to manually glue everything together. LangChain provides abstractions for all of this.

> **Abstraction**: The practice of hiding complex, underlying implementation details and showing only the essential features of an object to the user.
> 
> *example*: Think of a coofee machine. To get espresso, you only need to press a single button, you don't need to understand water pressure, internal temperature etc. The button is the abstract interface that hides the mechanical complexity.

Think of LangChain as Flask/FastAPI for AI applications. (Not required, but makes building complex systems much easier.)


