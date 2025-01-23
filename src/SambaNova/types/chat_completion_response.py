# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChatCompletionResponse", "Usage"]


class Usage(BaseModel):
    acceptance_rate: Optional[float] = None
    """acceptance rate"""

    completion_tokens: Optional[int] = None
    """number of tokens generated in completion"""

    completion_tokens_after_first_per_sec: Optional[float] = None
    """completion tokens per second after first token generation"""

    completion_tokens_after_first_per_sec_first_ten: Optional[float] = None
    """completion tokens per second after first token generation first ten"""

    completion_tokens_per_sec: Optional[float] = None
    """completion tokens per second"""

    end_time: Optional[float] = None
    """The Unix timestamp (in seconds) of when the generation finished."""

    is_last_response: Optional[Literal[True]] = None
    """whether or not is last response, always true for non streaming response"""

    prompt_tokens: Optional[int] = None
    """number of tokens used in the prompt sent"""

    start_time: Optional[float] = None
    """The Unix timestamp (in seconds) of when the generation started."""

    time_to_first_token: Optional[float] = None
    """also TTF, time (in seconds) taken to generate the first token"""

    total_latency: Optional[int] = None
    """total time (in seconds) taken to generate the full generation"""

    total_tokens: Optional[int] = None
    """prompt tokens + completion tokens"""

    total_tokens_per_sec: Optional[float] = None
    """tokens per second including prompt and completion"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponse(BaseModel):
    id: str
    """A unique identifier for the chat completion."""

    choices: List[object]

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created."""

    model: str
    """The model used for the chat completion."""

    object: Literal["chat.completion"]
    """The object type, always `chat.completion`."""

    system_fingerprint: str
    """Backend configuration that the model runs with."""

    usage: Optional[Usage] = None
    """Usage metrics for the completion request"""
