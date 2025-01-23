# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GeneralError", "Error"]


class Error(BaseModel):
    code: Optional[str] = None
    """error code"""

    message: Optional[str] = None
    """error message"""

    param: Optional[str] = None
    """error params"""

    type: Optional[str] = None
    """error type"""


class GeneralError(BaseModel):
    error: Error
