# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ChatCompletionCreateParamsBase",
    "Message",
    "MessageSystemMessage",
    "MessageUserMessage",
    "MessageAssistantMessage",
    "MessageToolMessage",
    "ResponseFormat",
    "StreamOptions",
    "ToolChoice",
    "ToolChoiceToolChoiceObject",
    "ToolChoiceToolChoiceObjectFunction",
    "Tool",
    "ToolFunction",
    "ChatCompletionCreateParamsNonStreaming",
    "ChatCompletionCreateParamsStreaming",
]


class ChatCompletionCreateParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """A list of messages comprising the conversation so far."""

    model: Required[
        Union[
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
        ]
    ]
    """The model ID to use (e.g.

    Meta-Llama-3.3-70B-Instruct). See available
    [models](https://cloud.sambanova.ai/pricing)
    """

    frequency_penalty: float
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """

    logit_bias: Optional[object]
    """This is not yet supported by our models.

    Modify the likelihood of specified tokens appearing in the completion.
    """

    logprobs: Optional[bool]
    """This is not yet supported by our models.

    Whether to return log probabilities of the output tokens or not. If true,
    returns the log probabilities of each output token returned in the `content` of
    `message`.
    """

    max_completion_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the chat completion.

    The total length of input tokens and generated tokens is limited by the model's
    context length.
    """

    max_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the chat completion.

    The total length of input tokens and generated tokens is limited by the model's
    context length.
    """

    n: Optional[int]
    """This is not yet supported by our models.

    How many chat completion choices to generate for each input message.
    """

    parallel_tool_calls: Optional[bool]
    """Whether to enable parallel function calling during tool use."""

    presence_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.
    """

    response_format: Optional[ResponseFormat]
    """An object specifying the format that the model must output.

    Setting to `{ "type": "json_object" }` enables JSON mode, which will check the
    message the model generates is valid JSON. **Important:** when using JSON mode,
    you **must** also instruct the model to produce JSON yourself via a system or
    user message.
    """

    seed: Optional[int]
    """This is not yet supported by our models."""

    stop: Union[Optional[str], List[str], None]
    """Sequences where the API will stop generating tokens.

    The returned text will not contain the stop sequence.
    """

    stream_options: Optional[StreamOptions]
    """Options for streaming response. Only set this when setting stream as true"""

    temperature: Optional[float]
    """
    What sampling temperature to use, determines the degree of randomness in the
    response. between 0 and 2, Higher values like 0.8 will make the output more
    random, while lower values like 0.2 will make it more focused and deterministic.
    Is recommended altering this, top_p or top_k but not more than one of these.
    """

    tool_choice: Optional[ToolChoice]
    """Controls which (if any) tool is called by the model.

    `none` means the model will not call any tool and instead generates a message.
    `auto` means the model can pick between generating a message or calling one or
    more tools. `required` means the model must call one or more tools. Specifying a
    particular tool via `{"type": "function", "function": {"name": "my_function"}}`
    forces the model to call that tool.
    """

    tools: Optional[Iterable[Tool]]
    """A list of tools the model may call.

    Use this to provide a list of functions the model may generate JSON inputs for.
    """

    top_k: Optional[int]
    """Amount limit of token choices.

    An alternative to sampling with temperature, the model considers the results of
    the first K tokens with higher probability. So 10 means only the first 10 tokens
    with higher probability are considered. Is recommended altering this, top_p or
    temperature but not more than one of these.
    """

    top_logprobs: Optional[int]
    """This is not yet supported by our models.

    An integer between 0 and 20 specifying the number of most likely tokens to
    return at each token position, each with an associated log probability.
    `logprobs` must be set to `true` if this parameter is used.
    """

    top_p: Optional[float]
    """Cumulative probability for token choices.

    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered. Is
    recommended altering this, top_k or temperature but not more than one of these.
    """


class MessageSystemMessageTyped(TypedDict, total=False):
    content: Required[Union[str, Iterable[object], None]]
    """The contents of the system message."""

    role: Required[Literal["system"]]
    """The role of the messages author, in this case `system`."""

    examples: object


MessageSystemMessage: TypeAlias = Union[MessageSystemMessageTyped, Dict[str, object]]


class MessageUserMessageTyped(TypedDict, total=False):
    content: Required[Union[str, Iterable[object], None]]
    """The contents of the user message."""

    role: Required[Literal["user"]]
    """The role of the messages author, in this case `user`."""


MessageUserMessage: TypeAlias = Union[MessageUserMessageTyped, Dict[str, object]]


class MessageAssistantMessageTyped(TypedDict, total=False):
    content: Required[Union[str, Iterable[object], None]]
    """The contents of the assistant message."""

    role: Required[Literal["assistant"]]
    """The role of the messages author, in this case `assistant`."""

    tool_calls: Optional[Iterable[object]]
    """The tool calls generated by the model."""


MessageAssistantMessage: TypeAlias = Union[MessageAssistantMessageTyped, Dict[str, object]]


class MessageToolMessageTyped(TypedDict, total=False):
    content: Required[Union[str, Iterable[object]]]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""


MessageToolMessage: TypeAlias = Union[MessageToolMessageTyped, Dict[str, object]]

Message: TypeAlias = Union[MessageSystemMessage, MessageUserMessage, MessageAssistantMessage, MessageToolMessage]


class ResponseFormat(TypedDict, total=False):
    type: Literal["json_object"]
    """Only `json_object` allowed yet."""


class StreamOptionsTyped(TypedDict, total=False):
    include_usage: Optional[bool]
    """Whether to include the usage metrics in a final chunk or not"""


StreamOptions: TypeAlias = Union[StreamOptionsTyped, Dict[str, object]]


class ToolChoiceToolChoiceObjectFunctionTyped(TypedDict, total=False):
    name: Required[str]
    """the name of the tool expected to be used by the model"""


ToolChoiceToolChoiceObjectFunction: TypeAlias = Union[ToolChoiceToolChoiceObjectFunctionTyped, Dict[str, object]]


class ToolChoiceToolChoiceObjectTyped(TypedDict, total=False):
    function: Required[ToolChoiceToolChoiceObjectFunction]
    """Specifies a tool the model should use.

    Use it to force the model to call that specific tool.
    """

    type: Required[Literal["function"]]
    """The type of the tool. only `function` is supported."""


ToolChoiceToolChoiceObject: TypeAlias = Union[ToolChoiceToolChoiceObjectTyped, Dict[str, object]]

ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], ToolChoiceToolChoiceObject]


class ToolFunctionTyped(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes.
    """

    description: Optional[str]
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object.

    see the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format. Omitting `parameters` defines a function with an
    empty parameter list.
    """


ToolFunction: TypeAlias = Union[ToolFunctionTyped, Dict[str, object]]


class ToolTyped(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[str]
    """The type of the tool. Currently, only `function` is supported."""


Tool: TypeAlias = Union[ToolTyped, Dict[str, object]]


class ChatCompletionCreateParamsNonStreaming(ChatCompletionCreateParamsBase, total=False):
    stream: Optional[Literal[False]]
    """If set, partial message deltas will be sent.

    Tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message.
    """


class ChatCompletionCreateParamsStreaming(ChatCompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """If set, partial message deltas will be sent.

    Tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message.
    """


ChatCompletionCreateParams = Union[ChatCompletionCreateParamsNonStreaming, ChatCompletionCreateParamsStreaming]
