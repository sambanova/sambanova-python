# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "MessageCountTokensParams",
    "Message",
    "MessageContentContentBlockArray",
    "MessageContentContentBlockArrayMessageInputTextBlock",
    "MessageContentContentBlockArrayMessageInputTextBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputImageBlock",
    "MessageContentContentBlockArrayMessageInputImageBlockSource",
    "MessageContentContentBlockArrayMessageInputImageBlockSourceMessageInputImageSourceBase64",
    "MessageContentContentBlockArrayMessageInputImageBlockSourceMessageInputImageSourceURL",
    "MessageContentContentBlockArrayMessageInputImageBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputToolUseBlock",
    "MessageContentContentBlockArrayMessageInputToolUseBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputToolResultBlock",
    "MessageContentContentBlockArrayMessageInputToolResultBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArray",
    "MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputTextBlock",
    "MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputTextBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlock",
    "MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockSource",
    "MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockSourceMessageInputImageSourceBase64",
    "MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockSourceMessageInputImageSourceURL",
    "MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputServerToolUseBlock",
    "MessageContentContentBlockArrayMessageInputServerToolUseBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputSearchResultBlock",
    "MessageContentContentBlockArrayMessageInputSearchResultBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputSearchResultBlockContent",
    "MessageContentContentBlockArrayMessageInputSearchResultBlockContentCacheControl",
    "MessageContentContentBlockArrayMessageInputWebSearchToolResultBlock",
    "MessageContentContentBlockArrayMessageInputWebSearchToolResultBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputWebFetchToolResultBlock",
    "MessageContentContentBlockArrayMessageInputWebFetchToolResultBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputCodeExecutionToolResultBlock",
    "MessageContentContentBlockArrayMessageInputCodeExecutionToolResultBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputBashCodeExecutionToolResultBlock",
    "MessageContentContentBlockArrayMessageInputBashCodeExecutionToolResultBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputTextEditorCodeExecutionToolResultBlock",
    "MessageContentContentBlockArrayMessageInputTextEditorCodeExecutionToolResultBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputToolSearchToolResultBlock",
    "MessageContentContentBlockArrayMessageInputToolSearchToolResultBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputThinkingBlock",
    "MessageContentContentBlockArrayMessageInputRedactedThinkingBlock",
    "MessageContentContentBlockArrayMessageInputContainerUploadBlock",
    "MessageContentContentBlockArrayMessageInputContainerUploadBlockCacheControl",
    "MessageContentContentBlockArrayMessageInputDocumentBlock",
    "MessageContentContentBlockArrayMessageInputDocumentBlockCacheControl",
    "SystemSystemTextBlockArray",
    "SystemSystemTextBlockArrayCacheControl",
    "Thinking",
    "ThinkingMessageThinkingDisabled",
    "ThinkingMessageThinkingEnabled",
    "ThinkingMessageThinkingAdaptive",
    "ToolChoice",
    "ToolChoiceMessageToolChoiceAuto",
    "ToolChoiceMessageToolChoiceAny",
    "ToolChoiceMessageToolChoiceNone",
    "ToolChoiceMessageToolChoiceTool",
    "Tool",
    "ToolCacheControl",
]


class MessageCountTokensParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """Conversation turns."""

    model: Required[str]
    """Model identifier."""

    system: Union[str, Iterable[SystemSystemTextBlockArray]]
    """System prompt for the conversation.

    Accepts either a single string (most common) or an array of text blocks (used
    when individual segments need `cache_control` markers). Multiple text blocks are
    joined with newlines and prepended to the conversation as a `role: system`
    message.
    """

    thinking: Thinking
    """Controls Anthropic-style extended thinking.

    **In v1**: only `type:"disabled"` is silently accepted as a no-op;
    `type:"enabled"` and `type:"adaptive"` return a 400 `invalid_request_error`
    (`unsupported_parameter`).
    """

    tool_choice: Optional[ToolChoice]
    """How the model should choose from the provided tools."""

    tools: Optional[Iterable[Tool]]
    """Tool definitions the model may call."""

    anthropic_version: Annotated[str, PropertyInfo(alias="anthropic-version")]


