# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TranscriptionSegment"]


class TranscriptionSegment(BaseModel):
    """A segment of transcribed or translated text.

    Timings are exact at audio chunk boundaries and interpolated within a chunk. `tokens`, `avg_logprob`, `compression_ratio` and `no_speech_prob` are always empty or zero.
    """

    id: int
    """Index of the segment."""

    avg_logprob: float
    """Average logprob of the segment. Always zero."""

    compression_ratio: float
    """Compression ratio of the segment. Always zero."""

    end: float
    """End time of the segment in seconds."""

    no_speech_prob: float
    """Probability of no speech in the segment. Always zero."""

    seek: int
    """Seek offset of the segment."""

    start: float
    """Start time of the segment in seconds."""

    temperature: float
    """Temperature parameter used to generate the segment."""

    text: str
    """Text content of the segment."""

    tokens: List[int]
    """Token IDs of the text content. Always empty."""

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
