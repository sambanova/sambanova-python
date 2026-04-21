# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .chat_completion_response import ChatCompletionResponse
from .chat_completion_stream_response import ChatCompletionStreamResponse

__all__ = ["CompletionCreateResponse"]

CompletionCreateResponse: TypeAlias = Union[ChatCompletionResponse, ChatCompletionStreamResponse]
