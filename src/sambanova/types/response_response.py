# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResponseResponse",
    "Error",
    "IncompleteDetails",
    "Output",
    "OutputResponseMessage",
    "OutputResponseMessageContentContentPartArray",
    "OutputResponseMessageContentContentPartArrayResponseTextContent",
    "OutputResponseMessageContentContentPartArrayResponseTextContentAnnotation",
    "OutputResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation",
    "OutputResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation",
    "OutputResponseMessageContentContentPartArrayResponseTextContentLogprob",
    "OutputResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs",
    "OutputResponseMessageContentContentPartArrayResponseImageContent",
    "OutputResponseMessageContentContentPartArrayResponseAudioContent",
    "OutputResponseMessageContentContentPartArrayResponseAudioContentInputAudio",
    "OutputResponseFunctionCall",
    "OutputResponseOutputReasoning",
    "OutputResponseOutputReasoningContent",
    "ToolChoice",
    "ToolChoiceResponseNamedToolChoice",
    "Tool",
    "Reasoning",
    "Text",
    "TextFormat",
    "TextFormatResponseTextFormatText",
    "TextFormatResponseTextFormatJsonObject",
    "TextFormatResponseTextFormatJsonSchema",
    "Usage",
    "UsageInputTokensDetails",
    "UsageOutputTokensDetails",
]


class Error(BaseModel):
    """In-band error object present when status is "failed".

    Null when the response completed successfully.
    """

    code: str
    """The error code."""

    message: str
    """A human-readable error message."""


class IncompleteDetails(BaseModel):
    """Present when status is "incomplete".

    Describes why generation stopped before completion (e.g. max_output_tokens reached).
    """

    reason: Optional[str] = None
    """The reason why the response is incomplete."""


class OutputResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation(BaseModel):
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


class OutputResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation(BaseModel):
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


OutputResponseMessageContentContentPartArrayResponseTextContentAnnotation: TypeAlias = Annotated[
    Union[
        OutputResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation,
        OutputResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs(BaseModel):
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


class OutputResponseMessageContentContentPartArrayResponseTextContentLogprob(BaseModel):
    token: str

    logprob: float

    top_logprobs: OutputResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs

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


class OutputResponseMessageContentContentPartArrayResponseTextContent(BaseModel):
    """A plain text content part for use inside a ResponseMessage."""

    text: str
    """The text content of this part."""

    type: Literal["input_text", "output_text"]
    """The type of this content part.

    "input_text" for user, developer, and system roles, and output_text for
    assistant messages.
    """

    annotations: Optional[List[OutputResponseMessageContentContentPartArrayResponseTextContentAnnotation]] = None
    """Annotations on spans of this text part, such as URL or file citations.

    Only present on output_text parts returned by the server. Not currently produced
    by SambaNova — included for OpenAI API compatibility.
    """

    logprobs: Optional[List[OutputResponseMessageContentContentPartArrayResponseTextContentLogprob]] = None
    """Log probability information for the output tokens.

    Only present on output_text parts when `top_logprobs` is set on the request.
    """


class OutputResponseMessageContentContentPartArrayResponseImageContent(BaseModel):
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


class OutputResponseMessageContentContentPartArrayResponseAudioContentInputAudio(BaseModel):
    """The audio data and format."""

    data: str
    """Base64-encoded audio data."""

    format: Literal["mp3", "wav"]
    """The format of the audio data."""


class OutputResponseMessageContentContentPartArrayResponseAudioContent(BaseModel):
    """An audio content part for use inside a ResponseMessage.

    Supported in input messages (user role). Provide base64-encoded audio data with the format.
    """

    input_audio: OutputResponseMessageContentContentPartArrayResponseAudioContentInputAudio
    """The audio data and format."""

    type: Literal["input_audio"]
    """The type of this content part. Always "input_audio"."""


OutputResponseMessageContentContentPartArray: TypeAlias = Union[
    OutputResponseMessageContentContentPartArrayResponseTextContent,
    OutputResponseMessageContentContentPartArrayResponseImageContent,
    OutputResponseMessageContentContentPartArrayResponseAudioContent,
]


class OutputResponseMessage(BaseModel):
    """A message item.

    When used as input, id and status are optional. When present in output[], id and status are always set by the server.  Role "assistant" with content type "output_text" represents a prior model turn; user/system/developer turns use content type "input_text". Plain string content is accepted in all roles on input.
    """

    content: Union[str, List[OutputResponseMessageContentContentPartArray]]
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


class OutputResponseFunctionCall(BaseModel):
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


class OutputResponseOutputReasoningContent(BaseModel):
    """A single content part within a reasoning item's content[].

    Contains the raw reasoning text produced by the model during its internal thinking process.
    """

    text: str
    """The raw reasoning text generated by the model."""

    type: Literal["reasoning_text"]
    """The type of this reasoning content part. Always "reasoning_text"."""


class OutputResponseOutputReasoning(BaseModel):
    """
    A reasoning item emitted in output[] by models that expose their internal chain-of-thought. Contains the raw reasoning text the model produced before generating its final answer.
    """

    type: Literal["reasoning"]
    """The type of this output item. Always "reasoning"."""

    id: Optional[str] = None
    """Unique identifier for this reasoning item, assigned by the server."""

    content: Optional[List[OutputResponseOutputReasoningContent]] = None
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


Output: TypeAlias = Annotated[
    Union[OutputResponseMessage, OutputResponseFunctionCall, OutputResponseOutputReasoning],
    PropertyInfo(discriminator="type"),
]


class ToolChoiceResponseNamedToolChoice(BaseModel):
    """Forces the model to call a specific function.

    Pass this object as tool_choice to guarantee the model will invoke the named function.
    """

    name: str
    """The name of the function to call."""

    type: Literal["function"]
    """The type of tool to force. Always "function"."""


ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], ToolChoiceResponseNamedToolChoice]


