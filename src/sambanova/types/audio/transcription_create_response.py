# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .transcription_response import TranscriptionResponse
from .transcription_stream_response import TranscriptionStreamResponse

__all__ = ["TranscriptionCreateResponse"]

TranscriptionCreateResponse: TypeAlias = Union[TranscriptionResponse, TranscriptionStreamResponse]
