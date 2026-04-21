# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ResponseCreateParamsBase",
    "InputInputItemList",
    "InputInputItemListResponseMessage",
    "InputInputItemListResponseMessageContentContentPartArray",
    "InputInputItemListResponseMessageContentContentPartArrayResponseTextContent",
    "InputInputItemListResponseMessageContentContentPartArrayResponseTextContentAnnotation",
    "InputInputItemListResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation",
    "InputInputItemListResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation",
    "InputInputItemListResponseMessageContentContentPartArrayResponseTextContentLogprob",
    "InputInputItemListResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs",
    "InputInputItemListResponseMessageContentContentPartArrayResponseImageContent",
    "InputInputItemListResponseMessageContentContentPartArrayResponseAudioContent",
    "InputInputItemListResponseMessageContentContentPartArrayResponseAudioContentInputAudio",
    "InputInputItemListResponseFunctionCall",
    "InputInputItemListResponseFunctionCallOutput",
    "InputInputItemListResponseOutputReasoning",
    "InputInputItemListResponseOutputReasoningContent",
    "Reasoning",
    "Text",
    "TextFormat",
    "TextFormatResponseTextFormatText",
    "TextFormatResponseTextFormatJsonObject",
    "TextFormatResponseTextFormatJsonSchema",
    "ToolChoice",
    "ToolChoiceResponseNamedToolChoice",
    "Tool",
    "ResponseCreateParamsNonStreaming",
    "ResponseCreateParamsStreaming",
]


class ResponseCreateParamsBase(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputInputItemList]]]
    """
    Text input to the model, or a structured list of input items representing the
    full conversation turn. A plain string is equivalent to a single user message.
    """

    model: Required[Union[str, Literal["gpt-oss-120b"]]]
    """The model ID to use (e.g.

    gpt-oss-120b). See available
    [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)
    """

    background: Optional[bool]
    """Accepted for API compatibility and echoed back in the response.

    Has no effect on server behavior.
    """

    frequency_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.
    Not currently implemented; accepted for API compatibility and echoed in the
    response.
    """

    instructions: Optional[str]
    """Inserts a system (or developer) message as the first item in the model's
    context.

    Equivalent to a system-role message prepended to input[].
    """

    max_output_tokens: Optional[int]
    """
    Upper bound on the number of tokens the model may generate, including visible
    output tokens and reasoning tokens.
    """

    max_tool_calls: Optional[int]
    """Maximum number of tool calls the model may make in a single response turn.

    Not currently implemented; accepted for API compatibility.
    """

    metadata: Optional[Dict[str, str]]
    """Included for API compatibility, but not supported"""

    parallel_tool_calls: Optional[bool]
    """Whether the model may issue multiple tool calls in parallel within one turn."""

    presence_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics. Not currently
    implemented; accepted for API compatibility and echoed in the response.
    """

    previous_response_id: Optional[str]
    """Not supported.

    SambaNova is stateless and does not maintain server-side conversation state.
    Accepted for API compatibility but ignored; clients must supply the full
    conversation history in input[].
    """

    reasoning: Optional[Reasoning]
    """Reasoning configuration for models that support it.

    Ignored on non-reasoning models.
    """

    service_tier: Optional[str]
    """Accepted for API compatibility and echoed back in the response.

    Has no effect on server behavior.
    """

    store: Optional[bool]
    """
    SambaNova is stateless - this field is accepted for API compatibility but has no
    effect. Always echoed back as false.
    """

    temperature: Optional[float]
    """Controls randomness in generation.

    Range: 0–2. It is recommended to alter this, top_p, or top_k but not more than
    one at a time.
    """

    text: Text
    """Response format configuration.

    Supports plain text, json_object, and json_schema.
    """

    tool_choice: ToolChoice
    """Controls which tool (if any) the model calls.

    String values: "none" disables tool calls; "auto" lets the model decide;
    "required" forces at least one tool call. To force a specific function, provide
    a ResponseNamedToolChoice object.
    """

    tools: Optional[Iterable[Tool]]
    """Tools available to the model.

    Only type: "function" is supported; all other tool types are filtered
    server-side.
    """

    top_k: Optional[int]
    """Limits sampling to the top K most probable tokens.

    It is recommended to alter this, top_p, or temperature but not more than one at
    a time.
    """

    top_logprobs: Optional[int]
    """Number of top log-probability entries to return per output token.

    Null means log probabilities are not returned.
    """

    top_p: Optional[float]
    """Nucleus sampling cutoff.

    Range: 0–1. It is recommended to alter this, temperature, or top_k but not more
    than one at a time.
    """

    truncation: Optional[Literal["auto", "disabled"]]
    """Accepted for API compatibility and echoed in the response.

    Context truncation behavior is not currently configurable via this field in
    SambaNova.
    """

    user: Optional[str]
    """Included for API compatibility, but only echoed back in response"""


class InputInputItemListResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation(
    TypedDict, total=False
):
    """A URL citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: Required[int]
    """Character offset in the output text where the citation ends."""

    start_index: Required[int]
    """Character offset in the output text where the citation starts."""

    type: Required[Literal["url_citation"]]
    """The annotation type. Always "url_citation"."""

    url: Required[str]
    """The URL being cited."""

    title: Optional[str]
    """The title of the cited page."""


class InputInputItemListResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation(
    TypedDict, total=False
):
    """A file citation annotation on an output text span.

    Not currently implemented by SambaNova — included for OpenAI API compatibility.
    """

    end_index: Required[int]
    """Character offset in the output text where the citation ends."""

    file_id: Required[str]
    """The ID of the cited file."""

    start_index: Required[int]
    """Character offset in the output text where the citation starts."""

    type: Required[Literal["file_citation"]]
    """The annotation type. Always "file_citation"."""


InputInputItemListResponseMessageContentContentPartArrayResponseTextContentAnnotation: TypeAlias = Union[
    InputInputItemListResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseURLCitation,
    InputInputItemListResponseMessageContentContentPartArrayResponseTextContentAnnotationResponseFileCitation,
]


class InputInputItemListResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object  # pyright: ignore[reportGeneralTypeIssues]
):
    token: Required[str]

    logprob: Required[float]

    bytes: Optional[Iterable[int]]


class InputInputItemListResponseMessageContentContentPartArrayResponseTextContentLogprob(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object  # pyright: ignore[reportGeneralTypeIssues]
):
    token: Required[str]

    logprob: Required[float]

    top_logprobs: Required[
        InputInputItemListResponseMessageContentContentPartArrayResponseTextContentLogprobTopLogprobs
    ]

    bytes: Optional[Iterable[int]]


class InputInputItemListResponseMessageContentContentPartArrayResponseTextContent(TypedDict, total=False):
    """A plain text content part for use inside a ResponseMessage."""

    text: Required[str]
    """The text content of this part."""

    type: Required[Literal["input_text", "output_text"]]
    """The type of this content part.

    "input_text" for user, developer, and system roles, and output_text for
    assistant messages.
    """

    annotations: Optional[
        Iterable[InputInputItemListResponseMessageContentContentPartArrayResponseTextContentAnnotation]
    ]
    """Annotations on spans of this text part, such as URL or file citations.

    Only present on output_text parts returned by the server. Not currently produced
    by SambaNova — included for OpenAI API compatibility.
    """

    logprobs: Optional[Iterable[InputInputItemListResponseMessageContentContentPartArrayResponseTextContentLogprob]]
    """Log probability information for the output tokens.

    Only present on output_text parts when `top_logprobs` is set on the request.
    """


class InputInputItemListResponseMessageContentContentPartArrayResponseImageContent(TypedDict, total=False):
    """An image content part for use inside a ResponseMessage.

    Supported in input messages (user role). Provide a base64-encoded image as a data URL. external URLs not supported.
    """

    image_url: Required[Optional[str]]
    """A base64-encoded image in data URL format or fully qualified URL (e.g.

    "data:image/png;base64,..."). Currently only base64-encoded image data is
    supported.
    """

    type: Required[Literal["input_image"]]
    """The type of this content part. Always "input_image"."""

    detail: Optional[Literal["auto", "low", "high"]]
    """The detail level for image processing.

    "auto" lets the model decide. "low" uses a fixed low-res tile. "high" enables
    high-res tiling.
    """


class InputInputItemListResponseMessageContentContentPartArrayResponseAudioContentInputAudio(TypedDict, total=False):
    """The audio data and format."""

    data: Required[str]
    """Base64-encoded audio data."""

    format: Required[Literal["mp3", "wav"]]
    """The format of the audio data."""


class InputInputItemListResponseMessageContentContentPartArrayResponseAudioContent(TypedDict, total=False):
    """An audio content part for use inside a ResponseMessage.

    Supported in input messages (user role). Provide base64-encoded audio data with the format.
    """

    input_audio: Required[InputInputItemListResponseMessageContentContentPartArrayResponseAudioContentInputAudio]
    """The audio data and format."""

    type: Required[Literal["input_audio"]]
    """The type of this content part. Always "input_audio"."""


InputInputItemListResponseMessageContentContentPartArray: TypeAlias = Union[
    InputInputItemListResponseMessageContentContentPartArrayResponseTextContent,
    InputInputItemListResponseMessageContentContentPartArrayResponseImageContent,
    InputInputItemListResponseMessageContentContentPartArrayResponseAudioContent,
]


class InputInputItemListResponseMessage(TypedDict, total=False):
    """A message item.

    When used as input, id and status are optional. When present in output[], id and status are always set by the server.  Role "assistant" with content type "output_text" represents a prior model turn; user/system/developer turns use content type "input_text". Plain string content is accepted in all roles on input.
    """

    content: Required[Union[str, Iterable[InputInputItemListResponseMessageContentContentPartArray]]]
    """The message content.

    Either a plain text string or an array of typed content parts. For assistant
    turns, array parts use type "output_text"; for user/system/developer turns,
    array parts use type "input_text".
    """

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message.

    "assistant" is set by the server on output items. All four values are valid when
    constructing input items.
    """

    type: Required[Optional[Literal["message"]]]
    """The type of this item. Always "message"."""

    id: Optional[str]
    """Unique identifier for this message item.

    Always present on output items returned by the server. Not required when
    constructing input items.
    """

    status: Literal["in_progress", "completed", "incomplete"]
    """Processing state of this item.

    Always set on output items returned by the server. Not required when
    constructing input items.
    """


