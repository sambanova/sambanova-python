# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..types import message_create_params, message_count_tokens_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.message_stream_event import MessageStreamEvent
from ..types.message_create_response import MessageCreateResponse
from ..types.message_count_tokens_response import MessageCountTokensResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sambanova/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sambanova/sambanova-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
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
                "DeepSeek-V3.1-cb",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-V3.2",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Qwen3-235B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
                "MiniMax-M2.5",
                "MiniMax-M2.7",
                "gemma-3-12b-it",
            ],
        ],
        container: Optional[str] | Omit = omit,
        metadata: message_create_params.Metadata | Omit = omit,
        service_tier: Optional[Literal["auto", "standard_only"]] | Omit = omit,
        stop_sequences: Optional[SequenceNotStr[str]] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        system: Union[str, Iterable[message_create_params.SystemSystemTextBlockArray]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thinking: message_create_params.Thinking | Omit = omit,
        tool_choice: Optional[message_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse:
        """Anthropic Messages API compatible endpoint.

        Generates a model response for the
        supplied conversation. Authentication accepts either the bearer
        `Authorization: Bearer <key>` header (SambaNova SDK default) or the `x-api-key`
        header (Anthropic SDK default); the same API key is used in both cases. When
        `stream: true` is set, the response is a sequence of Server-Sent Events whose
        payloads conform to `MessageStreamEvent`; otherwise the response is a single
        `Message` object.

        Args:
          max_tokens: Maximum number of tokens to generate. The combined input + output token count is
              bounded by the model's context window.

          messages: Conversation turns.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/docs/en/models/sambacloud-models)

          container: Existing code-execution container ID to reuse. **In v1**: silently dropped

          metadata: Free-form metadata attached to the request. Currently only `user_id` Additional
              fields are accepted but ignored.

          service_tier: Service-tier preference. **In v1**: silently dropped

          stop_sequences: Custom strings that, when generated, cause the model to stop.

          stream: If true, the response is a sequence of Server-Sent Events whose payloads conform
              to `MessageStreamEvent`.

          system: System prompt for the conversation. Accepts either a single string (most common)
              or an array of text blocks (used when individual segments need `cache_control`
              markers). Multiple text blocks are joined with newlines and prepended to the
              conversation as a `role: system` message.

          temperature: Sampling temperature in `[0.0, 2.0]`. Higher values produce more random output,
              lower values more deterministic. Adjust only one of `temperature`, `top_p`,
              `top_k`.

          thinking: Controls Anthropic-style extended thinking. **In v1**: only `type:"disabled"` is
              silently accepted as a no-op; `type:"enabled"` and `type:"adaptive"` return a
              400 `invalid_request_error` (`unsupported_parameter`).

          tool_choice: How the model should choose from the provided tools.

          tools: Tool definitions the model may call.

          top_k: Top-k sampling. Considers only the K most likely tokens at each step. Set to 0
              to disable.

          top_p: Nucleus sampling. Considers tokens with cumulative probability mass up to
              `top_p`.

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
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
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
                "DeepSeek-V3.1-cb",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-V3.2",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Qwen3-235B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
                "MiniMax-M2.5",
                "MiniMax-M2.7",
                "gemma-3-12b-it",
            ],
        ],
        stream: Literal[True],
        container: Optional[str] | Omit = omit,
        metadata: message_create_params.Metadata | Omit = omit,
        service_tier: Optional[Literal["auto", "standard_only"]] | Omit = omit,
        stop_sequences: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Union[str, Iterable[message_create_params.SystemSystemTextBlockArray]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thinking: message_create_params.Thinking | Omit = omit,
        tool_choice: Optional[message_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[MessageStreamEvent]:
        """Anthropic Messages API compatible endpoint.

        Generates a model response for the
        supplied conversation. Authentication accepts either the bearer
        `Authorization: Bearer <key>` header (SambaNova SDK default) or the `x-api-key`
        header (Anthropic SDK default); the same API key is used in both cases. When
        `stream: true` is set, the response is a sequence of Server-Sent Events whose
        payloads conform to `MessageStreamEvent`; otherwise the response is a single
        `Message` object.

        Args:
          max_tokens: Maximum number of tokens to generate. The combined input + output token count is
              bounded by the model's context window.

          messages: Conversation turns.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/docs/en/models/sambacloud-models)

          stream: If true, the response is a sequence of Server-Sent Events whose payloads conform
              to `MessageStreamEvent`.

          container: Existing code-execution container ID to reuse. **In v1**: silently dropped

          metadata: Free-form metadata attached to the request. Currently only `user_id` Additional
              fields are accepted but ignored.

          service_tier: Service-tier preference. **In v1**: silently dropped

          stop_sequences: Custom strings that, when generated, cause the model to stop.

          system: System prompt for the conversation. Accepts either a single string (most common)
              or an array of text blocks (used when individual segments need `cache_control`
              markers). Multiple text blocks are joined with newlines and prepended to the
              conversation as a `role: system` message.

          temperature: Sampling temperature in `[0.0, 2.0]`. Higher values produce more random output,
              lower values more deterministic. Adjust only one of `temperature`, `top_p`,
              `top_k`.

          thinking: Controls Anthropic-style extended thinking. **In v1**: only `type:"disabled"` is
              silently accepted as a no-op; `type:"enabled"` and `type:"adaptive"` return a
              400 `invalid_request_error` (`unsupported_parameter`).

          tool_choice: How the model should choose from the provided tools.

          tools: Tool definitions the model may call.

          top_k: Top-k sampling. Considers only the K most likely tokens at each step. Set to 0
              to disable.

          top_p: Nucleus sampling. Considers tokens with cumulative probability mass up to
              `top_p`.

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
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
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
                "DeepSeek-V3.1-cb",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-V3.2",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Qwen3-235B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
                "MiniMax-M2.5",
                "MiniMax-M2.7",
                "gemma-3-12b-it",
            ],
        ],
        stream: bool,
        container: Optional[str] | Omit = omit,
        metadata: message_create_params.Metadata | Omit = omit,
        service_tier: Optional[Literal["auto", "standard_only"]] | Omit = omit,
        stop_sequences: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Union[str, Iterable[message_create_params.SystemSystemTextBlockArray]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thinking: message_create_params.Thinking | Omit = omit,
        tool_choice: Optional[message_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse | Stream[MessageStreamEvent]:
        """Anthropic Messages API compatible endpoint.

        Generates a model response for the
        supplied conversation. Authentication accepts either the bearer
        `Authorization: Bearer <key>` header (SambaNova SDK default) or the `x-api-key`
        header (Anthropic SDK default); the same API key is used in both cases. When
        `stream: true` is set, the response is a sequence of Server-Sent Events whose
        payloads conform to `MessageStreamEvent`; otherwise the response is a single
        `Message` object.

        Args:
          max_tokens: Maximum number of tokens to generate. The combined input + output token count is
              bounded by the model's context window.

          messages: Conversation turns.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/docs/en/models/sambacloud-models)

          stream: If true, the response is a sequence of Server-Sent Events whose payloads conform
              to `MessageStreamEvent`.

          container: Existing code-execution container ID to reuse. **In v1**: silently dropped

          metadata: Free-form metadata attached to the request. Currently only `user_id` Additional
              fields are accepted but ignored.

          service_tier: Service-tier preference. **In v1**: silently dropped

          stop_sequences: Custom strings that, when generated, cause the model to stop.

          system: System prompt for the conversation. Accepts either a single string (most common)
              or an array of text blocks (used when individual segments need `cache_control`
              markers). Multiple text blocks are joined with newlines and prepended to the
              conversation as a `role: system` message.

          temperature: Sampling temperature in `[0.0, 2.0]`. Higher values produce more random output,
              lower values more deterministic. Adjust only one of `temperature`, `top_p`,
              `top_k`.

          thinking: Controls Anthropic-style extended thinking. **In v1**: only `type:"disabled"` is
              silently accepted as a no-op; `type:"enabled"` and `type:"adaptive"` return a
              400 `invalid_request_error` (`unsupported_parameter`).

          tool_choice: How the model should choose from the provided tools.

          tools: Tool definitions the model may call.

          top_k: Top-k sampling. Considers only the K most likely tokens at each step. Set to 0
              to disable.

          top_p: Nucleus sampling. Considers tokens with cumulative probability mass up to
              `top_p`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["max_tokens", "messages", "model"], ["max_tokens", "messages", "model", "stream"])
    def create(
        self,
        *,
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
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
                "DeepSeek-V3.1-cb",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-V3.2",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Qwen3-235B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
                "MiniMax-M2.5",
                "MiniMax-M2.7",
                "gemma-3-12b-it",
            ],
        ],
        container: Optional[str] | Omit = omit,
        metadata: message_create_params.Metadata | Omit = omit,
        service_tier: Optional[Literal["auto", "standard_only"]] | Omit = omit,
        stop_sequences: Optional[SequenceNotStr[str]] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        system: Union[str, Iterable[message_create_params.SystemSystemTextBlockArray]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thinking: message_create_params.Thinking | Omit = omit,
        tool_choice: Optional[message_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse | Stream[MessageStreamEvent]:
        extra_headers = {**strip_not_given({"anthropic-version": anthropic_version}), **(extra_headers or {})}
        return self._post(
            "/messages",
            body=maybe_transform(
                {
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "container": container,
                    "metadata": metadata,
                    "service_tier": service_tier,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "system": system,
                    "temperature": temperature,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                message_create_params.MessageCreateParamsStreaming
                if stream
                else message_create_params.MessageCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(Any, MessageCreateResponse),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=Stream[MessageStreamEvent],
        )

    def count_tokens(
        self,
        *,
        messages: Iterable[message_count_tokens_params.Message],
        model: str,
        system: Union[str, Iterable[message_count_tokens_params.SystemSystemTextBlockArray]] | Omit = omit,
        thinking: message_count_tokens_params.Thinking | Omit = omit,
        tool_choice: Optional[message_count_tokens_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_count_tokens_params.Tool]] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCountTokensResponse:
        """Anthropic `count_tokens` compatible endpoint.

        Returns the number of input tokens
        that would be consumed by a `POST /messages` call with the same prompt content
        (system, messages, tools, tool_choice). Authentication accepts either the bearer
        `Authorization: Bearer <key>` header (SambaNova SDK default) or the `x-api-key`
        header (Anthropic SDK default); the same API key is used in both cases.

        Args:
          messages: Conversation turns.

          model: Model identifier.

          system: System prompt for the conversation. Accepts either a single string (most common)
              or an array of text blocks (used when individual segments need `cache_control`
              markers). Multiple text blocks are joined with newlines and prepended to the
              conversation as a `role: system` message.

          thinking: Controls Anthropic-style extended thinking. **In v1**: only `type:"disabled"` is
              silently accepted as a no-op; `type:"enabled"` and `type:"adaptive"` return a
              400 `invalid_request_error` (`unsupported_parameter`).

          tool_choice: How the model should choose from the provided tools.

          tools: Tool definitions the model may call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"anthropic-version": anthropic_version}), **(extra_headers or {})}
        return self._post(
            "/messages/count_tokens",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "system": system,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                },
                message_count_tokens_params.MessageCountTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCountTokensResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sambanova/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sambanova/sambanova-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
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
                "DeepSeek-V3.1-cb",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-V3.2",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Qwen3-235B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
                "MiniMax-M2.5",
                "MiniMax-M2.7",
                "gemma-3-12b-it",
            ],
        ],
        container: Optional[str] | Omit = omit,
        metadata: message_create_params.Metadata | Omit = omit,
        service_tier: Optional[Literal["auto", "standard_only"]] | Omit = omit,
        stop_sequences: Optional[SequenceNotStr[str]] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        system: Union[str, Iterable[message_create_params.SystemSystemTextBlockArray]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thinking: message_create_params.Thinking | Omit = omit,
        tool_choice: Optional[message_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse:
        """Anthropic Messages API compatible endpoint.

        Generates a model response for the
        supplied conversation. Authentication accepts either the bearer
        `Authorization: Bearer <key>` header (SambaNova SDK default) or the `x-api-key`
        header (Anthropic SDK default); the same API key is used in both cases. When
        `stream: true` is set, the response is a sequence of Server-Sent Events whose
        payloads conform to `MessageStreamEvent`; otherwise the response is a single
        `Message` object.

        Args:
          max_tokens: Maximum number of tokens to generate. The combined input + output token count is
              bounded by the model's context window.

          messages: Conversation turns.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/docs/en/models/sambacloud-models)

          container: Existing code-execution container ID to reuse. **In v1**: silently dropped

          metadata: Free-form metadata attached to the request. Currently only `user_id` Additional
              fields are accepted but ignored.

          service_tier: Service-tier preference. **In v1**: silently dropped

          stop_sequences: Custom strings that, when generated, cause the model to stop.

          stream: If true, the response is a sequence of Server-Sent Events whose payloads conform
              to `MessageStreamEvent`.

          system: System prompt for the conversation. Accepts either a single string (most common)
              or an array of text blocks (used when individual segments need `cache_control`
              markers). Multiple text blocks are joined with newlines and prepended to the
              conversation as a `role: system` message.

          temperature: Sampling temperature in `[0.0, 2.0]`. Higher values produce more random output,
              lower values more deterministic. Adjust only one of `temperature`, `top_p`,
              `top_k`.

          thinking: Controls Anthropic-style extended thinking. **In v1**: only `type:"disabled"` is
              silently accepted as a no-op; `type:"enabled"` and `type:"adaptive"` return a
              400 `invalid_request_error` (`unsupported_parameter`).

          tool_choice: How the model should choose from the provided tools.

          tools: Tool definitions the model may call.

          top_k: Top-k sampling. Considers only the K most likely tokens at each step. Set to 0
              to disable.

          top_p: Nucleus sampling. Considers tokens with cumulative probability mass up to
              `top_p`.

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
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
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
                "DeepSeek-V3.1-cb",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-V3.2",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Qwen3-235B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
                "MiniMax-M2.5",
                "MiniMax-M2.7",
                "gemma-3-12b-it",
            ],
        ],
        stream: Literal[True],
        container: Optional[str] | Omit = omit,
        metadata: message_create_params.Metadata | Omit = omit,
        service_tier: Optional[Literal["auto", "standard_only"]] | Omit = omit,
        stop_sequences: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Union[str, Iterable[message_create_params.SystemSystemTextBlockArray]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thinking: message_create_params.Thinking | Omit = omit,
        tool_choice: Optional[message_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[MessageStreamEvent]:
        """Anthropic Messages API compatible endpoint.

        Generates a model response for the
        supplied conversation. Authentication accepts either the bearer
        `Authorization: Bearer <key>` header (SambaNova SDK default) or the `x-api-key`
        header (Anthropic SDK default); the same API key is used in both cases. When
        `stream: true` is set, the response is a sequence of Server-Sent Events whose
        payloads conform to `MessageStreamEvent`; otherwise the response is a single
        `Message` object.

        Args:
          max_tokens: Maximum number of tokens to generate. The combined input + output token count is
              bounded by the model's context window.

          messages: Conversation turns.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/docs/en/models/sambacloud-models)

          stream: If true, the response is a sequence of Server-Sent Events whose payloads conform
              to `MessageStreamEvent`.

          container: Existing code-execution container ID to reuse. **In v1**: silently dropped

          metadata: Free-form metadata attached to the request. Currently only `user_id` Additional
              fields are accepted but ignored.

          service_tier: Service-tier preference. **In v1**: silently dropped

          stop_sequences: Custom strings that, when generated, cause the model to stop.

          system: System prompt for the conversation. Accepts either a single string (most common)
              or an array of text blocks (used when individual segments need `cache_control`
              markers). Multiple text blocks are joined with newlines and prepended to the
              conversation as a `role: system` message.

          temperature: Sampling temperature in `[0.0, 2.0]`. Higher values produce more random output,
              lower values more deterministic. Adjust only one of `temperature`, `top_p`,
              `top_k`.

          thinking: Controls Anthropic-style extended thinking. **In v1**: only `type:"disabled"` is
              silently accepted as a no-op; `type:"enabled"` and `type:"adaptive"` return a
              400 `invalid_request_error` (`unsupported_parameter`).

          tool_choice: How the model should choose from the provided tools.

          tools: Tool definitions the model may call.

          top_k: Top-k sampling. Considers only the K most likely tokens at each step. Set to 0
              to disable.

          top_p: Nucleus sampling. Considers tokens with cumulative probability mass up to
              `top_p`.

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
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
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
                "DeepSeek-V3.1-cb",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-V3.2",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Qwen3-235B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
                "MiniMax-M2.5",
                "MiniMax-M2.7",
                "gemma-3-12b-it",
            ],
        ],
        stream: bool,
        container: Optional[str] | Omit = omit,
        metadata: message_create_params.Metadata | Omit = omit,
        service_tier: Optional[Literal["auto", "standard_only"]] | Omit = omit,
        stop_sequences: Optional[SequenceNotStr[str]] | Omit = omit,
        system: Union[str, Iterable[message_create_params.SystemSystemTextBlockArray]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thinking: message_create_params.Thinking | Omit = omit,
        tool_choice: Optional[message_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse | AsyncStream[MessageStreamEvent]:
        """Anthropic Messages API compatible endpoint.

        Generates a model response for the
        supplied conversation. Authentication accepts either the bearer
        `Authorization: Bearer <key>` header (SambaNova SDK default) or the `x-api-key`
        header (Anthropic SDK default); the same API key is used in both cases. When
        `stream: true` is set, the response is a sequence of Server-Sent Events whose
        payloads conform to `MessageStreamEvent`; otherwise the response is a single
        `Message` object.

        Args:
          max_tokens: Maximum number of tokens to generate. The combined input + output token count is
              bounded by the model's context window.

          messages: Conversation turns.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/docs/en/models/sambacloud-models)

          stream: If true, the response is a sequence of Server-Sent Events whose payloads conform
              to `MessageStreamEvent`.

          container: Existing code-execution container ID to reuse. **In v1**: silently dropped

          metadata: Free-form metadata attached to the request. Currently only `user_id` Additional
              fields are accepted but ignored.

          service_tier: Service-tier preference. **In v1**: silently dropped

          stop_sequences: Custom strings that, when generated, cause the model to stop.

          system: System prompt for the conversation. Accepts either a single string (most common)
              or an array of text blocks (used when individual segments need `cache_control`
              markers). Multiple text blocks are joined with newlines and prepended to the
              conversation as a `role: system` message.

          temperature: Sampling temperature in `[0.0, 2.0]`. Higher values produce more random output,
              lower values more deterministic. Adjust only one of `temperature`, `top_p`,
              `top_k`.

          thinking: Controls Anthropic-style extended thinking. **In v1**: only `type:"disabled"` is
              silently accepted as a no-op; `type:"enabled"` and `type:"adaptive"` return a
              400 `invalid_request_error` (`unsupported_parameter`).

          tool_choice: How the model should choose from the provided tools.

          tools: Tool definitions the model may call.

          top_k: Top-k sampling. Considers only the K most likely tokens at each step. Set to 0
              to disable.

          top_p: Nucleus sampling. Considers tokens with cumulative probability mass up to
              `top_p`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["max_tokens", "messages", "model"], ["max_tokens", "messages", "model", "stream"])
    async def create(
        self,
        *,
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
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
                "DeepSeek-V3.1-cb",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-V3.2",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Qwen3-235B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
                "MiniMax-M2.5",
                "MiniMax-M2.7",
                "gemma-3-12b-it",
            ],
        ],
        container: Optional[str] | Omit = omit,
        metadata: message_create_params.Metadata | Omit = omit,
        service_tier: Optional[Literal["auto", "standard_only"]] | Omit = omit,
        stop_sequences: Optional[SequenceNotStr[str]] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        system: Union[str, Iterable[message_create_params.SystemSystemTextBlockArray]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        thinking: message_create_params.Thinking | Omit = omit,
        tool_choice: Optional[message_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse | AsyncStream[MessageStreamEvent]:
        extra_headers = {**strip_not_given({"anthropic-version": anthropic_version}), **(extra_headers or {})}
        return await self._post(
            "/messages",
            body=await async_maybe_transform(
                {
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "container": container,
                    "metadata": metadata,
                    "service_tier": service_tier,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "system": system,
                    "temperature": temperature,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                message_create_params.MessageCreateParamsStreaming
                if stream
                else message_create_params.MessageCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(Any, MessageCreateResponse),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=AsyncStream[MessageStreamEvent],
        )

    async def count_tokens(
        self,
        *,
        messages: Iterable[message_count_tokens_params.Message],
        model: str,
        system: Union[str, Iterable[message_count_tokens_params.SystemSystemTextBlockArray]] | Omit = omit,
        thinking: message_count_tokens_params.Thinking | Omit = omit,
        tool_choice: Optional[message_count_tokens_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[message_count_tokens_params.Tool]] | Omit = omit,
        anthropic_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCountTokensResponse:
        """Anthropic `count_tokens` compatible endpoint.

        Returns the number of input tokens
        that would be consumed by a `POST /messages` call with the same prompt content
        (system, messages, tools, tool_choice). Authentication accepts either the bearer
        `Authorization: Bearer <key>` header (SambaNova SDK default) or the `x-api-key`
        header (Anthropic SDK default); the same API key is used in both cases.

        Args:
          messages: Conversation turns.

          model: Model identifier.

          system: System prompt for the conversation. Accepts either a single string (most common)
              or an array of text blocks (used when individual segments need `cache_control`
              markers). Multiple text blocks are joined with newlines and prepended to the
              conversation as a `role: system` message.

          thinking: Controls Anthropic-style extended thinking. **In v1**: only `type:"disabled"` is
              silently accepted as a no-op; `type:"enabled"` and `type:"adaptive"` return a
              400 `invalid_request_error` (`unsupported_parameter`).

          tool_choice: How the model should choose from the provided tools.

          tools: Tool definitions the model may call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"anthropic-version": anthropic_version}), **(extra_headers or {})}
        return await self._post(
            "/messages/count_tokens",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "system": system,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                },
                message_count_tokens_params.MessageCountTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCountTokensResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_raw_response_wrapper(
            messages.create,
        )
        self.count_tokens = to_raw_response_wrapper(
            messages.count_tokens,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_raw_response_wrapper(
            messages.create,
        )
        self.count_tokens = async_to_raw_response_wrapper(
            messages.count_tokens,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_streamed_response_wrapper(
            messages.create,
        )
        self.count_tokens = to_streamed_response_wrapper(
            messages.count_tokens,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_streamed_response_wrapper(
            messages.create,
        )
        self.count_tokens = async_to_streamed_response_wrapper(
            messages.count_tokens,
        )
