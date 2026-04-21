# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .response_response import ResponseResponse

__all__ = [
    "ResponseStreamEvent",
    "ResponseCreatedEvent",
    "ResponseInProgressEvent",
    "ResponseOutputItemAddedEvent",
    "ResponseOutputItemAddedEventItem",
    "ResponseOutputItemAddedEventItemResponseMessage",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArray",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContent",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotation",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentLogprob",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseImageContent",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseAudioContent",
    "ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseAudioContentInputAudio",
    "ResponseOutputItemAddedEventItemResponseFunctionCall",
    "ResponseOutputItemAddedEventItemResponseOutputReasoning",
    "ResponseOutputItemAddedEventItemResponseOutputReasoningContent",
    "ResponseContentPartAddedEvent",
    "ResponseContentPartAddedEventPart",
    "ResponseContentPartAddedEventPartResponseTextContent",
    "ResponseContentPartAddedEventPartResponseTextContentAnnotation",
    "ResponseContentPartAddedEventPartResponseTextContentAnnotationResponseURLCitation",
    "ResponseContentPartAddedEventPartResponseTextContentAnnotationResponseFileCitation",
    "ResponseContentPartAddedEventPartResponseTextContentLogprob",
    "ResponseContentPartAddedEventPartResponseTextContentLogprobTopLogprobs",
    "ResponseContentPartAddedEventPartResponseReasoningContent",
    "ResponseReasoningTextDeltaEvent",
    "ResponseReasoningTextDoneEvent",
    "ResponseOutputTextDeltaEvent",
    "ResponseOutputTextDeltaEventAnnotation",
    "ResponseOutputTextDeltaEventAnnotationResponseURLCitation",
    "ResponseOutputTextDeltaEventAnnotationResponseFileCitation",
    "ResponseOutputTextDeltaEventLogprob",
    "ResponseOutputTextDeltaEventLogprobTopLogprobs",
    "ResponseOutputTextDoneEvent",
    "ResponseOutputTextDoneEventAnnotation",
    "ResponseOutputTextDoneEventAnnotationResponseURLCitation",
    "ResponseOutputTextDoneEventAnnotationResponseFileCitation",
    "ResponseOutputTextDoneEventLogprob",
    "ResponseOutputTextDoneEventLogprobTopLogprobs",
    "ResponseFunctionCallArgumentsDeltaEvent",
    "ResponseFunctionCallArgumentsDoneEvent",
    "ResponseContentPartDoneEvent",
    "ResponseContentPartDoneEventPart",
    "ResponseContentPartDoneEventPartResponseTextContent",
    "ResponseContentPartDoneEventPartResponseTextContentAnnotation",
    "ResponseContentPartDoneEventPartResponseTextContentAnnotationResponseURLCitation",
    "ResponseContentPartDoneEventPartResponseTextContentAnnotationResponseFileCitation",
    "ResponseContentPartDoneEventPartResponseTextContentLogprob",
    "ResponseContentPartDoneEventPartResponseTextContentLogprobTopLogprobs",
    "ResponseContentPartDoneEventPartResponseReasoningContent",
    "ResponseOutputItemDoneEvent",
    "ResponseOutputItemDoneEventItem",
    "ResponseOutputItemDoneEventItemResponseMessage",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArray",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContent",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotation",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentLogprob",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseImageContent",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseAudioContent",
    "ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseAudioContentInputAudio",
    "ResponseOutputItemDoneEventItemResponseFunctionCall",
    "ResponseOutputItemDoneEventItemResponseOutputReasoning",
    "ResponseOutputItemDoneEventItemResponseOutputReasoningContent",
    "ResponseCompletedEvent",
]


class ResponseCreatedEvent(BaseModel):
    """Emitted as the first SSE event when a streaming response begins.

    The embedded response object has status `in_progress` and an empty `output` array. Clients can use this event to capture the response `id` for later correlation.
    """

    response: ResponseResponse
    """A response object returned by POST /responses (non-streaming).

    Contains the model's output items, echoed input parameters, lifecycle metadata,
    and token usage.
    """

    sequence_number: int
    """Monotonically increasing counter for ordering events within a streaming
    response.

    Starts at 0 for `response.created`.
    """

    type: Literal["response.created"]