class InputInputItemListResponseFunctionCall(TypedDict, total=False):
    """A function call item used in both input[] and output[].

    When present in output[], the model is requesting a tool call — id and status are always set by the server. When used in input[], it replays a prior function call from the conversation history for multi-turn tool loops.
    """

    arguments: Required[str]
    """
    A JSON string of the arguments to pass to the function, as generated by the
    model. Validate the arguments in your code before calling the function — the
    model may hallucinate parameters not defined in the schema.
    """

    call_id: Required[str]
    """The call ID generated by the model for this tool invocation.

    Used to correlate the function call with its corresponding function_call_output
    result.
    """

    name: Required[str]
    """The name of the function the model wants to call."""

    type: Required[Literal["function_call"]]
    """The type of this item. Always "function_call"."""

    id: Optional[str]
    """Unique identifier for this function call item.

    Always present on output items returned by the server. Required when replaying
    this item in a subsequent input[].
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """Processing state of this item.

    Always set on output items returned by the server. Not required when
    constructing input items.
    """


class InputInputItemListResponseFunctionCallOutput(TypedDict, total=False):
    """
    A tool result item used in input[] to return the output of a function call back to the model. Always input-only — the model never outputs function_call_output items. The call_id must match the id of the corresponding ResponseFunctionCall item from the prior model turn.
    """

    call_id: Required[str]
    """The call_id of the ResponseFunctionCall item this result corresponds to.

    Must match exactly.
    """

    output: Required[str]
    """A JSON string containing the result of the function call.

    Returned to the model as the tool's response.
    """

    type: Required[Literal["function_call_output"]]
    """The type of this item. Always "function_call_output"."""

    id: Optional[str]
    """Optional identifier for this output item."""

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """Processing state. Optional when constructing input items."""


class InputInputItemListResponseOutputReasoningContent(TypedDict, total=False):
    """A single content part within a reasoning item's content[].

    Contains the raw reasoning text produced by the model during its internal thinking process.
    """

    text: Required[str]
    """The raw reasoning text generated by the model."""

    type: Required[Literal["reasoning_text"]]
    """The type of this reasoning content part. Always "reasoning_text"."""


class InputInputItemListResponseOutputReasoning(TypedDict, total=False):
    """
    A reasoning item emitted in output[] by models that expose their internal chain-of-thought. Contains the raw reasoning text the model produced before generating its final answer.
    """

    type: Required[Literal["reasoning"]]
    """The type of this output item. Always "reasoning"."""

    id: Optional[str]
    """Unique identifier for this reasoning item, assigned by the server."""

    content: Optional[Iterable[InputInputItemListResponseOutputReasoningContent]]
    """The reasoning content parts.

    Each part has type "reasoning_text" and carries the raw thinking text. Absent
    when the item is first added (`response.output_item.added`); populated by
    `response.output_item.done`.
    """

    status: Optional[Literal["in_progress", "completed", "incomplete"]]
    """Processing state of this item.

    "in_progress" while streaming; "completed" when the full reasoning text has been
    emitted.
    """

    summary: Optional[Iterable[Dict[str, object]]]
    """A condensed summary of the reasoning content.

    Always returned as an empty array. Included for OpenAI API compatibility.
    """


InputInputItemList: TypeAlias = Union[
    InputInputItemListResponseMessage,
    InputInputItemListResponseFunctionCall,
    InputInputItemListResponseFunctionCallOutput,
    InputInputItemListResponseOutputReasoning,
]


class Reasoning(TypedDict, total=False):
    """Reasoning configuration for models that support it.

    Ignored on non-reasoning models.
    """

    effort: Optional[Literal["low", "medium", "high"]]
    """Reasoning effort level.

    "low" is faster with less depth; "high" is deeper at higher token cost.
    """


class TextFormatResponseTextFormatText(TypedDict, total=False):
    """Specifies that the model should produce output as plain text.

    This is the default.
    """

    type: Required[Literal["text"]]
    """The format type. Always "text"."""


class TextFormatResponseTextFormatJsonObject(TypedDict, total=False):
    """Specifies that the model should produce output as a raw JSON object.

    The model is not constrained to any specific schema.
    """

    type: Required[Literal["json_object"]]
    """The format type. Always "json_object"."""


class TextFormatResponseTextFormatJsonSchema(TypedDict, total=False):
    """
    Specifies that the model should produce structured output conforming to the provided JSON Schema. Unlike the Chat Completions API, the Responses API places name, schema, strict, and description directly on this object (not nested under a json_schema key).
    """

    name: Required[str]
    """A name for the schema, used to identify it in the model's output."""

    type: Required[Literal["json_schema"]]
    """The format type. Always "json_schema"."""

    description: Optional[str]
    """An optional description of the schema, used to guide the model."""

    schema: Optional[Dict[str, object]]
    """A JSON Schema object defining the structure the model's output must conform to.

    Typically includes "type", "properties", "required", and optionally
    "additionalProperties". Must be a valid JSON Schema.
    """

    strict: Optional[bool]
    """
    When true, the model is instructed to produce output that strictly matches the
    schema. Not currently enforced by SambaNova — accepted for API compatibility.
    """