class MessageContentContentBlockArrayMessageInputTextBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputTextBlock(TypedDict, total=False):
    """Plain-text segment of a message."""

    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: MessageContentContentBlockArrayMessageInputTextBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """

    citations: Optional[Iterable[Dict[str, object]]]


class MessageContentContentBlockArrayMessageInputImageBlockSourceMessageInputImageSourceBase64(TypedDict, total=False):
    """Inline image data encoded as base64."""

    data: Required[str]
    """Base64-encoded image bytes (no `data:` URI prefix)."""

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]
    """MIME type of the image bytes."""

    type: Required[Literal["base64"]]


class MessageContentContentBlockArrayMessageInputImageBlockSourceMessageInputImageSourceURL(TypedDict, total=False):
    """HTTPS URL pointing to an image.

    **Returns 400 in v1** — URL fetching is blocked. Use `type:"base64"` instead.
    """

    type: Required[Literal["url"]]

    url: Required[str]


MessageContentContentBlockArrayMessageInputImageBlockSource: TypeAlias = Union[
    MessageContentContentBlockArrayMessageInputImageBlockSourceMessageInputImageSourceBase64,
    MessageContentContentBlockArrayMessageInputImageBlockSourceMessageInputImageSourceURL,
]


class MessageContentContentBlockArrayMessageInputImageBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputImageBlock(TypedDict, total=False):
    """Image content.

    Only `source.type:"base64"` is supported in v1; URL sources return 400.
    """

    source: Required[MessageContentContentBlockArrayMessageInputImageBlockSource]
    """Inline image data encoded as base64."""

    type: Required[Literal["image"]]

    cache_control: MessageContentContentBlockArrayMessageInputImageBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputToolUseBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputToolUseBlock(TypedDict, total=False):
    """A prior assistant turn that invoked a tool."""

    id: Required[str]
    """Unique identifier for the tool call (used to correlate `tool_result`)."""

    input: Required[Dict[str, object]]
    """Tool inputs as a JSON object."""

    name: Required[str]
    """Name of the tool being invoked."""

    type: Required[Literal["tool_use"]]

    cache_control: MessageContentContentBlockArrayMessageInputToolUseBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputToolResultBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputTextBlockCacheControl(
    TypedDict, total=False
):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputTextBlock(
    TypedDict, total=False
):
    """Plain-text segment of a message."""

    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputTextBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """

    citations: Optional[Iterable[Dict[str, object]]]


class MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockSourceMessageInputImageSourceBase64(
    TypedDict, total=False
):
    """Inline image data encoded as base64."""

    data: Required[str]
    """Base64-encoded image bytes (no `data:` URI prefix)."""

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]
    """MIME type of the image bytes."""

    type: Required[Literal["base64"]]


class MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockSourceMessageInputImageSourceURL(
    TypedDict, total=False
):
    """HTTPS URL pointing to an image.

    **Returns 400 in v1** — URL fetching is blocked. Use `type:"base64"` instead.
    """

    type: Required[Literal["url"]]

    url: Required[str]


MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockSource: TypeAlias = Union[
    MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockSourceMessageInputImageSourceBase64,
    MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockSourceMessageInputImageSourceURL,
]


class MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockCacheControl(
    TypedDict, total=False
):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlock(
    TypedDict, total=False
):
    """Image content.

    Only `source.type:"base64"` is supported in v1; URL sources return 400.
    """

    source: Required[
        MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockSource
    ]
    """Inline image data encoded as base64."""

    type: Required[Literal["image"]]

    cache_control: MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArray: TypeAlias = Union[
    MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputTextBlock,
    MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArrayMessageInputImageBlock,
]


class MessageContentContentBlockArrayMessageInputToolResultBlock(TypedDict, total=False):
    """Result of a prior tool call."""

    tool_use_id: Required[str]
    """ID of the `tool_use` block this result corresponds to."""

    type: Required[Literal["tool_result"]]

    cache_control: MessageContentContentBlockArrayMessageInputToolResultBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """

    content: Union[
        str, Iterable[MessageContentContentBlockArrayMessageInputToolResultBlockContentToolResultContentArray]
    ]

    is_error: Optional[bool]
    """Silently dropped in v1."""


class MessageContentContentBlockArrayMessageInputServerToolUseBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputServerToolUseBlock(TypedDict, total=False):
    """Anthropic compatibility only — SambaNova does not run server-side tools.

    A prior assistant turn that invoked an Anthropic-hosted tool (web_search, code_execution, etc.). Accepted in conversation history (e.g. replaying an Anthropic-served session) but never originates from a SambaNova response. New `server_tool_use`-type tool definitions on outgoing requests are rejected with 400 `unsupported_tool_type`.
    """

    id: Required[str]

    input: Required[Dict[str, object]]

    name: Required[str]

    type: Required[Literal["server_tool_use"]]

    cache_control: MessageContentContentBlockArrayMessageInputServerToolUseBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputSearchResultBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputSearchResultBlockContentCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputSearchResultBlockContent(TypedDict, total=False):
    """Plain-text segment of a message."""

    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: MessageContentContentBlockArrayMessageInputSearchResultBlockContentCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """

    citations: Optional[Iterable[Dict[str, object]]]