class ResponseInProgressEvent(BaseModel):
    """
    Emitted when the response transitions to the `in_progress` state, immediately after `response.created`. The embedded response object still has an empty `output` array; model generation has not yet produced any content.
    """

    response: ResponseResponse
    """A response object returned by POST /responses (non-streaming).

    Contains the model's output items, echoed input parameters, lifecycle metadata,
    and token usage.
    """

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.in_progress"]


class ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation(
    BaseModel
):
    """A URL citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["url_citation"]
    """The annotation type. Always "url_citation"."""

    url: str
    """The URL being cited."""

    title: Optional[str] = None
    """The title of the cited page."""


class ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation(
    BaseModel
):
    """A file citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    file_id: str
    """The ID of the cited file."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["file_citation"]
    """The annotation type. Always "file_citation"."""


ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotation: TypeAlias = Annotated[
    Union[
        ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation,
        ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs(
    BaseModel
):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentLogprob(BaseModel):
    token: str

    logprob: float

    top_logprobs: (
        ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs
    )

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContent(BaseModel):
    """A plain text content part for use inside a ResponseMessage."""

    text: str
    """The text content of this part."""

    type: Literal["input_text", "output_text"]
    """The type of this content part.

    "input_text" for user, developer, and system roles, and output_text for
    assistant messages.
    """

    annotations: Optional[
        List[ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotation]
    ] = None
    """Annotations on spans of this text part, such as URL or file citations.

    Only present on output_text parts returned by the server. Not currently produced
    by SambaNova — included for OpenAI API compatibility.
    """

    logprobs: Optional[
        List[ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContentLogprob]
    ] = None
    """Log probability information for the output tokens.

    Only present on output_text parts when `top_logprobs` is set on the request.
    """


class ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseImageContent(BaseModel):
    """An image content part for use inside a ResponseMessage.

    Supported in input messages (user role). Provide a base64-encoded image as a data URL. external URLs not supported.
    """

    image_url: Optional[str] = None
    """A base64-encoded image in data URL format or fully qualified URL (e.g.

    "data:image/png;base64,..."). Currently only base64-encoded image data is
    supported.
    """

    type: Literal["input_image"]
    """The type of this content part. Always "input_image"."""

    detail: Optional[Literal["auto", "low", "high"]] = None
    """The detail level for image processing.

    "auto" lets the model decide. "low" uses a fixed low-res tile. "high" enables
    high-res tiling.
    """


class ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseAudioContentInputAudio(BaseModel):
    """The audio data and format."""

    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data."""


class ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseAudioContent(BaseModel):
    """An audio content part for use inside a ResponseMessage.

    Supported in input messages (user role). Provide base64-encoded audio data with the format.
    """

    input_audio: ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseAudioContentInputAudio
    """The audio data and format."""

    type: Literal["input_audio"]
    """The type of this content part. Always "input_audio"."""


ResponseOutputItemAddedEventItemResponseMessageContentContentPartArray: TypeAlias = Union[
    ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseTextContent,
    ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseImageContent,
    ResponseOutputItemAddedEventItemResponseMessageContentContentPartArrayResponseAudioContent,
]


class ResponseOutputItemAddedEventItemResponseMessage(BaseModel):
    """A message item.

    When used as input, id and status are optional. When present in output[], id and status are always set by the server.  Role "assistant" with content type "output_text" represents a prior model turn; user/system/developer turns use content type "input_text". Plain string content is accepted in all roles on input.
    """

    content: Union[str, List[ResponseOutputItemAddedEventItemResponseMessageContentContentPartArray]]
    """The message content.

    Either a plain text string or an array of typed content parts. For assistant
    turns, array parts use type "output_text"; for user/system/developer turns,
    array parts use type "input_text".
    """

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message.

    "assistant" is set by the server on output items. All four values are valid when
    constructing input items.
    """

    type: Optional[Literal["message"]] = None
    """The type of this item. Always "message"."""

    id: Optional[str] = None
    """Unique identifier for this message item.

    Always present on output items returned by the server. Not required when
    constructing input items.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """Processing state of this item.

    Always set on output items returned by the server. Not required when
    constructing input items.
    """


