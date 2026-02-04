# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .general_error import GeneralError
from .model_output_error import ModelOutputError
from .chat_completion_response import ChatCompletionResponse
from .chat_completion_stream_response import ChatCompletionStreamResponse

__all__ = ["CompletionCreateResponse"]

CompletionCreateResponse: TypeAlias = Union[
    ChatCompletionResponse, ChatCompletionStreamResponse, ModelOutputError, GeneralError
]
