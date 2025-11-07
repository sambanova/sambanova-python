# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..types import completion_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.completion_create_response import CompletionCreateResponse
from ..types.completion_stream_response import CompletionStreamResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sambanova/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sambanova/sambanova-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        model: Union[
            str,
            Literal[
                "Meta-Llama-3.3-70B-Instruct",
                "Meta-Llama-3.2-1B-Instruct",
                "Meta-Llama-3.2-3B-Instruct",
                "Llama-3.2-11B-Vision-Instruct",
                "Llama-3.2-90B-Vision-Instruct",
                "Meta-Llama-3.1-8B-Instruct",
                "Meta-Llama-3.1-70B-Instruct",
                "Meta-Llama-3.1-405B-Instruct",
                "Qwen2.5-Coder-32B-Instruct",
                "Qwen2.5-72B-Instruct",
                "QwQ-32B-Preview",
                "Meta-Llama-Guard-3-8B",
                "DeepSeek-R1",
                "DeepSeek-R1-0528",
                "DeepSeek-V3-0324",
                "DeepSeek-V3.1",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
            ],
        ],
        prompt: str,
        do_sample: Optional[bool] | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """Create completion

        Args:
          model: The model ID to use (e.g.

        Meta-Llama-3.3-70B-Instruct). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          prompt: Prompt to send to the model.

          do_sample: If true, sampling is enabled during output generation. If false, deterministic
              decoding is used.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: This is not yet supported by our models. Modify the likelihood of specified
              tokens appearing in the completion.

          logprobs: This is not yet supported by our models. Whether to return log probabilities of
              the output tokens or not. If true, returns the log probabilities of each output
              token returned in the `content` of `message`.

          max_completion_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          n: This is not yet supported by our models. How many chat completion choices to
              generate for each input message.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          top_k: Amount limit of token choices. An alternative to sampling with temperature, the
              model considers the results of the first K tokens with higher probability. So 10
              means only the first 10 tokens with higher probability are considered. Is
              recommended altering this, top_p or temperature but not more than one of these.

          top_logprobs: This is not yet supported by our models. An integer between 0 and 20 specifying
              the number of most likely tokens to return at each token position, each with an
              associated log probability. `logprobs` must be set to `true` if this parameter
              is used.

          top_p: Cumulative probability for token choices. An alternative to sampling with
              temperature, called nucleus sampling, where the model considers the results of
              the tokens with top_p probability mass. So 0.1 means only the tokens comprising
              the top 10% probability mass are considered. Is recommended altering this, top_k
              or temperature but not more than one of these.

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
        model: Union[
            str,
            Literal[
                "Meta-Llama-3.3-70B-Instruct",
                "Meta-Llama-3.2-1B-Instruct",
                "Meta-Llama-3.2-3B-Instruct",
                "Llama-3.2-11B-Vision-Instruct",
                "Llama-3.2-90B-Vision-Instruct",
                "Meta-Llama-3.1-8B-Instruct",
                "Meta-Llama-3.1-70B-Instruct",
                "Meta-Llama-3.1-405B-Instruct",
                "Qwen2.5-Coder-32B-Instruct",
                "Qwen2.5-72B-Instruct",
                "QwQ-32B-Preview",
                "Meta-Llama-Guard-3-8B",
                "DeepSeek-R1",
                "DeepSeek-R1-0528",
                "DeepSeek-V3-0324",
                "DeepSeek-V3.1",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
            ],
        ],
        prompt: str,
        stream: Literal[True],
        do_sample: Optional[bool] | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[CompletionStreamResponse]:
        """Create completion

        Args:
          model: The model ID to use (e.g.

        Meta-Llama-3.3-70B-Instruct). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          prompt: Prompt to send to the model.

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          do_sample: If true, sampling is enabled during output generation. If false, deterministic
              decoding is used.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: This is not yet supported by our models. Modify the likelihood of specified
              tokens appearing in the completion.

          logprobs: This is not yet supported by our models. Whether to return log probabilities of
              the output tokens or not. If true, returns the log probabilities of each output
              token returned in the `content` of `message`.

          max_completion_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          n: This is not yet supported by our models. How many chat completion choices to
              generate for each input message.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          top_k: Amount limit of token choices. An alternative to sampling with temperature, the
              model considers the results of the first K tokens with higher probability. So 10
              means only the first 10 tokens with higher probability are considered. Is
              recommended altering this, top_p or temperature but not more than one of these.

          top_logprobs: This is not yet supported by our models. An integer between 0 and 20 specifying
              the number of most likely tokens to return at each token position, each with an
              associated log probability. `logprobs` must be set to `true` if this parameter
              is used.

          top_p: Cumulative probability for token choices. An alternative to sampling with
              temperature, called nucleus sampling, where the model considers the results of
              the tokens with top_p probability mass. So 0.1 means only the tokens comprising
              the top 10% probability mass are considered. Is recommended altering this, top_k
              or temperature but not more than one of these.

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
        model: Union[
            str,
            Literal[
                "Meta-Llama-3.3-70B-Instruct",
                "Meta-Llama-3.2-1B-Instruct",
                "Meta-Llama-3.2-3B-Instruct",
                "Llama-3.2-11B-Vision-Instruct",
                "Llama-3.2-90B-Vision-Instruct",
                "Meta-Llama-3.1-8B-Instruct",
                "Meta-Llama-3.1-70B-Instruct",
                "Meta-Llama-3.1-405B-Instruct",
                "Qwen2.5-Coder-32B-Instruct",
                "Qwen2.5-72B-Instruct",
                "QwQ-32B-Preview",
                "Meta-Llama-Guard-3-8B",
                "DeepSeek-R1",
                "DeepSeek-R1-0528",
                "DeepSeek-V3-0324",
                "DeepSeek-V3.1",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
            ],
        ],
        prompt: str,
        stream: bool,
        do_sample: Optional[bool] | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | Stream[CompletionStreamResponse]:
        """Create completion

        Args:
          model: The model ID to use (e.g.

        Meta-Llama-3.3-70B-Instruct). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          prompt: Prompt to send to the model.

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          do_sample: If true, sampling is enabled during output generation. If false, deterministic
              decoding is used.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: This is not yet supported by our models. Modify the likelihood of specified
              tokens appearing in the completion.

          logprobs: This is not yet supported by our models. Whether to return log probabilities of
              the output tokens or not. If true, returns the log probabilities of each output
              token returned in the `content` of `message`.

          max_completion_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          n: This is not yet supported by our models. How many chat completion choices to
              generate for each input message.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          top_k: Amount limit of token choices. An alternative to sampling with temperature, the
              model considers the results of the first K tokens with higher probability. So 10
              means only the first 10 tokens with higher probability are considered. Is
              recommended altering this, top_p or temperature but not more than one of these.

          top_logprobs: This is not yet supported by our models. An integer between 0 and 20 specifying
              the number of most likely tokens to return at each token position, each with an
              associated log probability. `logprobs` must be set to `true` if this parameter
              is used.

          top_p: Cumulative probability for token choices. An alternative to sampling with
              temperature, called nucleus sampling, where the model considers the results of
              the tokens with top_p probability mass. So 0.1 means only the tokens comprising
              the top 10% probability mass are considered. Is recommended altering this, top_k
              or temperature but not more than one of these.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt"], ["model", "prompt", "stream"])
    def create(
        self,
        *,
        model: Union[
            str,
            Literal[
                "Meta-Llama-3.3-70B-Instruct",
                "Meta-Llama-3.2-1B-Instruct",
                "Meta-Llama-3.2-3B-Instruct",
                "Llama-3.2-11B-Vision-Instruct",
                "Llama-3.2-90B-Vision-Instruct",
                "Meta-Llama-3.1-8B-Instruct",
                "Meta-Llama-3.1-70B-Instruct",
                "Meta-Llama-3.1-405B-Instruct",
                "Qwen2.5-Coder-32B-Instruct",
                "Qwen2.5-72B-Instruct",
                "QwQ-32B-Preview",
                "Meta-Llama-Guard-3-8B",
                "DeepSeek-R1",
                "DeepSeek-R1-0528",
                "DeepSeek-V3-0324",
                "DeepSeek-V3.1",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
            ],
        ],
        prompt: str,
        do_sample: Optional[bool] | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | Stream[CompletionStreamResponse]:
        return self._post(
            "/completions",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "do_sample": do_sample,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, CompletionCreateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=Stream[CompletionStreamResponse],
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sambanova/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sambanova/sambanova-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        model: Union[
            str,
            Literal[
                "Meta-Llama-3.3-70B-Instruct",
                "Meta-Llama-3.2-1B-Instruct",
                "Meta-Llama-3.2-3B-Instruct",
                "Llama-3.2-11B-Vision-Instruct",
                "Llama-3.2-90B-Vision-Instruct",
                "Meta-Llama-3.1-8B-Instruct",
                "Meta-Llama-3.1-70B-Instruct",
                "Meta-Llama-3.1-405B-Instruct",
                "Qwen2.5-Coder-32B-Instruct",
                "Qwen2.5-72B-Instruct",
                "QwQ-32B-Preview",
                "Meta-Llama-Guard-3-8B",
                "DeepSeek-R1",
                "DeepSeek-R1-0528",
                "DeepSeek-V3-0324",
                "DeepSeek-V3.1",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
            ],
        ],
        prompt: str,
        do_sample: Optional[bool] | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """Create completion

        Args:
          model: The model ID to use (e.g.

        Meta-Llama-3.3-70B-Instruct). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          prompt: Prompt to send to the model.

          do_sample: If true, sampling is enabled during output generation. If false, deterministic
              decoding is used.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: This is not yet supported by our models. Modify the likelihood of specified
              tokens appearing in the completion.

          logprobs: This is not yet supported by our models. Whether to return log probabilities of
              the output tokens or not. If true, returns the log probabilities of each output
              token returned in the `content` of `message`.

          max_completion_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          n: This is not yet supported by our models. How many chat completion choices to
              generate for each input message.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          top_k: Amount limit of token choices. An alternative to sampling with temperature, the
              model considers the results of the first K tokens with higher probability. So 10
              means only the first 10 tokens with higher probability are considered. Is
              recommended altering this, top_p or temperature but not more than one of these.

          top_logprobs: This is not yet supported by our models. An integer between 0 and 20 specifying
              the number of most likely tokens to return at each token position, each with an
              associated log probability. `logprobs` must be set to `true` if this parameter
              is used.

          top_p: Cumulative probability for token choices. An alternative to sampling with
              temperature, called nucleus sampling, where the model considers the results of
              the tokens with top_p probability mass. So 0.1 means only the tokens comprising
              the top 10% probability mass are considered. Is recommended altering this, top_k
              or temperature but not more than one of these.

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
        model: Union[
            str,
            Literal[
                "Meta-Llama-3.3-70B-Instruct",
                "Meta-Llama-3.2-1B-Instruct",
                "Meta-Llama-3.2-3B-Instruct",
                "Llama-3.2-11B-Vision-Instruct",
                "Llama-3.2-90B-Vision-Instruct",
                "Meta-Llama-3.1-8B-Instruct",
                "Meta-Llama-3.1-70B-Instruct",
                "Meta-Llama-3.1-405B-Instruct",
                "Qwen2.5-Coder-32B-Instruct",
                "Qwen2.5-72B-Instruct",
                "QwQ-32B-Preview",
                "Meta-Llama-Guard-3-8B",
                "DeepSeek-R1",
                "DeepSeek-R1-0528",
                "DeepSeek-V3-0324",
                "DeepSeek-V3.1",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
            ],
        ],
        prompt: str,
        stream: Literal[True],
        do_sample: Optional[bool] | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[CompletionStreamResponse]:
        """Create completion

        Args:
          model: The model ID to use (e.g.

        Meta-Llama-3.3-70B-Instruct). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          prompt: Prompt to send to the model.

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          do_sample: If true, sampling is enabled during output generation. If false, deterministic
              decoding is used.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: This is not yet supported by our models. Modify the likelihood of specified
              tokens appearing in the completion.

          logprobs: This is not yet supported by our models. Whether to return log probabilities of
              the output tokens or not. If true, returns the log probabilities of each output
              token returned in the `content` of `message`.

          max_completion_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          n: This is not yet supported by our models. How many chat completion choices to
              generate for each input message.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          top_k: Amount limit of token choices. An alternative to sampling with temperature, the
              model considers the results of the first K tokens with higher probability. So 10
              means only the first 10 tokens with higher probability are considered. Is
              recommended altering this, top_p or temperature but not more than one of these.

          top_logprobs: This is not yet supported by our models. An integer between 0 and 20 specifying
              the number of most likely tokens to return at each token position, each with an
              associated log probability. `logprobs` must be set to `true` if this parameter
              is used.

          top_p: Cumulative probability for token choices. An alternative to sampling with
              temperature, called nucleus sampling, where the model considers the results of
              the tokens with top_p probability mass. So 0.1 means only the tokens comprising
              the top 10% probability mass are considered. Is recommended altering this, top_k
              or temperature but not more than one of these.

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
        model: Union[
            str,
            Literal[
                "Meta-Llama-3.3-70B-Instruct",
                "Meta-Llama-3.2-1B-Instruct",
                "Meta-Llama-3.2-3B-Instruct",
                "Llama-3.2-11B-Vision-Instruct",
                "Llama-3.2-90B-Vision-Instruct",
                "Meta-Llama-3.1-8B-Instruct",
                "Meta-Llama-3.1-70B-Instruct",
                "Meta-Llama-3.1-405B-Instruct",
                "Qwen2.5-Coder-32B-Instruct",
                "Qwen2.5-72B-Instruct",
                "QwQ-32B-Preview",
                "Meta-Llama-Guard-3-8B",
                "DeepSeek-R1",
                "DeepSeek-R1-0528",
                "DeepSeek-V3-0324",
                "DeepSeek-V3.1",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
            ],
        ],
        prompt: str,
        stream: bool,
        do_sample: Optional[bool] | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | AsyncStream[CompletionStreamResponse]:
        """Create completion

        Args:
          model: The model ID to use (e.g.

        Meta-Llama-3.3-70B-Instruct). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          prompt: Prompt to send to the model.

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          do_sample: If true, sampling is enabled during output generation. If false, deterministic
              decoding is used.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: This is not yet supported by our models. Modify the likelihood of specified
              tokens appearing in the completion.

          logprobs: This is not yet supported by our models. Whether to return log probabilities of
              the output tokens or not. If true, returns the log probabilities of each output
              token returned in the `content` of `message`.

          max_completion_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          n: This is not yet supported by our models. How many chat completion choices to
              generate for each input message.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          top_k: Amount limit of token choices. An alternative to sampling with temperature, the
              model considers the results of the first K tokens with higher probability. So 10
              means only the first 10 tokens with higher probability are considered. Is
              recommended altering this, top_p or temperature but not more than one of these.

          top_logprobs: This is not yet supported by our models. An integer between 0 and 20 specifying
              the number of most likely tokens to return at each token position, each with an
              associated log probability. `logprobs` must be set to `true` if this parameter
              is used.

          top_p: Cumulative probability for token choices. An alternative to sampling with
              temperature, called nucleus sampling, where the model considers the results of
              the tokens with top_p probability mass. So 0.1 means only the tokens comprising
              the top 10% probability mass are considered. Is recommended altering this, top_k
              or temperature but not more than one of these.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt"], ["model", "prompt", "stream"])
    async def create(
        self,
        *,
        model: Union[
            str,
            Literal[
                "Meta-Llama-3.3-70B-Instruct",
                "Meta-Llama-3.2-1B-Instruct",
                "Meta-Llama-3.2-3B-Instruct",
                "Llama-3.2-11B-Vision-Instruct",
                "Llama-3.2-90B-Vision-Instruct",
                "Meta-Llama-3.1-8B-Instruct",
                "Meta-Llama-3.1-70B-Instruct",
                "Meta-Llama-3.1-405B-Instruct",
                "Qwen2.5-Coder-32B-Instruct",
                "Qwen2.5-72B-Instruct",
                "QwQ-32B-Preview",
                "Meta-Llama-Guard-3-8B",
                "DeepSeek-R1",
                "DeepSeek-R1-0528",
                "DeepSeek-V3-0324",
                "DeepSeek-V3.1",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
            ],
        ],
        prompt: str,
        do_sample: Optional[bool] | Omit = omit,
        frequency_penalty: float | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse | AsyncStream[CompletionStreamResponse]:
        return await self._post(
            "/completions",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "do_sample": do_sample,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, CompletionCreateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=AsyncStream[CompletionStreamResponse],
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
