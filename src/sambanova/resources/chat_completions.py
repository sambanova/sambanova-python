# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import chat_completion_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ..types.chat_completion_create_response import ChatCompletionCreateResponse

__all__ = ["ChatCompletionsResource", "AsyncChatCompletionsResource"]


class ChatCompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return ChatCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sambanova-python#with_streaming_response
        """
        return ChatCompletionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[chat_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        response_format: chat_completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        stream_options: chat_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse:
        """
        Creates a model response for the given chat conversation.

        Args:
          max_tokens: Maximum number of tokens to generate.

          messages: A list of messages comprising the conversation so far.

          model: The name of the model to query.

          response_format: Ensures the model outputs a valid JSON.

          stop: Sequences where the API will stop generating tokens.

          stream: If set, partial message deltas will be sent.

          stream_options: Options for streaming response.

          temperature: Degree of randomness in the response.

          tools: A list of tools the model may call.

          top_k: Limit for token choices.

          top_p: Cumulative probability for token choices.

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
        stream: Literal[True],
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[chat_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        response_format: chat_completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream_options: chat_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ChatCompletionCreateResponse]:
        """
        Creates a model response for the given chat conversation.

        Args:
          stream: If set, partial message deltas will be sent.

          max_tokens: Maximum number of tokens to generate.

          messages: A list of messages comprising the conversation so far.

          model: The name of the model to query.

          response_format: Ensures the model outputs a valid JSON.

          stop: Sequences where the API will stop generating tokens.

          stream_options: Options for streaming response.

          temperature: Degree of randomness in the response.

          tools: A list of tools the model may call.

          top_k: Limit for token choices.

          top_p: Cumulative probability for token choices.

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
        stream: bool,
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[chat_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        response_format: chat_completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream_options: chat_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse | Stream[ChatCompletionCreateResponse]:
        """
        Creates a model response for the given chat conversation.

        Args:
          stream: If set, partial message deltas will be sent.

          max_tokens: Maximum number of tokens to generate.

          messages: A list of messages comprising the conversation so far.

          model: The name of the model to query.

          response_format: Ensures the model outputs a valid JSON.

          stop: Sequences where the API will stop generating tokens.

          stream_options: Options for streaming response.

          temperature: Degree of randomness in the response.

          tools: A list of tools the model may call.

          top_k: Limit for token choices.

          top_p: Cumulative probability for token choices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def create(
        self,
        *,
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[chat_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        response_format: chat_completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: chat_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse | Stream[ChatCompletionCreateResponse]:
        return self._post(
            "/v1/chat/completions",
            body=maybe_transform(
                {
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "response_format": response_format,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                chat_completion_create_params.ChatCompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionCreateResponse,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionCreateResponse],
        )


class AsyncChatCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sambanova-python#with_streaming_response
        """
        return AsyncChatCompletionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[chat_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        response_format: chat_completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        stream_options: chat_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse:
        """
        Creates a model response for the given chat conversation.

        Args:
          max_tokens: Maximum number of tokens to generate.

          messages: A list of messages comprising the conversation so far.

          model: The name of the model to query.

          response_format: Ensures the model outputs a valid JSON.

          stop: Sequences where the API will stop generating tokens.

          stream: If set, partial message deltas will be sent.

          stream_options: Options for streaming response.

          temperature: Degree of randomness in the response.

          tools: A list of tools the model may call.

          top_k: Limit for token choices.

          top_p: Cumulative probability for token choices.

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
        stream: Literal[True],
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[chat_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        response_format: chat_completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream_options: chat_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ChatCompletionCreateResponse]:
        """
        Creates a model response for the given chat conversation.

        Args:
          stream: If set, partial message deltas will be sent.

          max_tokens: Maximum number of tokens to generate.

          messages: A list of messages comprising the conversation so far.

          model: The name of the model to query.

          response_format: Ensures the model outputs a valid JSON.

          stop: Sequences where the API will stop generating tokens.

          stream_options: Options for streaming response.

          temperature: Degree of randomness in the response.

          tools: A list of tools the model may call.

          top_k: Limit for token choices.

          top_p: Cumulative probability for token choices.

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
        stream: bool,
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[chat_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        response_format: chat_completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream_options: chat_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse | AsyncStream[ChatCompletionCreateResponse]:
        """
        Creates a model response for the given chat conversation.

        Args:
          stream: If set, partial message deltas will be sent.

          max_tokens: Maximum number of tokens to generate.

          messages: A list of messages comprising the conversation so far.

          model: The name of the model to query.

          response_format: Ensures the model outputs a valid JSON.

          stop: Sequences where the API will stop generating tokens.

          stream_options: Options for streaming response.

          temperature: Degree of randomness in the response.

          tools: A list of tools the model may call.

          top_k: Limit for token choices.

          top_p: Cumulative probability for token choices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def create(
        self,
        *,
        max_tokens: int | NotGiven = NOT_GIVEN,
        messages: Iterable[chat_completion_create_params.Message] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        response_format: chat_completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: chat_completion_create_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse | AsyncStream[ChatCompletionCreateResponse]:
        return await self._post(
            "/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "response_format": response_format,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                chat_completion_create_params.ChatCompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionCreateResponse,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionCreateResponse],
        )


class ChatCompletionsResourceWithRawResponse:
    def __init__(self, chat_completions: ChatCompletionsResource) -> None:
        self._chat_completions = chat_completions

        self.create = to_raw_response_wrapper(
            chat_completions.create,
        )


class AsyncChatCompletionsResourceWithRawResponse:
    def __init__(self, chat_completions: AsyncChatCompletionsResource) -> None:
        self._chat_completions = chat_completions

        self.create = async_to_raw_response_wrapper(
            chat_completions.create,
        )


class ChatCompletionsResourceWithStreamingResponse:
    def __init__(self, chat_completions: ChatCompletionsResource) -> None:
        self._chat_completions = chat_completions

        self.create = to_streamed_response_wrapper(
            chat_completions.create,
        )


class AsyncChatCompletionsResourceWithStreamingResponse:
    def __init__(self, chat_completions: AsyncChatCompletionsResource) -> None:
        self._chat_completions = chat_completions

        self.create = async_to_streamed_response_wrapper(
            chat_completions.create,
        )
