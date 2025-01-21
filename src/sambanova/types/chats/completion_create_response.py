# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CompletionCreateResponse", "Choice", "ChoiceMessage", "Usage"]


class ChoiceMessage(BaseModel):
    content: Optional[str] = None

    role: Optional[str] = None


class Choice(BaseModel):
    finish_reason: Optional[str] = None

    index: Optional[int] = None

    message: Optional[ChoiceMessage] = None


class Usage(BaseModel):
    input_tokens_count: Optional[int] = None

    api_model_execution_time: Optional[float] = FieldInfo(alias="model_execution_time", default=None)

    output_tokens_count: Optional[int] = None

    throughput_after_first_token: Optional[float] = None

    time_to_first_token: Optional[float] = None

    total_tokens_count: Optional[int] = None


class CompletionCreateResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    model: Optional[str] = None

    object: Optional[Literal["chat.completion"]] = None

    usage: Optional[Usage] = None
