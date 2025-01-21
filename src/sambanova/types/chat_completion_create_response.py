# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChatCompletionCreateResponse", "Choice", "ChoiceMessage", "Usage"]


class ChoiceMessage(BaseModel):
    content: Optional[str] = None

    role: Optional[str] = None


class Choice(BaseModel):
    finish_reason: Optional[str] = None

    index: Optional[int] = None

    message: Optional[ChoiceMessage] = None


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    completion_tokens_after_first_per_sec: Optional[float] = None

    prompt_tokens: Optional[int] = None

    time_to_first_token: Optional[float] = None

    total_latency: Optional[float] = None

    total_tokens: Optional[int] = None


class ChatCompletionCreateResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    model: Optional[str] = None

    object: Optional[Literal["chat.completion"]] = None

    usage: Optional[Usage] = None
