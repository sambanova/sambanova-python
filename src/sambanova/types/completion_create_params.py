# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "CompletionCreateParamsBase",
    "StreamOptions",
    "CompletionCreateParamsNonStreaming",
    "CompletionCreateParamsStreaming",
]


class CompletionCreateParamsBase(TypedDict, total=False):
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
                "DeepSeek-R1",
                "DeepSeek-R1-0528",
                "DeepSeek-V3-0324",
                "DeepSeek-V3.1",
                "DeepSeek-V3.1-Terminus",
                "DeepSeek-R1-Distill-Llama-70B",
                "Llama-4-Maverick-17B-128E-Instruct",
                "Llama-4-Scout-17B-16E-Instruct",
                "Qwen3-32B",
                "Llama-3.3-Swallow-70B-Instruct-v0.4",
                "gpt-oss-120b",
                "ALLaM-7B-Instruct-preview",
            ],
        ]
    ]
    """The model ID to use (e.g.

    Meta-Llama-3.3-70B-Instruct). See available
    [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)
    """

    prompt: Required[str]
    """Prompt to send to the model."""

    do_sample: Optional[bool]
    """If true, sampling is enabled during output generation.

    If false, deterministic decoding is used.
    """

    frequency_penalty: float
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """

    logit_bias: Optional[Dict[str, int]]
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

    presence_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.
    """

    seed: Optional[int]
    """This is not yet supported by our models."""

    stop: Union[Optional[str], SequenceNotStr[str], None]
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


class StreamOptionsTyped(TypedDict, total=False):
    include_usage: Optional[bool]
    """Whether to include the usage metrics in a final chunk or not"""


StreamOptions: TypeAlias = Union[StreamOptionsTyped, Dict[str, object]]


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Optional[Literal[False]]
    """If set, partial message deltas will be sent.

    Tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message.
    """


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """If set, partial message deltas will be sent.

    Tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message.
    """


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
