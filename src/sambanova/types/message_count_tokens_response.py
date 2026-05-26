# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MessageCountTokensResponse"]


class MessageCountTokensResponse(BaseModel):
    """Token count for the supplied prompt."""

    input_tokens: int
    """Total tokens in the prompt (system + messages + tools)."""
