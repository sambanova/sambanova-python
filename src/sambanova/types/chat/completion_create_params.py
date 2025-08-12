# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CompletionCreateParamsBase",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1ImageURL",
    "ResponseFormat",
    "StreamOptions",
    "ToolChoice",
    "ToolChoiceToolChoice",
    "Tool",
    "ToolParameters",
    "CompletionCreateParamsNonStreaming",
    "CompletionCreateParamsStreaming",
]


class CompletionCreateParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[str]
    """Model ID to query."""

    max_tokens: int

    response_format: ResponseFormat

    stop: Union[str, List[str]]

    stream_options: StreamOptions

    temperature: float

    tool_choice: ToolChoice

    tools: Iterable[Tool]

    top_k: int

    top_p: float


class MessageContentUnionMember1ImageURL(TypedDict, total=False):
    url: Required[str]
    """Data URI string like data:<format>;base64,<data>."""


class MessageContentUnionMember1(TypedDict, total=False):
    type: Required[Literal["text", "image_url"]]
    """Kind of message part."""

    image_url: MessageContentUnionMember1ImageURL
    """Image content when type is image_url."""

    text: str
    """Text content when type is text."""


class Message(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageContentUnionMember1]]]

    role: Required[Literal["system", "user", "assistant"]]


class ResponseFormat(TypedDict, total=False):
    type: Required[Literal["json_object", "json_schema"]]

    json_schema: Dict[str, object]


class StreamOptions(TypedDict, total=False):
    include_usage: bool


class ToolChoiceToolChoice(TypedDict, total=False):
    name: Required[str]


ToolChoice: TypeAlias = Union[Literal["auto", "required"], ToolChoiceToolChoice]


class ToolParameters(TypedDict, total=False):
    properties: Required[Dict[str, object]]

    type: Required[Literal["object"]]

    required: List[str]


class Tool(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameters: Required[ToolParameters]
    """JSON Schema for function parameters (must be an object schema)."""


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Literal[False]


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
