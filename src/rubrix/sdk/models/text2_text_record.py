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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.task_status import TaskStatus
from ..models.text2_text_annotation import Text2TextAnnotation
from ..models.text2_text_record_metadata import Text2TextRecordMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="Text2TextRecord")


@attr.s(auto_attribs=True)
class Text2TextRecord:
    """The output text2text task record"""

    text: str
    id: Union[Unset, int, str] = UNSET
    metadata: Union[Text2TextRecordMetadata, Unset] = UNSET
    event_timestamp: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, TaskStatus] = UNSET
    prediction: Union[Text2TextAnnotation, Unset] = UNSET
    annotation: Union[Text2TextAnnotation, Unset] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        id: Union[Unset, int, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        event_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.event_timestamp, Unset):
            event_timestamp = self.event_timestamp.isoformat()

        status: Union[Unset, TaskStatus] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        prediction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prediction, Unset):
            prediction = self.prediction.to_dict()

        annotation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotation, Unset):
            annotation = self.annotation.to_dict()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if event_timestamp is not UNSET:
            field_dict["event_timestamp"] = event_timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if prediction is not UNSET:
            field_dict["prediction"] = prediction
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        def _parse_id(data: Any) -> Union[Unset, int, str]:
            data = None if isinstance(data, Unset) else data
            id: Union[Unset, int, str]
            return cast(Union[Unset, int, str], data)

        id = _parse_id(d.pop("id", UNSET))

        metadata: Union[Text2TextRecordMetadata, Unset] = UNSET
        _metadata = d.pop("metadata", UNSET)
        if not isinstance(_metadata, Unset):
            metadata = Text2TextRecordMetadata.from_dict(_metadata)

        event_timestamp: Union[Unset, datetime.datetime] = UNSET
        _event_timestamp = d.pop("event_timestamp", UNSET)
        if not isinstance(_event_timestamp, Unset):
            event_timestamp = isoparse(_event_timestamp)

        status: Union[Unset, TaskStatus] = UNSET
        _status = d.pop("status", UNSET)
        if not isinstance(_status, Unset):
            status = TaskStatus(_status)

        prediction: Union[Text2TextAnnotation, Unset] = UNSET
        _prediction = d.pop("prediction", UNSET)
        if not isinstance(_prediction, Unset):
            prediction = Text2TextAnnotation.from_dict(_prediction)

        annotation: Union[Text2TextAnnotation, Unset] = UNSET
        _annotation = d.pop("annotation", UNSET)
        if not isinstance(_annotation, Unset):
            annotation = Text2TextAnnotation.from_dict(_annotation)

        last_updated: Union[Unset, datetime.datetime] = UNSET
        _last_updated = d.pop("last_updated", UNSET)
        if not isinstance(_last_updated, Unset):
            last_updated = isoparse(_last_updated)

        text2_text_record = cls(
            text=text,
            id=id,
            metadata=metadata,
            event_timestamp=event_timestamp,
            status=status,
            prediction=prediction,
            annotation=annotation,
            last_updated=last_updated,
        )

        text2_text_record.additional_properties = d
        return text2_text_record

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
