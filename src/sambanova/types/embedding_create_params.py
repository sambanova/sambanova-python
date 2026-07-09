# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
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
    [models](https://docs.sambanova.ai/docs/en/models/sambacloud-models)
    """

    encoding_format: Optional[Literal["float", "base64"]]
    """The format to return the embeddings in.

    Can be either `float` or `base64`. Omitted from the request when not set.
    """
