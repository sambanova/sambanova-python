# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = [
    "TranslationCreateParamsBase",
    "StreamOptions",
    "TranslationCreateParamsNonStreaming",
    "TranslationCreateParamsStreaming",
]


class TranslationCreateParamsBase(TypedDict, total=False):
    file: Required[FileTypes]
    """
    The audio file object to transcribe or translate, in one of these formats: FLAC,
    MP3, MP4, MPEG, MPGA, M4A, Ogg, WAV, or WebM format. File size limit is 25MB.
    """

    model: Required[Union[str, Literal["Whisper-Large-v3"]]]
    """
    The model ID to use See available
    [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)
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

    response_format: Literal["json", "text"]
    """Output format JSON or text."""

    stream_options: Optional[StreamOptions]
    """Optional settings that apply when `stream` is true."""


class StreamOptions(TypedDict, total=False):
    include_usage: Optional[bool]
    """
    If true and `stream` is enabled, optional usage metadata will be included in the
    last streamed response event.
    """


class TranslationCreateParamsNonStreaming(TranslationCreateParamsBase, total=False):
    stream: Literal[False]
    """Enables streaming responses."""


class TranslationCreateParamsStreaming(TranslationCreateParamsBase):
    stream: Required[Literal[True]]
    """Enables streaming responses."""


TranslationCreateParams = Union[TranslationCreateParamsNonStreaming, TranslationCreateParamsStreaming]