class Tool(BaseModel):
    """A tool definition passed to the model via the tools[] array.

    Only type "function" is supported; other tool types are filtered server-side.
    """

    name: str
    """The name of the function to be called."""

    type: Literal["function"]
    """The type of tool. Always "function"."""

    description: Optional[str] = None
    """A description of what the function does.

    Used by the model to decide when and whether to call it.
    """

    parameters: Optional[Dict[str, object]] = None
    """The parameters the function accepts, described as a JSON Schema object.

    Omit or set to null for functions that take no parameters.
    """

    strict: Optional[bool] = None
    """
    When true, the model is instructed to generate arguments that strictly conform
    to the provided JSON schema. Not currently enforced by SambaNova accepted for
    API compatibility and echoed back as null in the response.
    """


class Reasoning(BaseModel):
    """The reasoning configuration used for this response."""

    effort: Optional[Literal["low", "medium", "high"]] = None
    """The reasoning effort level that was applied for supported models."""

    summary: Optional[str] = None
    """Not supported."""


class TextFormatResponseTextFormatText(BaseModel):
    """Specifies that the model should produce output as plain text.

    This is the default.
    """

    type: Literal["text"]
    """The format type. Always "text"."""


class TextFormatResponseTextFormatJsonObject(BaseModel):
    """Specifies that the model should produce output as a raw JSON object.

    The model is not constrained to any specific schema.
    """

    type: Literal["json_object"]
    """The format type. Always "json_object"."""


class TextFormatResponseTextFormatJsonSchema(BaseModel):
    """
    Specifies that the model should produce structured output conforming to the provided JSON Schema. Unlike the Chat Completions API, the Responses API places name, schema, strict, and description directly on this object (not nested under a json_schema key).
    """

    name: str
    """A name for the schema, used to identify it in the model's output."""

    type: Literal["json_schema"]
    """The format type. Always "json_schema"."""

    description: Optional[str] = None
    """An optional description of the schema, used to guide the model."""

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)
    """A JSON Schema object defining the structure the model's output must conform to.

    Typically includes "type", "properties", "required", and optionally
    "additionalProperties". Must be a valid JSON Schema.
    """

    strict: Optional[bool] = None
    """
    When true, the model is instructed to produce output that strictly matches the
    schema. Not currently enforced by SambaNova — accepted for API compatibility.
    """


TextFormat: TypeAlias = Annotated[
    Union[
        TextFormatResponseTextFormatText, TextFormatResponseTextFormatJsonObject, TextFormatResponseTextFormatJsonSchema
    ],
    PropertyInfo(discriminator="type"),
]


class Text(BaseModel):
    """The text format configuration (structured output mode) used for this response."""

    format: Optional[TextFormat] = None
    """
    Controls the format of the model's output for the Responses API text.format
    field. "text" returns plain text (default). "json_object" returns a raw JSON
    object. "json_schema" enforces structured output matching a provided JSON Schema
    definition (fields are flat — no json_schema wrapper key).
    """


class UsageInputTokensDetails(BaseModel):
    """Breakdown of input token consumption."""

    cached_tokens: Optional[int] = None
    """Number of input tokens served from the prompt cache.

    Cached tokens are billed at a reduced rate.
    """


class UsageOutputTokensDetails(BaseModel):
    """Breakdown of output token consumption."""

    reasoning_tokens: Optional[int] = None
    """Number of tokens consumed by the model's internal reasoning process.

    Only present on reasoning-capable models.
    """


