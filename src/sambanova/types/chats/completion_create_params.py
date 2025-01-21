# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CompletionCreateParamsBase",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1ImageURL",
    "ResponseFormat",
    "StreamOptions",
    "ToolChoice",
    "ToolChoiceUnionMember1",
    "ToolChoiceUnionMember1Function",
    "Tool",
    "ToolFunction",
    "ToolFunctionParameters",
    "CompletionCreateParamsNonStreaming",
    "CompletionCreateParamsStreaming",
]


class CompletionCreateParamsBase(TypedDict, total=False):
    max_tokens: int
    """Maximum number of tokens to generate."""

    messages: Iterable[Message]
    """A list of messages comprising the conversation so far."""

    model: str
    """The name of the model to query."""

    response_format: ResponseFormat
    """Ensures the model outputs a valid JSON."""

    stop: Union[str, List[str]]
    """Sequences where the API will stop generating tokens."""

    stream_options: StreamOptions
    """Options for streaming response."""

    temperature: float
    """Degree of randomness in the response."""

    tool_choice: ToolChoice

    tools: Iterable[Tool]
    """A list of tools the model may call."""

    top_k: int
    """Limit for token choices."""

    top_p: float
    """Cumulative probability for token choices."""


class MessageContentUnionMember1ImageURL(TypedDict, total=False):
    url: str


class MessageContentUnionMember1(TypedDict, total=False):
    image_url: MessageContentUnionMember1ImageURL

    text: str

    type: Literal["text", "image_url"]


class Message(TypedDict, total=False):
    content: Union[str, Iterable[MessageContentUnionMember1]]
    """The contents of a text-only message."""

    role: Literal["system", "user", "assistant", "tool"]
    """The role of the message author."""


class ResponseFormat(TypedDict, total=False):
    type: Literal["json_object"]


class StreamOptions(TypedDict, total=False):
    include_usage: bool


class ToolChoiceUnionMember1Function(TypedDict, total=False):
    name: str


class ToolChoiceUnionMember1(TypedDict, total=False):
    function: ToolChoiceUnionMember1Function

    type: Literal["function", "auto", "none"]


ToolChoice: TypeAlias = Union[str, ToolChoiceUnionMember1]


class ToolFunctionParameters(TypedDict, total=False):
    properties: object

    type: str


class ToolFunction(TypedDict, total=False):
    description: str

    name: str

    parameters: ToolFunctionParameters


class Tool(TypedDict, total=False):
    function: ToolFunction

    type: Literal["function"]


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Literal[False]
    """If set, partial message deltas will be sent."""


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """If set, partial message deltas will be sent."""


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
