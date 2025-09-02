# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmbeddingCreateParams"]


class EmbeddingCreateParams(TypedDict, total=False):
    input: Required[Union[str, SequenceNotStr[str]]]
    """Input text to embed.

    to embed multiple inputs in a single request, pass an array of strings. The
    input must not exceed the max input tokens for the model
    """

    model: Required[Union[str, Literal["E5-Mistral-7B-Instruct"]]]
    """
    The model ID to use See available
    [models](https://docs.sambanova.ai/cloud/docs/get-started/supported-models)
    """
