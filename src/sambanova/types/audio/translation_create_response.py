# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .translation_response import TranslationResponse
from .translation_stream_response import TranslationStreamResponse

__all__ = ["TranslationCreateResponse"]

TranslationCreateResponse: TypeAlias = Union[TranslationResponse, TranslationStreamResponse]
