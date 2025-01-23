# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..types import chat_completion_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    required_args,
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
        This property can be used as a prefix for any HTTP method call to return
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
        messages: Iterable[chat_completion_create_params.Message],
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
            ],
        ],
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        stream_options: Optional[chat_completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_completion_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[chat_completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse:
        """
        Create chat-based completion

        Args:
          messages: A list of messages comprising the conversation so far.

          model: The model ID to use (e.g. Meta-Llama-3.3-70B-Instruct). See available
              [models](https://cloud.sambanova.ai/pricing)

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

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_object" }` enables JSON mode, which will check the message the
              model generates is valid JSON. **Important:** when using JSON mode, you **must**
              also instruct the model to produce JSON yourself via a system or user message.

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

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

          tools: A list of tools the model may call. Use this to provide a list of functions the
              model may generate JSON inputs for.

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
        messages: Iterable[chat_completion_create_params.Message],
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
            ],
        ],
        stream: Literal[True],
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        stream_options: Optional[chat_completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_completion_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[chat_completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ChatCompletionCreateResponse]:
        """
        Create chat-based completion

        Args:
          messages: A list of messages comprising the conversation so far.

          model: The model ID to use (e.g. Meta-Llama-3.3-70B-Instruct). See available
              [models](https://cloud.sambanova.ai/pricing)

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

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

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_object" }` enables JSON mode, which will check the message the
              model generates is valid JSON. **Important:** when using JSON mode, you **must**
              also instruct the model to produce JSON yourself via a system or user message.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

          tools: A list of tools the model may call. Use this to provide a list of functions the
              model may generate JSON inputs for.

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
        messages: Iterable[chat_completion_create_params.Message],
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
            ],
        ],
        stream: bool,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        stream_options: Optional[chat_completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_completion_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[chat_completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse | Stream[ChatCompletionCreateResponse]:
        """
        Create chat-based completion

        Args:
          messages: A list of messages comprising the conversation so far.

          model: The model ID to use (e.g. Meta-Llama-3.3-70B-Instruct). See available
              [models](https://cloud.sambanova.ai/pricing)

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

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

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_object" }` enables JSON mode, which will check the message the
              model generates is valid JSON. **Important:** when using JSON mode, you **must**
              also instruct the model to produce JSON yourself via a system or user message.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

          tools: A list of tools the model may call. Use this to provide a list of functions the
              model may generate JSON inputs for.

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

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    def create(
        self,
        *,
        messages: Iterable[chat_completion_create_params.Message],
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
            ],
        ],
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: Optional[chat_completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_completion_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[chat_completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse | Stream[ChatCompletionCreateResponse]:
        return cast(
            ChatCompletionCreateResponse,
            self._post(
                "/v1/chat/completions",
                body=maybe_transform(
                    {
                        "messages": messages,
                        "model": model,
                        "frequency_penalty": frequency_penalty,
                        "logit_bias": logit_bias,
                        "logprobs": logprobs,
                        "max_completion_tokens": max_completion_tokens,
                        "max_tokens": max_tokens,
                        "n": n,
                        "parallel_tool_calls": parallel_tool_calls,
                        "presence_penalty": presence_penalty,
                        "response_format": response_format,
                        "seed": seed,
                        "stop": stop,
                        "stream": stream,
                        "stream_options": stream_options,
                        "temperature": temperature,
                        "tool_choice": tool_choice,
                        "tools": tools,
                        "top_k": top_k,
                        "top_logprobs": top_logprobs,
                        "top_p": top_p,
                    },
                    chat_completion_create_params.ChatCompletionCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatCompletionCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
                stream=stream or False,
                stream_cls=Stream[ChatCompletionCreateResponse],
            ),
        )


class AsyncChatCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        messages: Iterable[chat_completion_create_params.Message],
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
            ],
        ],
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        stream_options: Optional[chat_completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_completion_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[chat_completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse:
        """
        Create chat-based completion

        Args:
          messages: A list of messages comprising the conversation so far.

          model: The model ID to use (e.g. Meta-Llama-3.3-70B-Instruct). See available
              [models](https://cloud.sambanova.ai/pricing)

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

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_object" }` enables JSON mode, which will check the message the
              model generates is valid JSON. **Important:** when using JSON mode, you **must**
              also instruct the model to produce JSON yourself via a system or user message.

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

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

          tools: A list of tools the model may call. Use this to provide a list of functions the
              model may generate JSON inputs for.

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
        messages: Iterable[chat_completion_create_params.Message],
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
            ],
        ],
        stream: Literal[True],
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        stream_options: Optional[chat_completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_completion_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[chat_completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ChatCompletionCreateResponse]:
        """
        Create chat-based completion

        Args:
          messages: A list of messages comprising the conversation so far.

          model: The model ID to use (e.g. Meta-Llama-3.3-70B-Instruct). See available
              [models](https://cloud.sambanova.ai/pricing)

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

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

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_object" }` enables JSON mode, which will check the message the
              model generates is valid JSON. **Important:** when using JSON mode, you **must**
              also instruct the model to produce JSON yourself via a system or user message.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

          tools: A list of tools the model may call. Use this to provide a list of functions the
              model may generate JSON inputs for.

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
        messages: Iterable[chat_completion_create_params.Message],
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
            ],
        ],
        stream: bool,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        stream_options: Optional[chat_completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_completion_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[chat_completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse | AsyncStream[ChatCompletionCreateResponse]:
        """
        Create chat-based completion

        Args:
          messages: A list of messages comprising the conversation so far.

          model: The model ID to use (e.g. Meta-Llama-3.3-70B-Instruct). See available
              [models](https://cloud.sambanova.ai/pricing)

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

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

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_object" }` enables JSON mode, which will check the message the
              model generates is valid JSON. **Important:** when using JSON mode, you **must**
              also instruct the model to produce JSON yourself via a system or user message.

          seed: This is not yet supported by our models.

          stop: Sequences where the API will stop generating tokens. The returned text will not
              contain the stop sequence.

          stream_options: Options for streaming response. Only set this when setting stream as true

          temperature: What sampling temperature to use, determines the degree of randomness in the
              response. between 0 and 2, Higher values like 0.8 will make the output more
              random, while lower values like 0.2 will make it more focused and deterministic.
              Is recommended altering this, top_p or top_k but not more than one of these.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

          tools: A list of tools the model may call. Use this to provide a list of functions the
              model may generate JSON inputs for.

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

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    async def create(
        self,
        *,
        messages: Iterable[chat_completion_create_params.Message],
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
            ],
        ],
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[chat_completion_create_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: Optional[chat_completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[chat_completion_create_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[chat_completion_create_params.Tool]] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionCreateResponse | AsyncStream[ChatCompletionCreateResponse]:
        return cast(
            ChatCompletionCreateResponse,
            await self._post(
                "/v1/chat/completions",
                body=await async_maybe_transform(
                    {
                        "messages": messages,
                        "model": model,
                        "frequency_penalty": frequency_penalty,
                        "logit_bias": logit_bias,
                        "logprobs": logprobs,
                        "max_completion_tokens": max_completion_tokens,
                        "max_tokens": max_tokens,
                        "n": n,
                        "parallel_tool_calls": parallel_tool_calls,
                        "presence_penalty": presence_penalty,
                        "response_format": response_format,
                        "seed": seed,
                        "stop": stop,
                        "stream": stream,
                        "stream_options": stream_options,
                        "temperature": temperature,
                        "tool_choice": tool_choice,
                        "tools": tools,
                        "top_k": top_k,
                        "top_logprobs": top_logprobs,
                        "top_p": top_p,
                    },
                    chat_completion_create_params.ChatCompletionCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatCompletionCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
                stream=stream or False,
                stream_cls=AsyncStream[ChatCompletionCreateResponse],
            ),
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
