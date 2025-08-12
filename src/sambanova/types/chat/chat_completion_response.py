# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ChatCompletionResponse",
    "Choice",
    "ChoiceMessage",
    "ChoiceMessageContentUnionMember1",
    "ChoiceMessageContentUnionMember1ImageURL",
    "Usage",
]


class ChoiceMessageContentUnionMember1ImageURL(BaseModel):
    url: str
    """Data URI string like data:<format>;base64,<data>."""


class ChoiceMessageContentUnionMember1(BaseModel):
    type: Literal["text", "image_url"]
    """Kind of message part."""

    image_url: Optional[ChoiceMessageContentUnionMember1ImageURL] = None
    """Image content when type is image_url."""

    text: Optional[str] = None
    """Text content when type is text."""


class ChoiceMessage(BaseModel):
    content: Union[str, List[ChoiceMessageContentUnionMember1]]

    role: Literal["system", "user", "assistant"]


class Choice(BaseModel):
    finish_reason: str

    index: int

    logprobs: Optional[Dict[str, object]] = None

    message: Optional[ChoiceMessage] = None


class Usage(BaseModel):
    input_tokens_count: Optional[int] = None

    api_model_execution_time: Optional[float] = FieldInfo(alias="model_execution_time", default=None)

    output_tokens_count: Optional[int] = None

    queue_time: Optional[float] = None

    throughput_after_first_token: Optional[float] = None

    time_to_first_token: Optional[float] = None

    total_tokens_count: Optional[int] = None


class ChatCompletionResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    model: Optional[str] = None

    object: Optional[str] = None

    usage: Optional[Usage] = None
