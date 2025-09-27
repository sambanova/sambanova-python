# Chat

## Completions

Types:

```python
from sambanova.types.chat import (
    ChatCompletionResponse,
    ChatCompletionStreamResponse,
    GeneralError,
    ModelOutputError,
    CompletionCreateResponse,
)
```

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/sambanova/resources/chat/completions.py">create</a>(\*\*<a href="src/sambanova/types/chat/completion_create_params.py">params</a>) -> <a href="./src/sambanova/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>

# Embeddings

Types:

```python
from sambanova.types import EmbeddingsResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/sambanova/resources/embeddings.py">create</a>(\*\*<a href="src/sambanova/types/embedding_create_params.py">params</a>) -> <a href="./src/sambanova/types/embeddings_response.py">EmbeddingsResponse</a></code>

# Audio

## Transcriptions

Types:

```python
from sambanova.types.audio import (
    TranscriptionResponse,
    TranscriptionStreamResponse,
    TranscriptionCreateResponse,
)
```

Methods:

- <code title="post /audio/transcriptions">client.audio.transcriptions.<a href="./src/sambanova/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/sambanova/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/sambanova/types/audio/transcription_create_response.py">TranscriptionCreateResponse</a></code>

## Translations

Types:

```python
from sambanova.types.audio import (
    TranslationResponse,
    TranslationStreamResponse,
    TranslationCreateResponse,
)
```

Methods:

- <code title="post /audio/translations">client.audio.translations.<a href="./src/sambanova/resources/audio/translations.py">create</a>(\*\*<a href="src/sambanova/types/audio/translation_create_params.py">params</a>) -> <a href="./src/sambanova/types/audio/translation_create_response.py">TranslationCreateResponse</a></code>

# Models

Types:

```python
from sambanova.types import ModelResponse, ModelsResponse
```

Methods:

- <code title="get /models/{model_id}">client.models.<a href="./src/sambanova/resources/models.py">retrieve</a>(model_id) -> <a href="./src/sambanova/types/model_response.py">ModelResponse</a></code>
- <code title="get /models">client.models.<a href="./src/sambanova/resources/models.py">list</a>() -> <a href="./src/sambanova/types/models_response.py">ModelsResponse</a></code>
