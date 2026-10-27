# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transcription_segment import TranscriptionSegment

__all__ = ["TranslationResponse"]


class TranslationResponse(BaseModel):
    """Translation response json object"""

    text: str
    """audio file english text translation"""

    duration: Optional[float] = None
    """The duration of the input audio in seconds.

    Only returned with `response_format` set to `verbose_json`.
    """

    language: Optional[str] = None
    """The language of the input audio.

    Only returned with `response_format` set to `verbose_json`.
    """

    segments: Optional[List[TranscriptionSegment]] = None
    """Segments of the transcribed text with their timings.

    Only returned with `response_format` set to `verbose_json`.
    """

    task: Optional[Literal["transcribe", "translate"]] = None
    """The task performed. Only returned with `response_format` set to `verbose_json`."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