TextFormat: TypeAlias = Union[
    TextFormatResponseTextFormatText, TextFormatResponseTextFormatJsonObject, TextFormatResponseTextFormatJsonSchema
]


class Text(TypedDict, total=False):
    """Response format configuration.

    Supports plain text, json_object, and json_schema.
    """

    format: TextFormat
    """
    Controls the format of the model's output for the Responses API text.format
    field. "text" returns plain text (default). "json_object" returns a raw JSON
    object. "json_schema" enforces structured output matching a provided JSON Schema
    definition (fields are flat — no json_schema wrapper key).
    """


class ToolChoiceResponseNamedToolChoice(TypedDict, total=False):
    """Forces the model to call a specific function.

    Pass this object as tool_choice to guarantee the model will invoke the named function.
    """

    name: Required[str]
    """The name of the function to call."""

    type: Required[Literal["function"]]
    """The type of tool to force. Always "function"."""


ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], ToolChoiceResponseNamedToolChoice]


class Tool(TypedDict, total=False):
    """A tool definition passed to the model via the tools[] array.

    Only type "function" is supported; other tool types are filtered server-side.
    """

    name: Required[str]
    """The name of the function to be called."""

    type: Required[Literal["function"]]
    """The type of tool. Always "function"."""

    description: Optional[str]
    """A description of what the function does.

    Used by the model to decide when and whether to call it.
    """

    parameters: Optional[Dict[str, object]]
    """The parameters the function accepts, described as a JSON Schema object.

    Omit or set to null for functions that take no parameters.
    """

    strict: Optional[bool]
    """
    When true, the model is instructed to generate arguments that strictly conform
    to the provided JSON schema. Not currently enforced by SambaNova accepted for
    API compatibility and echoed back as null in the response.
    """


class ResponseCreateParamsNonStreaming(ResponseCreateParamsBase, total=False):
    stream: Optional[Literal[False]]
    """If true, the response is delivered as server-sent events (SSE)."""


class ResponseCreateParamsStreaming(ResponseCreateParamsBase):
    stream: Required[Literal[True]]
    """If true, the response is delivered as server-sent events (SSE)."""


ResponseCreateParams = Union[ResponseCreateParamsNonStreaming, ResponseCreateParamsStreaming]
