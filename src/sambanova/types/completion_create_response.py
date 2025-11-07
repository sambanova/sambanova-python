# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .completion_response import CompletionResponse
from .completion_stream_response import CompletionStreamResponse

__all__ = ["CompletionCreateResponse"]

CompletionCreateResponse: TypeAlias = Union[CompletionResponse, CompletionStreamResponse]