class ResponseOutputItemAddedEventItemResponseFunctionCall(BaseModel):
    """A function call item used in both input[] and output[].

    When present in output[], the model is requesting a tool call — id and status are always set by the server. When used in input[], it replays a prior function call from the conversation history for multi-turn tool loops.
    """

    arguments: str
    """
    A JSON string of the arguments to pass to the function, as generated by the
    model. Validate the arguments in your code before calling the function — the
    model may hallucinate parameters not defined in the schema.
    """

    call_id: str
    """The call ID generated by the model for this tool invocation.

    Used to correlate the function call with its corresponding function_call_output
    result.
    """

    name: str
    """The name of the function the model wants to call."""

    type: Literal["function_call"]
    """The type of this item. Always "function_call"."""

    id: Optional[str] = None
    """Unique identifier for this function call item.

    Always present on output items returned by the server. Required when replaying
    this item in a subsequent input[].
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """Processing state of this item.

    Always set on output items returned by the server. Not required when
    constructing input items.
    """


class ResponseOutputItemAddedEventItemResponseOutputReasoningContent(BaseModel):
    """A single content part within a reasoning item's content[].

    Contains the raw reasoning text produced by the model during its internal thinking process.
    """

    text: str
    """The raw reasoning text generated by the model."""

    type: Literal["reasoning_text"]
    """The type of this reasoning content part. Always "reasoning_text"."""


class ResponseOutputItemAddedEventItemResponseOutputReasoning(BaseModel):
    """
    A reasoning item emitted in output[] by models that expose their internal chain-of-thought. Contains the raw reasoning text the model produced before generating its final answer.
    """

    type: Literal["reasoning"]
    """The type of this output item. Always "reasoning"."""

    id: Optional[str] = None
    """Unique identifier for this reasoning item, assigned by the server."""

    content: Optional[List[ResponseOutputItemAddedEventItemResponseOutputReasoningContent]] = None
    """The reasoning content parts.

    Each part has type "reasoning_text" and carries the raw thinking text. Absent
    when the item is first added (`response.output_item.added`); populated by
    `response.output_item.done`.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """Processing state of this item.

    "in_progress" while streaming; "completed" when the full reasoning text has been
    emitted.
    """

    summary: Optional[List[Dict[str, object]]] = None
    """A condensed summary of the reasoning content.

    Always returned as an empty array. Included for OpenAI API compatibility.
    """


