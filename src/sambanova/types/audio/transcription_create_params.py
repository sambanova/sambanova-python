# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["TranscriptionCreateParams"]


class TranscriptionCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """
    The audio file object to transcribe or translate, in one of these formats: FLAC,
    MP3, MP4, MPEG, MPGA, M4A, Ogg, WAV, or WebM format. File size limit is 25MB.
    """

    model: Required[Union[str, Literal["Whisper-Large-v3"]]]
    """
    The model ID to use See available
    [models](https://docs.sambanova.ai/docs/en/models/sambacloud-models)
    """

    language: Optional[
        Literal[
            "en",
            "zh",
            "de",
            "es",
            "ru",
            "ko",
            "fr",
            "ja",
            "pt",
            "tr",
            "pl",
            "ca",
            "nl",
            "ar",
            "sv",
            "it",
            "id",
            "hi",
            "fi",
            "vi",
            "he",
            "uk",
            "el",
            "ms",
            "cs",
            "ro",
            "da",
            "hu",
            "ta",
            "no",
            "th",
            "ur",
            "hr",
            "bg",
            "lt",
            "la",
            "mi",
            "ml",
            "cy",
            "sk",
            "te",
            "fa",
            "lv",
            "bn",
            "sr",
            "az",
            "sl",
            "kn",
            "et",
            "mk",
            "br",
            "eu",
            "is",
            "hy",
            "ne",
            "mn",
            "bs",
            "kk",
            "sq",
            "sw",
            "gl",
            "mr",
            "pa",
            "si",
            "km",
            "sn",
            "yo",
            "so",
            "af",
            "oc",
            "ka",
            "be",
            "tg",
            "sd",
            "gu",
            "am",
            "yi",
            "lo",
            "uz",
            "fo",
            "ht",
            "ps",
            "tk",
            "nn",
            "mt",
            "sa",
            "lb",
            "my",
            "bo",
            "tl",
            "mg",
            "as",
            "tt",
            "haw",
            "ln",
            "ha",
            "ba",
            "jw",
            "su",
            "yue",
        ]
    ]
    """Optional language of the input audio.

    Supplying the input language in ISO-639-1 (e.g. en) format will improve accuracy
    and latency.
    """

    prompt: Optional[str]
    """
    Optional text prompt provided to influence transcription Translation style or
    vocabulary. Example: “Please transcribe carefully, including pauses and
    hesitations.”
    """

    response_format: Literal["json", "text", "verbose_json", "srt", "vtt"]
    """The format of the output.

    `json` and `verbose_json` return a JSON object (`verbose_json` adds `task`,
    `language`, `duration` and `segments`); `text`, `srt` and `vtt` return plain
    text.
    """

    timestamp_granularities: List[Literal["segment"]]
    """The timestamp granularities to populate.

    Requires `response_format` set to `verbose_json`. Only `segment` is supported;
    segment timings are approximate within each 30-second audio chunk.
    """