class Usage(BaseModel):
    """Token usage statistics for this response."""

    input_tokens: int
    """
    Number of tokens in the input, including conversation history and any system
    instructions.
    """

    output_tokens: int
    """
    Number of tokens generated in the output, including visible text and any
    reasoning tokens.
    """

    total_tokens: int
    """Total tokens consumed by this request (input + output)."""

    acceptance_rate: Optional[float] = None
    """Speculative decoding acceptance rate.

    Ratio of draft tokens accepted by the verifier model. Higher values indicate
    better speculation efficiency.
    """

    end_time: Optional[float] = None
    """Unix timestamp (seconds) of when generation finished."""

    input_tokens_details: Optional[UsageInputTokensDetails] = None
    """Breakdown of input token consumption."""

    is_last_response: Optional[bool] = None
    """Always true for non-streaming responses.

    For streaming, true only on the final chunk that carries usage.
    """

    output_tokens_after_first_per_sec: Optional[float] = None
    """Output token throughput measured after the first token was emitted.

    Excludes the time-to-first-token latency from the rate calculation.
    """

    output_tokens_details: Optional[UsageOutputTokensDetails] = None
    """Breakdown of output token consumption."""

    output_tokens_per_sec: Optional[float] = None
    """Output token throughput (tokens/second) for this response."""

    start_time: Optional[float] = None
    """Unix timestamp (seconds) of when generation started."""

    time_to_first_token: Optional[float] = None
    """Time in seconds from request receipt to first output token (TTFT)."""

    total_latency: Optional[float] = None
    """Total time in seconds taken to generate the full response."""

    total_tokens_per_sec: Optional[float] = None
    """Total token throughput (input + output tokens/second)."""


class ResponseResponse(BaseModel):
    """A response object returned by POST /responses (non-streaming).

    Contains the model's output items, echoed input parameters, lifecycle metadata, and token usage.
    """

    id: str
    """Unique identifier for this response."""

    background: Optional[bool] = None
    """Whether background generation was requested."""

    created_at: int
    """Unix timestamp (seconds) when the response was created."""

    error: Optional[Error] = None
    """In-band error object present when status is "failed".

    Null when the response completed successfully.
    """

    frequency_penalty: Optional[float] = None
    """The frequency_penalty value echoed from the request.

    Not currently implemented; accepted for API compatibility
    """

    incomplete_details: Optional[IncompleteDetails] = None
    """Present when status is "incomplete".

    Describes why generation stopped before completion (e.g. max_output_tokens
    reached).
    """

    metadata: Optional[Dict[str, str]] = None
    """The metadata echoed from the request."""

    model: str
    """The model ID used to generate this response."""

    object: Literal["response"]
    """The object type. Always "response"."""

    output: List[Output]
    """Ordered array of output items generated by the model.

    Items may be of type "message", "reasoning", or "function_call".
    """

    parallel_tool_calls: bool
    """Whether parallel tool calls were enabled."""

    presence_penalty: Optional[float] = None
    """The presence_penalty value echoed from the request.

    Not currently implemented; accepted for API compatibility
    """

    service_tier: Optional[str] = None
    """The service tier used to process this request, as reported by the server."""

    status: Literal["completed", "failed", "in_progress", "incomplete"]
    """Lifecycle status of the response.

    "completed" means the model finished successfully. "failed" means an error
    occurred during generation. "incomplete" means generation was cut short (e.g.
    max_output_tokens reached).
    """

    store: Optional[bool] = None
    """Whether the response was stored server-side.

    SambaNova is stateless - always false.
    """

    temperature: Optional[float] = None
    """The temperature value used for this response."""

    tool_choice: ToolChoice
    """Controls which tool (if any) the model calls.

    String values: "none" disables tool calls; "auto" lets the model decide;
    "required" forces at least one tool call. To force a specific function, provide
    a ResponseNamedToolChoice object.
    """

    tools: List[Tool]
    """Tool definitions available to the model for this response."""

    top_p: Optional[float] = None
    """The top_p value used for this response."""

    truncation: Optional[Literal["auto", "disabled"]] = None
    """The truncation value echoed from the request."""

    user: Optional[str] = None
    """The user, echoed back from request."""

    completed_at: Optional[int] = None
    """Unix timestamp (seconds) when the response finished generating."""

    instructions: Optional[str] = None
    """The system instructions echoed from the request, or null if none were provided."""

    max_output_tokens: Optional[int] = None
    """The max_output_tokens limit echoed from the request."""

    max_tool_calls: Optional[int] = None
    """The max_tool_calls value echoed from the request."""

    previous_response_id: Optional[str] = None
    """Not supported.

    Always null. SambaNova is stateless; use input[] to supply full conversation
    history.
    """

    reasoning: Optional[Reasoning] = None
    """The reasoning configuration used for this response."""

    text: Optional[Text] = None
    """The text format configuration (structured output mode) used for this response."""

    top_k: Optional[int] = None
    """The top_k value used for this response."""

    top_logprobs: Optional[int] = None
    """The top_logprobs value echoed from the request."""

    usage: Optional[Usage] = None
    """Token usage statistics for this response."""