ResponseOutputItemAddedEventItem: TypeAlias = Annotated[
    Union[
        ResponseOutputItemAddedEventItemResponseMessage,
        ResponseOutputItemAddedEventItemResponseFunctionCall,
        ResponseOutputItemAddedEventItemResponseOutputReasoning,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemAddedEvent(BaseModel):
    """
    Emitted when a new output item (message, function call, or reasoning) is added to the response output array. The item has `status: in_progress` and may have empty content at this point.
    """

    item: ResponseOutputItemAddedEventItem
    """A single item in the output[] array returned by the model.

    Can be a message (with text or tool call content), a function call request, or a
    reasoning trace. Discriminated by the "type" field.
    """

    output_index: int
    """Index of the output item in the response `output` array."""

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.output_item.added"]


class ResponseContentPartAddedEventPartResponseTextContentAnnotationResponseURLCitation(BaseModel):
    """A URL citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["url_citation"]
    """The annotation type. Always "url_citation"."""

    url: str
    """The URL being cited."""

    title: Optional[str] = None
    """The title of the cited page."""


class ResponseContentPartAddedEventPartResponseTextContentAnnotationResponseFileCitation(BaseModel):
    """A file citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    file_id: str
    """The ID of the cited file."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["file_citation"]
    """The annotation type. Always "file_citation"."""


ResponseContentPartAddedEventPartResponseTextContentAnnotation: TypeAlias = Annotated[
    Union[
        ResponseContentPartAddedEventPartResponseTextContentAnnotationResponseURLCitation,
        ResponseContentPartAddedEventPartResponseTextContentAnnotationResponseFileCitation,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseContentPartAddedEventPartResponseTextContentLogprobTopLogprobs(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseContentPartAddedEventPartResponseTextContentLogprob(BaseModel):
    token: str

    logprob: float

    top_logprobs: ResponseContentPartAddedEventPartResponseTextContentLogprobTopLogprobs

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseContentPartAddedEventPartResponseTextContent(BaseModel):
    """A plain text content part for use inside a ResponseMessage."""

    text: str
    """The text content of this part."""

    type: Literal["input_text", "output_text"]
    """The type of this content part.

    "input_text" for user, developer, and system roles, and output_text for
    assistant messages.
    """

    annotations: Optional[List[ResponseContentPartAddedEventPartResponseTextContentAnnotation]] = None
    """Annotations on spans of this text part, such as URL or file citations.

    Only present on output_text parts returned by the server. Not currently produced
    by SambaNova — included for OpenAI API compatibility.
    """

    logprobs: Optional[List[ResponseContentPartAddedEventPartResponseTextContentLogprob]] = None
    """Log probability information for the output tokens.

    Only present on output_text parts when `top_logprobs` is set on the request.
    """


class ResponseContentPartAddedEventPartResponseReasoningContent(BaseModel):
    """A single content part within a reasoning item's content[].

    Contains the raw reasoning text produced by the model during its internal thinking process.
    """

    text: str
    """The raw reasoning text generated by the model."""

    type: Literal["reasoning_text"]
    """The type of this reasoning content part. Always "reasoning_text"."""


ResponseContentPartAddedEventPart: TypeAlias = Union[
    ResponseContentPartAddedEventPartResponseTextContent, ResponseContentPartAddedEventPartResponseReasoningContent
]


class ResponseContentPartAddedEvent(BaseModel):
    """Emitted when a new content part is added to an output item's content array.

    The part's `text` is empty at this point; subsequent `response.output_text.delta` or `response.reasoning_text.delta` events carry the incremental content.
    """

    content_index: int
    """Index of this content part within the output item's `content` array."""

    item_id: str
    """ID of the output item to which this content part belongs."""

    output_index: int
    """Index of the parent output item in the response `output` array."""

    part: ResponseContentPartAddedEventPart
    """A content part within a streaming event.

    Discriminated by `type`: `output_text` for assistant message content (reuses
    ResponseTextContent), `reasoning_text` for model reasoning (OSS extension).
    """

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.content_part.added"]


class ResponseReasoningTextDeltaEvent(BaseModel):
    """Emitted for each incremental chunk of reasoning text generated by the model.

    Accumulate `delta` values in order to reconstruct the full reasoning text.
    """

    delta: str
    """The incremental chunk of reasoning text."""

    item_id: str
    """ID of the reasoning output item this delta belongs to."""

    output_index: int
    """Index of the reasoning output item in the response `output` array."""

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.reasoning_text.delta"]


class ResponseReasoningTextDoneEvent(BaseModel):
    """Emitted when a reasoning content part has been fully generated.

    The `text` field contains the complete accumulated reasoning text (equivalent to concatenating all preceding `response.reasoning_text.delta` values). Structural mirror of `response.reasoning_text.delta` with `text` instead of `delta`.
    """

    item_id: str
    """ID of the reasoning output item this content belongs to."""

    output_index: int
    """Index of the reasoning output item in the response `output` array."""

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    text: str
    """The full accumulated reasoning text for this content part."""

    type: Literal["response.reasoning_text.done"]


class ResponseOutputTextDeltaEventAnnotationResponseURLCitation(BaseModel):
    """A URL citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["url_citation"]
    """The annotation type. Always "url_citation"."""

    url: str
    """The URL being cited."""

    title: Optional[str] = None
    """The title of the cited page."""


class ResponseOutputTextDeltaEventAnnotationResponseFileCitation(BaseModel):
    """A file citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    file_id: str
    """The ID of the cited file."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["file_citation"]
    """The annotation type. Always "file_citation"."""


ResponseOutputTextDeltaEventAnnotation: TypeAlias = Annotated[
    Union[
        ResponseOutputTextDeltaEventAnnotationResponseURLCitation,
        ResponseOutputTextDeltaEventAnnotationResponseFileCitation,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputTextDeltaEventLogprobTopLogprobs(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseOutputTextDeltaEventLogprob(BaseModel):
    token: str

    logprob: float

    top_logprobs: ResponseOutputTextDeltaEventLogprobTopLogprobs

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseOutputTextDeltaEvent(BaseModel):
    """Emitted for each incremental chunk of assistant message text.

    Accumulate `delta` values in order to reconstruct the full output text.
    """

    annotations: List[ResponseOutputTextDeltaEventAnnotation]
    """Annotations attached to this delta chunk, if any."""

    content_index: int
    """Index of the content part within the output item's `content` array."""

    delta: str
    """The incremental chunk of output text."""

    item_id: str
    """ID of the message output item this delta belongs to."""

    logprobs: List[ResponseOutputTextDeltaEventLogprob]
    """Log probability information for the tokens in this delta, if requested."""

    output_index: int
    """Index of the message output item in the response `output` array."""

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.output_text.delta"]


class ResponseOutputTextDoneEventAnnotationResponseURLCitation(BaseModel):
    """A URL citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["url_citation"]
    """The annotation type. Always "url_citation"."""

    url: str
    """The URL being cited."""

    title: Optional[str] = None
    """The title of the cited page."""


class ResponseOutputTextDoneEventAnnotationResponseFileCitation(BaseModel):
    """A file citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    file_id: str
    """The ID of the cited file."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["file_citation"]
    """The annotation type. Always "file_citation"."""


ResponseOutputTextDoneEventAnnotation: TypeAlias = Annotated[
    Union[
        ResponseOutputTextDoneEventAnnotationResponseURLCitation,
        ResponseOutputTextDoneEventAnnotationResponseFileCitation,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputTextDoneEventLogprobTopLogprobs(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseOutputTextDoneEventLogprob(BaseModel):
    token: str

    logprob: float

    top_logprobs: ResponseOutputTextDoneEventLogprobTopLogprobs

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseOutputTextDoneEvent(BaseModel):
    """Emitted when an output text content part has been fully generated.

    The `text` field contains the complete accumulated output text (equivalent to concatenating all preceding `response.output_text.delta` values). Structural mirror of `response.output_text.delta` with `text` instead of `delta`.
    """

    annotations: List[ResponseOutputTextDoneEventAnnotation]
    """All annotations attached to this text part."""

    content_index: int
    """Index of the content part within the output item's `content` array."""

    item_id: str
    """ID of the message output item this content belongs to."""

    logprobs: List[ResponseOutputTextDoneEventLogprob]
    """Log probability information for all tokens, if requested."""

    output_index: int
    """Index of the message output item in the response `output` array."""

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    text: str
    """The full accumulated output text for this content part."""

    type: Literal["response.output_text.done"]


class ResponseFunctionCallArgumentsDeltaEvent(BaseModel):
    """
    Emitted for each incremental chunk of function call arguments JSON generated by the model. Accumulate `delta` values in order to reconstruct the full arguments string. The accumulated result will be a valid JSON string once the corresponding `response.function_call_arguments.done` event is received.
    """

    delta: str
    """The incremental chunk of the function call arguments JSON string."""

    item_id: str
    """ID of the function call output item this delta belongs to."""

    output_index: int
    """Index of the function call output item in the response `output` array."""

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.function_call_arguments.delta"]


class ResponseFunctionCallArgumentsDoneEvent(BaseModel):
    """Emitted when a function call's arguments have been fully generated.

    The `arguments` field contains the complete JSON arguments string (equivalent to concatenating all preceding `response.function_call_arguments.delta` values). Structural mirror of `response.function_call_arguments.delta` with `arguments` instead of `delta`.
    """

    arguments: str
    """The complete JSON arguments string for the function call."""

    item_id: str
    """ID of the function call output item."""

    output_index: int
    """Index of the function call output item in the response `output` array."""

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.function_call_arguments.done"]


class ResponseContentPartDoneEventPartResponseTextContentAnnotationResponseURLCitation(BaseModel):
    """A URL citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["url_citation"]
    """The annotation type. Always "url_citation"."""

    url: str
    """The URL being cited."""

    title: Optional[str] = None
    """The title of the cited page."""


class ResponseContentPartDoneEventPartResponseTextContentAnnotationResponseFileCitation(BaseModel):
    """A file citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    file_id: str
    """The ID of the cited file."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["file_citation"]
    """The annotation type. Always "file_citation"."""


ResponseContentPartDoneEventPartResponseTextContentAnnotation: TypeAlias = Annotated[
    Union[
        ResponseContentPartDoneEventPartResponseTextContentAnnotationResponseURLCitation,
        ResponseContentPartDoneEventPartResponseTextContentAnnotationResponseFileCitation,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseContentPartDoneEventPartResponseTextContentLogprobTopLogprobs(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseContentPartDoneEventPartResponseTextContentLogprob(BaseModel):
    token: str

    logprob: float

    top_logprobs: ResponseContentPartDoneEventPartResponseTextContentLogprobTopLogprobs

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseContentPartDoneEventPartResponseTextContent(BaseModel):
    """A plain text content part for use inside a ResponseMessage."""

    text: str
    """The text content of this part."""

    type: Literal["input_text", "output_text"]
    """The type of this content part.

    "input_text" for user, developer, and system roles, and output_text for
    assistant messages.
    """

    annotations: Optional[List[ResponseContentPartDoneEventPartResponseTextContentAnnotation]] = None
    """Annotations on spans of this text part, such as URL or file citations.

    Only present on output_text parts returned by the server. Not currently produced
    by SambaNova — included for OpenAI API compatibility.
    """

    logprobs: Optional[List[ResponseContentPartDoneEventPartResponseTextContentLogprob]] = None
    """Log probability information for the output tokens.

    Only present on output_text parts when `top_logprobs` is set on the request.
    """


class ResponseContentPartDoneEventPartResponseReasoningContent(BaseModel):
    """A single content part within a reasoning item's content[].

    Contains the raw reasoning text produced by the model during its internal thinking process.
    """

    text: str
    """The raw reasoning text generated by the model."""

    type: Literal["reasoning_text"]
    """The type of this reasoning content part. Always "reasoning_text"."""


ResponseContentPartDoneEventPart: TypeAlias = Union[
    ResponseContentPartDoneEventPartResponseTextContent, ResponseContentPartDoneEventPartResponseReasoningContent
]


class ResponseContentPartDoneEvent(BaseModel):
    """Emitted when a content part has been fully generated.

    The `part` field contains the complete content for this part (equivalent to the state after accumulating all preceding delta events). Structural mirror of `response.content_part.added`.
    """

    content_index: int
    """Index of this content part within the output item's `content` array."""

    item_id: str
    """ID of the output item this content part belongs to."""

    output_index: int
    """Index of the parent output item in the response `output` array."""

    part: ResponseContentPartDoneEventPart
    """A content part within a streaming event.

    Discriminated by `type`: `output_text` for assistant message content (reuses
    ResponseTextContent), `reasoning_text` for model reasoning (OSS extension).
    """

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.content_part.done"]


class ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation(
    BaseModel
):
    """A URL citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["url_citation"]
    """The annotation type. Always "url_citation"."""

    url: str
    """The URL being cited."""

    title: Optional[str] = None
    """The title of the cited page."""


class ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation(
    BaseModel
):
    """A file citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: int
    """Character offset in the output text where the citation ends."""

    file_id: str
    """The ID of the cited file."""

    start_index: int
    """Character offset in the output text where the citation starts."""

    type: Literal["file_citation"]
    """The annotation type. Always "file_citation"."""


ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotation: TypeAlias = Annotated[
    Union[
        ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation,
        ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs(
    BaseModel
):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentLogprob(BaseModel):
    token: str

    logprob: float

    top_logprobs: (
        ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs
    )

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContent(BaseModel):
    """A plain text content part for use inside a ResponseMessage."""

    text: str
    """The text content of this part."""

    type: Literal["input_text", "output_text"]
    """The type of this content part.

    "input_text" for user, developer, and system roles, and output_text for
    assistant messages.
    """

    annotations: Optional[
        List[ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentAnnotation]
    ] = None
    """Annotations on spans of this text part, such as URL or file citations.

    Only present on output_text parts returned by the server. Not currently produced
    by SambaNova — included for OpenAI API compatibility.
    """

    logprobs: Optional[
        List[ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContentLogprob]
    ] = None
    """Log probability information for the output tokens.

    Only present on output_text parts when `top_logprobs` is set on the request.
    """


class ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseImageContent(BaseModel):
    """An image content part for use inside a ResponseMessage.

    Supported in input messages (user role). Provide a base64-encoded image as a data URL. external URLs not supported.
    """

    image_url: Optional[str] = None
    """A base64-encoded image in data URL format or fully qualified URL (e.g.

    "data:image/png;base64,..."). Currently only base64-encoded image data is
    supported.
    """

    type: Literal["input_image"]
    """The type of this content part. Always "input_image"."""

    detail: Optional[Literal["auto", "low", "high"]] = None
    """The detail level for image processing.

    "auto" lets the model decide. "low" uses a fixed low-res tile. "high" enables
    high-res tiling.
    """


class ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseAudioContentInputAudio(BaseModel):
    """The audio data and format."""

    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data."""


class ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseAudioContent(BaseModel):
    """An audio content part for use inside a ResponseMessage.

    Supported in input messages (user role). Provide base64-encoded audio data with the format.
    """

    input_audio: ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseAudioContentInputAudio
    """The audio data and format."""

    type: Literal["input_audio"]
    """The type of this content part. Always "input_audio"."""


ResponseOutputItemDoneEventItemResponseMessageContentContentPartArray: TypeAlias = Union[
    ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseTextContent,
    ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseImageContent,
    ResponseOutputItemDoneEventItemResponseMessageContentContentPartArrayResponseAudioContent,
]


class ResponseOutputItemDoneEventItemResponseMessage(BaseModel):
    """A message item.

    When used as input, id and status are optional. When present in output[], id and status are always set by the server.  Role "assistant" with content type "output_text" represents a prior model turn; user/system/developer turns use content type "input_text". Plain string content is accepted in all roles on input.
    """

    content: Union[str, List[ResponseOutputItemDoneEventItemResponseMessageContentContentPartArray]]
    """The message content.

    Either a plain text string or an array of typed content parts. For assistant
    turns, array parts use type "output_text"; for user/system/developer turns,
    array parts use type "input_text".
    """

    role: Literal["user", "assistant", "system", "developer"]
    """The role of the message.

    "assistant" is set by the server on output items. All four values are valid when
    constructing input items.
    """

    type: Optional[Literal["message"]] = None
    """The type of this item. Always "message"."""

    id: Optional[str] = None
    """Unique identifier for this message item.

    Always present on output items returned by the server. Not required when
    constructing input items.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """Processing state of this item.

    Always set on output items returned by the server. Not required when
    constructing input items.
    """


class ResponseOutputItemDoneEventItemResponseFunctionCall(BaseModel):
    """A function call item used in both input[] and output[].

    When present in output[], the model is requesting a tool call — id and status are always set by the server. When used in input[], it replays a prior function call from the conversation history for multi-turn tool loops.
    """

    arguments: str
    """
    A JSON string of the arguments to pass to the function, as generated by the
    model. Validate the arguments in your code before calling the function — the
    model may hallucinate parameters not defined in the schema.
    """

    call_id: str
    """The call ID generated by the model for this tool invocation.

    Used to correlate the function call with its corresponding function_call_output
    result.
    """

    name: str
    """The name of the function the model wants to call."""

    type: Literal["function_call"]
    """The type of this item. Always "function_call"."""

    id: Optional[str] = None
    """Unique identifier for this function call item.

    Always present on output items returned by the server. Required when replaying
    this item in a subsequent input[].
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """Processing state of this item.

    Always set on output items returned by the server. Not required when
    constructing input items.
    """


class ResponseOutputItemDoneEventItemResponseOutputReasoningContent(BaseModel):
    """A single content part within a reasoning item's content[].

    Contains the raw reasoning text produced by the model during its internal thinking process.
    """

    text: str
    """The raw reasoning text generated by the model."""

    type: Literal["reasoning_text"]
    """The type of this reasoning content part. Always "reasoning_text"."""


class ResponseOutputItemDoneEventItemResponseOutputReasoning(BaseModel):
    """
    A reasoning item emitted in output[] by models that expose their internal chain-of-thought. Contains the raw reasoning text the model produced before generating its final answer.
    """

    type: Literal["reasoning"]
    """The type of this output item. Always "reasoning"."""

    id: Optional[str] = None
    """Unique identifier for this reasoning item, assigned by the server."""

    content: Optional[List[ResponseOutputItemDoneEventItemResponseOutputReasoningContent]] = None
    """The reasoning content parts.

    Each part has type "reasoning_text" and carries the raw thinking text. Absent
    when the item is first added (`response.output_item.added`); populated by
    `response.output_item.done`.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]] = None
    """Processing state of this item.

    "in_progress" while streaming; "completed" when the full reasoning text has been
    emitted.
    """

    summary: Optional[List[Dict[str, object]]] = None
    """A condensed summary of the reasoning content.

    Always returned as an empty array. Included for OpenAI API compatibility.
    """


ResponseOutputItemDoneEventItem: TypeAlias = Annotated[
    Union[
        ResponseOutputItemDoneEventItemResponseMessage,
        ResponseOutputItemDoneEventItemResponseFunctionCall,
        ResponseOutputItemDoneEventItemResponseOutputReasoning,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemDoneEvent(BaseModel):
    """
    Emitted when an output item has been fully generated and its status transitions to `completed`. The `item` field contains the complete output item including all accumulated content. Structural mirror of `response.output_item.added`.
    """

    item: ResponseOutputItemDoneEventItem
    """A single item in the output[] array returned by the model.

    Can be a message (with text or tool call content), a function call request, or a
    reasoning trace. Discriminated by the "type" field.
    """

    output_index: int
    """Index of the output item in the response `output` array."""

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.output_item.done"]


class ResponseCompletedEvent(BaseModel):
    """
    Emitted as the final SSE event when a streaming response has been fully generated. The embedded response object has `status: completed`, a fully populated `output` array, and a populated `usage` object. Structural mirror of `response.created`.
    """

    response: ResponseResponse
    """A response object returned by POST /responses (non-streaming).

    Contains the model's output items, echoed input parameters, lifecycle metadata,
    and token usage.
    """

    sequence_number: int
    """
    Monotonically increasing counter for ordering events within a streaming
    response.
    """

    type: Literal["response.completed"]


ResponseStreamEvent: TypeAlias = Annotated[
    Union[
        ResponseCreatedEvent,
        ResponseInProgressEvent,
        ResponseOutputItemAddedEvent,
        ResponseContentPartAddedEvent,
        ResponseReasoningTextDeltaEvent,
        ResponseReasoningTextDoneEvent,
        ResponseOutputTextDeltaEvent,
        ResponseOutputTextDoneEvent,
        ResponseFunctionCallArgumentsDeltaEvent,
        ResponseFunctionCallArgumentsDoneEvent,
        ResponseContentPartDoneEvent,
        ResponseOutputItemDoneEvent,
        ResponseCompletedEvent,
    ],
    PropertyInfo(discriminator="type"),
]
