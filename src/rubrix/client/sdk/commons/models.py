#  coding=utf-8
#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from datetime import datetime
from enum import Enum
from typing import Any, MutableMapping, List
from typing import Dict
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union
from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field
from pydantic.generics import GenericModel


class TaskStatus(str, Enum):
    default = "Default"
    edited = "Edited"
    discarded = "Discarded"
    validated = "Validated"


class BaseAnnotation(BaseModel):
    agent: str


T = TypeVar("T", bound=BaseAnnotation)


class BaseRecord(GenericModel, Generic[T]):
    id: Optional[Union[int, str]] = Field(default_factory=lambda: str(uuid4()))
    metadata: Dict[str, Any] = Field(default=None)
    event_timestamp: Optional[datetime] = None
    status: Optional[TaskStatus] = None
    prediction: Optional[T] = None
    annotation: Optional[T] = None


class UpdateDatasetRequest(BaseModel):
    tags: Dict[str, str] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PredictionStatus(str, Enum):
    OK = "ok"
    KO = "ko"


class ScoreRange(BaseModel):
    range_from: float = Field(default=0.0, alias="from")
    range_to: float = Field(default=None, alias="to")


R = TypeVar("R")


class Response(GenericModel, Generic[T]):
    status_code: int
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[R]


class BulkResponse(BaseModel):
    dataset: str
    processed: int
    failed: int = 0


class ErrorMessage(BaseModel):
    detail: str


class ValidationError(BaseModel):
    loc: List[str]
    msg: str
    type: str


class HTTPValidationError(BaseModel):
    detail: List[ValidationError]
