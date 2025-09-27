# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelResponse", "Pricing"]


class Pricing(BaseModel):
    completion: Optional[float] = None
    """price per completion token in USD"""

    duration_per_hour: Optional[float] = None
    """price per input hour"""

    prompt: Optional[float] = None
    """price per prompt token in USD"""

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


class ModelResponse(BaseModel):
    id: str
    """model id"""

    context_length: Optional[int] = None
    """model context length"""

    max_completion_tokens: Optional[int] = None
    """model max completion tokens"""

    object: Optional[Literal["model"]] = None
    """type"""

    owned_by: Optional[str] = None
    """model owner"""

    pricing: Optional[Pricing] = None
    """pricing details"""

    sn_metadata: Optional[builtins.object] = None
    """additional sn metadata"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]
