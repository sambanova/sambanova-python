# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, Mapping, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, required_args, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...types.audio import transcription_create_params
from ..._base_client import make_request_options
from ...types.audio.transcription_create_response import TranscriptionCreateResponse
from ...types.audio.transcription_stream_response import TranscriptionStreamResponse

__all__ = ["TranscriptionsResource", "AsyncTranscriptionsResource"]


class TranscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sambanova/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return TranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sambanova/sambanova-python#with_streaming_response
        """
        return TranscriptionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["Whisper-Large-v3"]],
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
        | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        response_format: Literal["json", "text"] | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: Optional[transcription_create_params.StreamOptions] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptionCreateResponse:
        """
        Transcribes audio into the input language.

        Args:
          file: The audio file object to transcribe or translate, in one of these formats: FLAC,
              MP3, MP4, MPEG, MPGA, M4A, Ogg, WAV, or WebM format. File size limit is 25MB.

          model: The model ID to use See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          language: Optional language of the input audio. Supplying the input language in ISO-639-1
              (e.g. en) format will improve accuracy and latency.

          prompt: Optional text prompt provided to influence transcription Translation style or
              vocabulary. Example: “Please transcribe carefully, including pauses and
              hesitations.”

          response_format: Output format JSON or text.

          stream: Enables streaming responses.

          stream_options: Optional settings that apply when `stream` is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["Whisper-Large-v3"]],
        stream: Literal[True],
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
        | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        response_format: Literal["json", "text"] | Omit = omit,
        stream_options: Optional[transcription_create_params.StreamOptions] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[TranscriptionStreamResponse]:
        """
        Transcribes audio into the input language.

        Args:
          file: The audio file object to transcribe or translate, in one of these formats: FLAC,
              MP3, MP4, MPEG, MPGA, M4A, Ogg, WAV, or WebM format. File size limit is 25MB.

          model: The model ID to use See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          stream: Enables streaming responses.

          language: Optional language of the input audio. Supplying the input language in ISO-639-1
              (e.g. en) format will improve accuracy and latency.

          prompt: Optional text prompt provided to influence transcription Translation style or
              vocabulary. Example: “Please transcribe carefully, including pauses and
              hesitations.”

          response_format: Output format JSON or text.

          stream_options: Optional settings that apply when `stream` is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["Whisper-Large-v3"]],
        stream: bool,
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
        | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        response_format: Literal["json", "text"] | Omit = omit,
        stream_options: Optional[transcription_create_params.StreamOptions] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptionCreateResponse | Stream[TranscriptionStreamResponse]:
        """
        Transcribes audio into the input language.

        Args:
          file: The audio file object to transcribe or translate, in one of these formats: FLAC,
              MP3, MP4, MPEG, MPGA, M4A, Ogg, WAV, or WebM format. File size limit is 25MB.

          model: The model ID to use See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          stream: Enables streaming responses.

          language: Optional language of the input audio. Supplying the input language in ISO-639-1
              (e.g. en) format will improve accuracy and latency.

          prompt: Optional text prompt provided to influence transcription Translation style or
              vocabulary. Example: “Please transcribe carefully, including pauses and
              hesitations.”

          response_format: Output format JSON or text.

          stream_options: Optional settings that apply when `stream` is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["file", "model"], ["file", "model", "stream"])
    def create(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["Whisper-Large-v3"]],
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
        | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        response_format: Literal["json", "text"] | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: Optional[transcription_create_params.StreamOptions] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptionCreateResponse | Stream[TranscriptionStreamResponse]:
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "stream": stream,
                "stream_options": stream_options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/audio/transcriptions",
            body=maybe_transform(
                body,
                transcription_create_params.TranscriptionCreateParamsStreaming
                if stream
                else transcription_create_params.TranscriptionCreateParamsNonStreaming,
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, TranscriptionCreateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=Stream[TranscriptionStreamResponse],
        )


class AsyncTranscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sambanova/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sambanova/sambanova-python#with_streaming_response
        """
        return AsyncTranscriptionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["Whisper-Large-v3"]],
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
        | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        response_format: Literal["json", "text"] | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: Optional[transcription_create_params.StreamOptions] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptionCreateResponse:
        """
        Transcribes audio into the input language.

        Args:
          file: The audio file object to transcribe or translate, in one of these formats: FLAC,
              MP3, MP4, MPEG, MPGA, M4A, Ogg, WAV, or WebM format. File size limit is 25MB.

          model: The model ID to use See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          language: Optional language of the input audio. Supplying the input language in ISO-639-1
              (e.g. en) format will improve accuracy and latency.

          prompt: Optional text prompt provided to influence transcription Translation style or
              vocabulary. Example: “Please transcribe carefully, including pauses and
              hesitations.”

          response_format: Output format JSON or text.

          stream: Enables streaming responses.

          stream_options: Optional settings that apply when `stream` is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["Whisper-Large-v3"]],
        stream: Literal[True],
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
        | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        response_format: Literal["json", "text"] | Omit = omit,
        stream_options: Optional[transcription_create_params.StreamOptions] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[TranscriptionStreamResponse]:
        """
        Transcribes audio into the input language.

        Args:
          file: The audio file object to transcribe or translate, in one of these formats: FLAC,
              MP3, MP4, MPEG, MPGA, M4A, Ogg, WAV, or WebM format. File size limit is 25MB.

          model: The model ID to use See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          stream: Enables streaming responses.

          language: Optional language of the input audio. Supplying the input language in ISO-639-1
              (e.g. en) format will improve accuracy and latency.

          prompt: Optional text prompt provided to influence transcription Translation style or
              vocabulary. Example: “Please transcribe carefully, including pauses and
              hesitations.”

          response_format: Output format JSON or text.

          stream_options: Optional settings that apply when `stream` is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["Whisper-Large-v3"]],
        stream: bool,
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
        | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        response_format: Literal["json", "text"] | Omit = omit,
        stream_options: Optional[transcription_create_params.StreamOptions] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptionCreateResponse | AsyncStream[TranscriptionStreamResponse]:
        """
        Transcribes audio into the input language.

        Args:
          file: The audio file object to transcribe or translate, in one of these formats: FLAC,
              MP3, MP4, MPEG, MPGA, M4A, Ogg, WAV, or WebM format. File size limit is 25MB.

          model: The model ID to use See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          stream: Enables streaming responses.

          language: Optional language of the input audio. Supplying the input language in ISO-639-1
              (e.g. en) format will improve accuracy and latency.

          prompt: Optional text prompt provided to influence transcription Translation style or
              vocabulary. Example: “Please transcribe carefully, including pauses and
              hesitations.”

          response_format: Output format JSON or text.

          stream_options: Optional settings that apply when `stream` is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["file", "model"], ["file", "model", "stream"])
    async def create(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["Whisper-Large-v3"]],
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
        | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        response_format: Literal["json", "text"] | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: Optional[transcription_create_params.StreamOptions] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranscriptionCreateResponse | AsyncStream[TranscriptionStreamResponse]:
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "stream": stream,
                "stream_options": stream_options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/audio/transcriptions",
            body=await async_maybe_transform(
                body,
                transcription_create_params.TranscriptionCreateParamsStreaming
                if stream
                else transcription_create_params.TranscriptionCreateParamsNonStreaming,
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, TranscriptionCreateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=AsyncStream[TranscriptionStreamResponse],
        )


class TranscriptionsResourceWithRawResponse:
    def __init__(self, transcriptions: TranscriptionsResource) -> None:
        self._transcriptions = transcriptions

        self.create = to_raw_response_wrapper(
            transcriptions.create,
        )


class AsyncTranscriptionsResourceWithRawResponse:
    def __init__(self, transcriptions: AsyncTranscriptionsResource) -> None:
        self._transcriptions = transcriptions

        self.create = async_to_raw_response_wrapper(
            transcriptions.create,
        )


class TranscriptionsResourceWithStreamingResponse:
    def __init__(self, transcriptions: TranscriptionsResource) -> None:
        self._transcriptions = transcriptions

        self.create = to_streamed_response_wrapper(
            transcriptions.create,
        )


class AsyncTranscriptionsResourceWithStreamingResponse:
    def __init__(self, transcriptions: AsyncTranscriptionsResource) -> None:
        self._transcriptions = transcriptions

        self.create = async_to_streamed_response_wrapper(
            transcriptions.create,
        )
