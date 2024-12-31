from typing import TypedDict, Union
from enum import Enum


class ResponseType(Enum):
    ERROR = 'ERROR'
    SUCCESS = "SUCCESS"


class SuccessResponse(TypedDict):
    status: ResponseType
    data: object


class ErrorResponse(TypedDict):
    status: ResponseType
    message: str


Response = Union[SuccessResponse, ErrorResponse]