class MessageContentContentBlockArrayMessageInputSearchResultBlock(TypedDict, total=False):
    """Inline search result content.

    In v1 the `title`, `source`, and `content[]` text are extracted into a text block; citations are dropped.
    """

    type: Required[Literal["search_result"]]

    cache_control: MessageContentContentBlockArrayMessageInputSearchResultBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """

    citations: Optional[Dict[str, object]]

    content: Iterable[MessageContentContentBlockArrayMessageInputSearchResultBlockContent]

    source: str

    title: str


class MessageContentContentBlockArrayMessageInputWebSearchToolResultBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputWebSearchToolResultBlock(TypedDict, total=False):
    """Anthropic compatibility only — SambaNova does not run server-side `web_search`.

    Echo of a prior Anthropic-served `web_search` tool call; accepted in conversation history but never originates from a SambaNova response. When present, only `title` (`url`) per result is extracted into a tool message.
    """

    content: Required[Iterable[Dict[str, object]]]

    tool_use_id: Required[str]

    type: Required[Literal["web_search_tool_result"]]

    cache_control: MessageContentContentBlockArrayMessageInputWebSearchToolResultBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputWebFetchToolResultBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputWebFetchToolResultBlock(TypedDict, total=False):
    """Anthropic compatibility only — SambaNova does not run server-side `web_fetch`.

    Echo of a prior Anthropic-served `web_fetch` tool call; accepted in conversation history but never originates from a SambaNova response. When present, only the text content is extracted.
    """

    content: Required[Dict[str, object]]

    tool_use_id: Required[str]

    type: Required[Literal["web_fetch_tool_result"]]

    cache_control: MessageContentContentBlockArrayMessageInputWebFetchToolResultBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputCodeExecutionToolResultBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputCodeExecutionToolResultBlock(TypedDict, total=False):
    """
    Anthropic compatibility only — SambaNova does not run server-side `code_execution`. Echo of a prior Anthropic-served `code_execution` tool call; accepted in conversation history but never originates from a SambaNova response. When present, only `stdout`, `stderr`, and `return_code` are extracted; image output is dropped.
    """

    content: Required[Dict[str, object]]

    tool_use_id: Required[str]

    type: Required[Literal["code_execution_tool_result"]]

    cache_control: MessageContentContentBlockArrayMessageInputCodeExecutionToolResultBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputBashCodeExecutionToolResultBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputBashCodeExecutionToolResultBlock(TypedDict, total=False):
    """
    Anthropic compatibility only — SambaNova does not run server-side bash code execution. Echo of a prior Anthropic-served bash tool call; accepted in conversation history but never originates from a SambaNova response. Same lossy extraction as `code_execution_tool_result`.
    """

    content: Required[Dict[str, object]]

    tool_use_id: Required[str]

    type: Required[Literal["bash_code_execution_tool_result"]]

    cache_control: MessageContentContentBlockArrayMessageInputBashCodeExecutionToolResultBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputTextEditorCodeExecutionToolResultBlockCacheControl(
    TypedDict, total=False
):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputTextEditorCodeExecutionToolResultBlock(TypedDict, total=False):
    """
    Anthropic compatibility only — SambaNova does not run server-side text-editor code execution. Echo of a prior Anthropic-served text-editor tool call; accepted in conversation history but never originates from a SambaNova response. When present, only file content is extracted; metadata (line count, file type) is dropped.
    """

    content: Required[Dict[str, object]]

    tool_use_id: Required[str]

    type: Required[Literal["text_editor_code_execution_tool_result"]]

    cache_control: MessageContentContentBlockArrayMessageInputTextEditorCodeExecutionToolResultBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputToolSearchToolResultBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputToolSearchToolResultBlock(TypedDict, total=False):
    """Anthropic compatibility only — SambaNova does not run server-side `tool_search`.

    Echo of a prior Anthropic-served `tool_search` tool call; accepted in conversation history but never originates from a SambaNova response. When present, an empty string is emitted to the tool message (no plain-text fields).
    """

    content: Required[Dict[str, object]]

    tool_use_id: Required[str]

    type: Required[Literal["tool_search_tool_result"]]

    cache_control: MessageContentContentBlockArrayMessageInputToolSearchToolResultBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputThinkingBlock(TypedDict, total=False):
    """Extended-reasoning trace from a prior assistant turn."""

    signature: Required[str]

    thinking: Required[str]

    type: Required[Literal["thinking"]]


class MessageContentContentBlockArrayMessageInputRedactedThinkingBlock(TypedDict, total=False):
    """
    Anthropic compatibility only — SambaNova does not produce encrypted thinking output. Echo of a prior Anthropic-served response where `thinking.display:"omitted"` was set. Accepted in conversation history but never originates from a SambaNova response. Silently dropped on input.
    """

    data: Required[str]

    type: Required[Literal["redacted_thinking"]]


class MessageContentContentBlockArrayMessageInputContainerUploadBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputContainerUploadBlock(TypedDict, total=False):
    """
    Anthropic compatibility only — SambaNova does not produce container_upload blocks (these come from Anthropic's server-side `code_execution` tool). Accepted in conversation history but never originates from a SambaNova response. Silently dropped on input.
    """

    file_id: Required[str]

    type: Required[Literal["container_upload"]]

    cache_control: MessageContentContentBlockArrayMessageInputContainerUploadBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """


class MessageContentContentBlockArrayMessageInputDocumentBlockCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class MessageContentContentBlockArrayMessageInputDocumentBlock(TypedDict, total=False):
    """PDF or document content.

    **Returns 400** — no document-extraction pipeline available.
    """

    source: Required[Dict[str, object]]

    type: Required[Literal["document"]]

    cache_control: MessageContentContentBlockArrayMessageInputDocumentBlockCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """

    citations: Optional[Dict[str, object]]

    context: Optional[str]

    title: Optional[str]


MessageContentContentBlockArray: TypeAlias = Union[
    MessageContentContentBlockArrayMessageInputTextBlock,
    MessageContentContentBlockArrayMessageInputImageBlock,
    MessageContentContentBlockArrayMessageInputToolUseBlock,
    MessageContentContentBlockArrayMessageInputToolResultBlock,
    MessageContentContentBlockArrayMessageInputServerToolUseBlock,
    MessageContentContentBlockArrayMessageInputSearchResultBlock,
    MessageContentContentBlockArrayMessageInputWebSearchToolResultBlock,
    MessageContentContentBlockArrayMessageInputWebFetchToolResultBlock,
    MessageContentContentBlockArrayMessageInputCodeExecutionToolResultBlock,
    MessageContentContentBlockArrayMessageInputBashCodeExecutionToolResultBlock,
    MessageContentContentBlockArrayMessageInputTextEditorCodeExecutionToolResultBlock,
    MessageContentContentBlockArrayMessageInputToolSearchToolResultBlock,
    MessageContentContentBlockArrayMessageInputThinkingBlock,
    MessageContentContentBlockArrayMessageInputRedactedThinkingBlock,
    MessageContentContentBlockArrayMessageInputContainerUploadBlock,
    MessageContentContentBlockArrayMessageInputDocumentBlock,
]


class Message(TypedDict, total=False):
    """A turn in the conversation."""

    content: Required[Union[str, Iterable[MessageContentContentBlockArray]]]

    role: Required[Literal["user", "assistant"]]
    """Conversational role.

    `user` for the human-side turn, `assistant` for prior model output.
    """


class SystemSystemTextBlockArrayCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class SystemSystemTextBlockArray(TypedDict, total=False):
    """A text segment within a structured `system` prompt array.

    Multiple text blocks are concatenated (with newlines) and prepended to the conversation as a `role: system` message at the chat-completions layer.
    """

    text: Required[str]
    """Plain-text content of the system prompt segment."""

    type: Required[Literal["text"]]

    cache_control: SystemSystemTextBlockArrayCacheControl
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """

    citations: Optional[Iterable[Dict[str, object]]]
    """Optional citations. **In v1**: silently dropped"""


class ThinkingMessageThinkingDisabled(TypedDict, total=False):
    """Disables Anthropic-style extended thinking.

    **In v1**: silently accepted as a no-op
    """

    type: Required[Literal["disabled"]]


class ThinkingMessageThinkingEnabled(TypedDict, total=False):
    """Enables Anthropic-style extended thinking with a fixed budget.

    **In v1**: returns a 400 `invalid_request_error` (`unsupported_parameter`).
    """

    budget_tokens: Required[int]
    """
    Maximum tokens the model may spend on extended thinking before producing the
    final answer.
    """

    type: Required[Literal["enabled"]]


class ThinkingMessageThinkingAdaptive(TypedDict, total=False):
    """Enables Anthropic-style adaptive extended thinking.

    **In v1**: returns a 400 `invalid_request_error` (`unsupported_parameter`).
    """

    type: Required[Literal["adaptive"]]

    budget_tokens: Optional[int]
    """Optional upper bound on tokens spent on adaptive thinking.

    When omitted, the backend chooses based on prompt complexity.
    """


Thinking: TypeAlias = Union[
    ThinkingMessageThinkingDisabled, ThinkingMessageThinkingEnabled, ThinkingMessageThinkingAdaptive
]


class ToolChoiceMessageToolChoiceAuto(TypedDict, total=False):
    """Let the model decide whether and which tool to use."""

    type: Required[Literal["auto"]]

    disable_parallel_tool_use: Optional[bool]
    """Silently dropped."""


class ToolChoiceMessageToolChoiceAny(TypedDict, total=False):
    """Require the model to call one of the provided tools."""

    type: Required[Literal["any"]]

    disable_parallel_tool_use: Optional[bool]
    """Silently dropped."""


class ToolChoiceMessageToolChoiceNone(TypedDict, total=False):
    """Forbid the model from calling any tool."""

    type: Required[Literal["none"]]


class ToolChoiceMessageToolChoiceTool(TypedDict, total=False):
    """Force the model to call a specific tool by name."""

    name: Required[str]
    """Name of the required tool."""

    type: Required[Literal["tool"]]

    disable_parallel_tool_use: Optional[bool]
    """Silently dropped."""


ToolChoice: TypeAlias = Union[
    ToolChoiceMessageToolChoiceAuto,
    ToolChoiceMessageToolChoiceAny,
    ToolChoiceMessageToolChoiceNone,
    ToolChoiceMessageToolChoiceTool,
]


class ToolCacheControl(TypedDict, total=False):
    """
    Marks the preceding content block (or system text block) as a prompt- cache breakpoint. Marker positions are collected by the adapter; their wiring into the router's longest-prefix matching **In v1**: position is recorded; the `ttl` value is ignored.
    """

    type: Required[Literal["ephemeral"]]
    """Cache breakpoint type. Only `ephemeral` is supported by Anthropic."""

    ttl: Optional[str]
    """Optional time-to-live hint (e.g. `"5m"`, `"1h"`). **Currently ignored** in v1"""


class Tool(TypedDict, total=False):
    """User-defined function tool definition.

    Only custom function tools are supported (Anthropic's `type:"custom"` style or the absent-type Beta style). Anthropic-hosted server tools (`web_search`, `code_execution`, `bash`, `text_editor`, `memory`, `tool_search` variants) return 400 `unsupported_tool_type` if sent.
    """

    name: Required[str]
    """Tool name. Must match `^[a-zA-Z0-9_-]+$`."""

    allowed_callers: Optional[SequenceNotStr[str]]
    """Silently dropped."""

    cache_control: Optional[ToolCacheControl]
    """
    Marks the preceding content block (or system text block) as a prompt- cache
    breakpoint. Marker positions are collected by the adapter; their wiring into the
    router's longest-prefix matching **In v1**: position is recorded; the `ttl`
    value is ignored.
    """

    defer_loading: Optional[bool]
    """Silently dropped."""

    description: Optional[str]
    """Human-readable description of when the tool should be used."""

    eager_input_streaming: Optional[bool]
    """Silently dropped."""

    input_examples: Optional[Iterable[Dict[str, object]]]
    """Silently dropped."""

    input_schema: Optional[Dict[str, object]]
    """JSON Schema describing the tool's expected input.

    Required by the Anthropic spec; accepted as optional by SambaNova.
    """

    strict: Optional[bool]
    """Silently dropped."""

    type: Optional[Literal["custom"]]
    """Tool-type discriminator.

    May be omitted (defaults to custom) or set to `custom`. Other values return 400
    `unsupported_tool_type`.
    """
