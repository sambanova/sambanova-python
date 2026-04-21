# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..types import response_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.response_stream_event import ResponseStreamEvent
from ..types.response_create_response import ResponseCreateResponse

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sambanova/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sambanova/sambanova-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputInputItemList]],
        model: Union[str, Literal["gpt-oss-120b"]],
        background: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        service_tier: Optional[str] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: response_create_params.Text | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse:
        """Creates a model response for the given input.

        Only `type: "function"` tools are
        supported; other tool types are filtered server-side. SambaNova is stateless,
        conversation history must be supplied in full via `input[]` on each request.

        Args:
          input: Text input to the model, or a structured list of input items representing the
              full conversation turn. A plain string is equivalent to a single user message.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          background: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim. Not currently implemented; accepted for API
              compatibility and echoed in the response.

          instructions: Inserts a system (or developer) message as the first item in the model's
              context. Equivalent to a system-role message prepended to input[].

          max_output_tokens: Upper bound on the number of tokens the model may generate, including visible
              output tokens and reasoning tokens.

          max_tool_calls: Maximum number of tool calls the model may make in a single response turn. Not
              currently implemented; accepted for API compatibility.

          metadata: Included for API compatibility, but not supported

          parallel_tool_calls: Whether the model may issue multiple tool calls in parallel within one turn.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics. Not currently implemented; accepted for API compatibility
              and echoed in the response.

          previous_response_id: Not supported. SambaNova is stateless and does not maintain server-side
              conversation state. Accepted for API compatibility but ignored; clients must
              supply the full conversation history in input[].

          reasoning: Reasoning configuration for models that support it. Ignored on non-reasoning
              models.

          service_tier: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          store: SambaNova is stateless - this field is accepted for API compatibility but has no
              effect. Always echoed back as false.

          stream: If true, the response is delivered as server-sent events (SSE).

          temperature: Controls randomness in generation. Range: 0–2. It is recommended to alter this,
              top_p, or top_k but not more than one at a time.

          text: Response format configuration. Supports plain text, json_object, and
              json_schema.

          tool_choice: Controls which tool (if any) the model calls. String values: "none" disables
              tool calls; "auto" lets the model decide; "required" forces at least one tool
              call. To force a specific function, provide a ResponseNamedToolChoice object.

          tools: Tools available to the model. Only type: "function" is supported; all other tool
              types are filtered server-side.

          top_k: Limits sampling to the top K most probable tokens. It is recommended to alter
              this, top_p, or temperature but not more than one at a time.

          top_logprobs: Number of top log-probability entries to return per output token. Null means log
              probabilities are not returned.

          top_p: Nucleus sampling cutoff. Range: 0–1. It is recommended to alter this,
              temperature, or top_k but not more than one at a time.

          truncation: Accepted for API compatibility and echoed in the response. Context truncation
              behavior is not currently configurable via this field in SambaNova.

          user: Included for API compatibility, but only echoed back in response

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
        input: Union[str, Iterable[response_create_params.InputInputItemList]],
        model: Union[str, Literal["gpt-oss-120b"]],
        stream: Literal[True],
        background: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        service_tier: Optional[str] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: response_create_params.Text | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ResponseStreamEvent]:
        """Creates a model response for the given input.

        Only `type: "function"` tools are
        supported; other tool types are filtered server-side. SambaNova is stateless,
        conversation history must be supplied in full via `input[]` on each request.

        Args:
          input: Text input to the model, or a structured list of input items representing the
              full conversation turn. A plain string is equivalent to a single user message.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          stream: If true, the response is delivered as server-sent events (SSE).

          background: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim. Not currently implemented; accepted for API
              compatibility and echoed in the response.

          instructions: Inserts a system (or developer) message as the first item in the model's
              context. Equivalent to a system-role message prepended to input[].

          max_output_tokens: Upper bound on the number of tokens the model may generate, including visible
              output tokens and reasoning tokens.

          max_tool_calls: Maximum number of tool calls the model may make in a single response turn. Not
              currently implemented; accepted for API compatibility.

          metadata: Included for API compatibility, but not supported

          parallel_tool_calls: Whether the model may issue multiple tool calls in parallel within one turn.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics. Not currently implemented; accepted for API compatibility
              and echoed in the response.

          previous_response_id: Not supported. SambaNova is stateless and does not maintain server-side
              conversation state. Accepted for API compatibility but ignored; clients must
              supply the full conversation history in input[].

          reasoning: Reasoning configuration for models that support it. Ignored on non-reasoning
              models.

          service_tier: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          store: SambaNova is stateless - this field is accepted for API compatibility but has no
              effect. Always echoed back as false.

          temperature: Controls randomness in generation. Range: 0–2. It is recommended to alter this,
              top_p, or top_k but not more than one at a time.

          text: Response format configuration. Supports plain text, json_object, and
              json_schema.

          tool_choice: Controls which tool (if any) the model calls. String values: "none" disables
              tool calls; "auto" lets the model decide; "required" forces at least one tool
              call. To force a specific function, provide a ResponseNamedToolChoice object.

          tools: Tools available to the model. Only type: "function" is supported; all other tool
              types are filtered server-side.

          top_k: Limits sampling to the top K most probable tokens. It is recommended to alter
              this, top_p, or temperature but not more than one at a time.

          top_logprobs: Number of top log-probability entries to return per output token. Null means log
              probabilities are not returned.

          top_p: Nucleus sampling cutoff. Range: 0–1. It is recommended to alter this,
              temperature, or top_k but not more than one at a time.

          truncation: Accepted for API compatibility and echoed in the response. Context truncation
              behavior is not currently configurable via this field in SambaNova.

          user: Included for API compatibility, but only echoed back in response

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
        input: Union[str, Iterable[response_create_params.InputInputItemList]],
        model: Union[str, Literal["gpt-oss-120b"]],
        stream: bool,
        background: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        service_tier: Optional[str] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: response_create_params.Text | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | Stream[ResponseStreamEvent]:
        """Creates a model response for the given input.

        Only `type: "function"` tools are
        supported; other tool types are filtered server-side. SambaNova is stateless,
        conversation history must be supplied in full via `input[]` on each request.

        Args:
          input: Text input to the model, or a structured list of input items representing the
              full conversation turn. A plain string is equivalent to a single user message.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          stream: If true, the response is delivered as server-sent events (SSE).

          background: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim. Not currently implemented; accepted for API
              compatibility and echoed in the response.

          instructions: Inserts a system (or developer) message as the first item in the model's
              context. Equivalent to a system-role message prepended to input[].

          max_output_tokens: Upper bound on the number of tokens the model may generate, including visible
              output tokens and reasoning tokens.

          max_tool_calls: Maximum number of tool calls the model may make in a single response turn. Not
              currently implemented; accepted for API compatibility.

          metadata: Included for API compatibility, but not supported

          parallel_tool_calls: Whether the model may issue multiple tool calls in parallel within one turn.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics. Not currently implemented; accepted for API compatibility
              and echoed in the response.

          previous_response_id: Not supported. SambaNova is stateless and does not maintain server-side
              conversation state. Accepted for API compatibility but ignored; clients must
              supply the full conversation history in input[].

          reasoning: Reasoning configuration for models that support it. Ignored on non-reasoning
              models.

          service_tier: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          store: SambaNova is stateless - this field is accepted for API compatibility but has no
              effect. Always echoed back as false.

          temperature: Controls randomness in generation. Range: 0–2. It is recommended to alter this,
              top_p, or top_k but not more than one at a time.

          text: Response format configuration. Supports plain text, json_object, and
              json_schema.

          tool_choice: Controls which tool (if any) the model calls. String values: "none" disables
              tool calls; "auto" lets the model decide; "required" forces at least one tool
              call. To force a specific function, provide a ResponseNamedToolChoice object.

          tools: Tools available to the model. Only type: "function" is supported; all other tool
              types are filtered server-side.

          top_k: Limits sampling to the top K most probable tokens. It is recommended to alter
              this, top_p, or temperature but not more than one at a time.

          top_logprobs: Number of top log-probability entries to return per output token. Null means log
              probabilities are not returned.

          top_p: Nucleus sampling cutoff. Range: 0–1. It is recommended to alter this,
              temperature, or top_k but not more than one at a time.

          truncation: Accepted for API compatibility and echoed in the response. Context truncation
              behavior is not currently configurable via this field in SambaNova.

          user: Included for API compatibility, but only echoed back in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputInputItemList]],
        model: Union[str, Literal["gpt-oss-120b"]],
        background: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        service_tier: Optional[str] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: response_create_params.Text | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | Stream[ResponseStreamEvent]:
        return self._post(
            "/responses",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "background": background,
                    "frequency_penalty": frequency_penalty,
                    "instructions": instructions,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "previous_response_id": previous_response_id,
                    "reasoning": reasoning,
                    "service_tier": service_tier,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncation": truncation,
                    "user": user,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ResponseCreateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=Stream[ResponseStreamEvent],
        )


class AsyncResponsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sambanova/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sambanova/sambanova-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputInputItemList]],
        model: Union[str, Literal["gpt-oss-120b"]],
        background: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        service_tier: Optional[str] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: response_create_params.Text | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse:
        """Creates a model response for the given input.

        Only `type: "function"` tools are
        supported; other tool types are filtered server-side. SambaNova is stateless,
        conversation history must be supplied in full via `input[]` on each request.

        Args:
          input: Text input to the model, or a structured list of input items representing the
              full conversation turn. A plain string is equivalent to a single user message.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          background: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim. Not currently implemented; accepted for API
              compatibility and echoed in the response.

          instructions: Inserts a system (or developer) message as the first item in the model's
              context. Equivalent to a system-role message prepended to input[].

          max_output_tokens: Upper bound on the number of tokens the model may generate, including visible
              output tokens and reasoning tokens.

          max_tool_calls: Maximum number of tool calls the model may make in a single response turn. Not
              currently implemented; accepted for API compatibility.

          metadata: Included for API compatibility, but not supported

          parallel_tool_calls: Whether the model may issue multiple tool calls in parallel within one turn.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics. Not currently implemented; accepted for API compatibility
              and echoed in the response.

          previous_response_id: Not supported. SambaNova is stateless and does not maintain server-side
              conversation state. Accepted for API compatibility but ignored; clients must
              supply the full conversation history in input[].

          reasoning: Reasoning configuration for models that support it. Ignored on non-reasoning
              models.

          service_tier: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          store: SambaNova is stateless - this field is accepted for API compatibility but has no
              effect. Always echoed back as false.

          stream: If true, the response is delivered as server-sent events (SSE).

          temperature: Controls randomness in generation. Range: 0–2. It is recommended to alter this,
              top_p, or top_k but not more than one at a time.

          text: Response format configuration. Supports plain text, json_object, and
              json_schema.

          tool_choice: Controls which tool (if any) the model calls. String values: "none" disables
              tool calls; "auto" lets the model decide; "required" forces at least one tool
              call. To force a specific function, provide a ResponseNamedToolChoice object.

          tools: Tools available to the model. Only type: "function" is supported; all other tool
              types are filtered server-side.

          top_k: Limits sampling to the top K most probable tokens. It is recommended to alter
              this, top_p, or temperature but not more than one at a time.

          top_logprobs: Number of top log-probability entries to return per output token. Null means log
              probabilities are not returned.

          top_p: Nucleus sampling cutoff. Range: 0–1. It is recommended to alter this,
              temperature, or top_k but not more than one at a time.

          truncation: Accepted for API compatibility and echoed in the response. Context truncation
              behavior is not currently configurable via this field in SambaNova.

          user: Included for API compatibility, but only echoed back in response

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
        input: Union[str, Iterable[response_create_params.InputInputItemList]],
        model: Union[str, Literal["gpt-oss-120b"]],
        stream: Literal[True],
        background: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        service_tier: Optional[str] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: response_create_params.Text | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ResponseStreamEvent]:
        """Creates a model response for the given input.

        Only `type: "function"` tools are
        supported; other tool types are filtered server-side. SambaNova is stateless,
        conversation history must be supplied in full via `input[]` on each request.

        Args:
          input: Text input to the model, or a structured list of input items representing the
              full conversation turn. A plain string is equivalent to a single user message.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          stream: If true, the response is delivered as server-sent events (SSE).

          background: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim. Not currently implemented; accepted for API
              compatibility and echoed in the response.

          instructions: Inserts a system (or developer) message as the first item in the model's
              context. Equivalent to a system-role message prepended to input[].

          max_output_tokens: Upper bound on the number of tokens the model may generate, including visible
              output tokens and reasoning tokens.

          max_tool_calls: Maximum number of tool calls the model may make in a single response turn. Not
              currently implemented; accepted for API compatibility.

          metadata: Included for API compatibility, but not supported

          parallel_tool_calls: Whether the model may issue multiple tool calls in parallel within one turn.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics. Not currently implemented; accepted for API compatibility
              and echoed in the response.

          previous_response_id: Not supported. SambaNova is stateless and does not maintain server-side
              conversation state. Accepted for API compatibility but ignored; clients must
              supply the full conversation history in input[].

          reasoning: Reasoning configuration for models that support it. Ignored on non-reasoning
              models.

          service_tier: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          store: SambaNova is stateless - this field is accepted for API compatibility but has no
              effect. Always echoed back as false.

          temperature: Controls randomness in generation. Range: 0–2. It is recommended to alter this,
              top_p, or top_k but not more than one at a time.

          text: Response format configuration. Supports plain text, json_object, and
              json_schema.

          tool_choice: Controls which tool (if any) the model calls. String values: "none" disables
              tool calls; "auto" lets the model decide; "required" forces at least one tool
              call. To force a specific function, provide a ResponseNamedToolChoice object.

          tools: Tools available to the model. Only type: "function" is supported; all other tool
              types are filtered server-side.

          top_k: Limits sampling to the top K most probable tokens. It is recommended to alter
              this, top_p, or temperature but not more than one at a time.

          top_logprobs: Number of top log-probability entries to return per output token. Null means log
              probabilities are not returned.

          top_p: Nucleus sampling cutoff. Range: 0–1. It is recommended to alter this,
              temperature, or top_k but not more than one at a time.

          truncation: Accepted for API compatibility and echoed in the response. Context truncation
              behavior is not currently configurable via this field in SambaNova.

          user: Included for API compatibility, but only echoed back in response

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
        input: Union[str, Iterable[response_create_params.InputInputItemList]],
        model: Union[str, Literal["gpt-oss-120b"]],
        stream: bool,
        background: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        service_tier: Optional[str] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: response_create_params.Text | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | AsyncStream[ResponseStreamEvent]:
        """Creates a model response for the given input.

        Only `type: "function"` tools are
        supported; other tool types are filtered server-side. SambaNova is stateless,
        conversation history must be supplied in full via `input[]` on each request.

        Args:
          input: Text input to the model, or a structured list of input items representing the
              full conversation turn. A plain string is equivalent to a single user message.

          model: The model ID to use (e.g. gpt-oss-120b). See available
              [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)

          stream: If true, the response is delivered as server-sent events (SSE).

          background: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim. Not currently implemented; accepted for API
              compatibility and echoed in the response.

          instructions: Inserts a system (or developer) message as the first item in the model's
              context. Equivalent to a system-role message prepended to input[].

          max_output_tokens: Upper bound on the number of tokens the model may generate, including visible
              output tokens and reasoning tokens.

          max_tool_calls: Maximum number of tool calls the model may make in a single response turn. Not
              currently implemented; accepted for API compatibility.

          metadata: Included for API compatibility, but not supported

          parallel_tool_calls: Whether the model may issue multiple tool calls in parallel within one turn.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics. Not currently implemented; accepted for API compatibility
              and echoed in the response.

          previous_response_id: Not supported. SambaNova is stateless and does not maintain server-side
              conversation state. Accepted for API compatibility but ignored; clients must
              supply the full conversation history in input[].

          reasoning: Reasoning configuration for models that support it. Ignored on non-reasoning
              models.

          service_tier: Accepted for API compatibility and echoed back in the response. Has no effect on
              server behavior.

          store: SambaNova is stateless - this field is accepted for API compatibility but has no
              effect. Always echoed back as false.

          temperature: Controls randomness in generation. Range: 0–2. It is recommended to alter this,
              top_p, or top_k but not more than one at a time.

          text: Response format configuration. Supports plain text, json_object, and
              json_schema.

          tool_choice: Controls which tool (if any) the model calls. String values: "none" disables
              tool calls; "auto" lets the model decide; "required" forces at least one tool
              call. To force a specific function, provide a ResponseNamedToolChoice object.

          tools: Tools available to the model. Only type: "function" is supported; all other tool
              types are filtered server-side.

          top_k: Limits sampling to the top K most probable tokens. It is recommended to alter
              this, top_p, or temperature but not more than one at a time.

          top_logprobs: Number of top log-probability entries to return per output token. Null means log
              probabilities are not returned.

          top_p: Nucleus sampling cutoff. Range: 0–1. It is recommended to alter this,
              temperature, or top_k but not more than one at a time.

          truncation: Accepted for API compatibility and echoed in the response. Context truncation
              behavior is not currently configurable via this field in SambaNova.

          user: Included for API compatibility, but only echoed back in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputInputItemList]],
        model: Union[str, Literal["gpt-oss-120b"]],
        background: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        max_output_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        service_tier: Optional[str] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        text: response_create_params.Text | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncation: Optional[Literal["auto", "disabled"]] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | AsyncStream[ResponseStreamEvent]:
        return await self._post(
            "/responses",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "background": background,
                    "frequency_penalty": frequency_penalty,
                    "instructions": instructions,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "metadata": metadata,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "previous_response_id": previous_response_id,
                    "reasoning": reasoning,
                    "service_tier": service_tier,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "text": text,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "truncation": truncation,
                    "user": user,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ResponseCreateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=stream or False,
            stream_cls=AsyncStream[ResponseStreamEvent],
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
