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

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.creation_text2_text_record import CreationText2TextRecord
from ..models.text2_text_bulk_data_metadata import Text2TextBulkDataMetadata
from ..models.text2_text_bulk_data_tags import Text2TextBulkDataTags
from ..types import UNSET, Unset

T = TypeVar("T", bound="Text2TextBulkData")


@attr.s(auto_attribs=True)
class Text2TextBulkData:
    """API bulk data for text2text

    Attributes:
    -----------

    records: List[CreationText2TextRecord]
        The text2text record list"""

    records: List[CreationText2TextRecord]
    tags: Union[Text2TextBulkDataTags, Unset] = UNSET
    metadata: Union[Text2TextBulkDataMetadata, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()

            records.append(records_item)

        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "records": records,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = CreationText2TextRecord.from_dict(records_item_data)

            records.append(records_item)

        tags: Union[Text2TextBulkDataTags, Unset] = UNSET
        _tags = d.pop("tags", UNSET)
        if not isinstance(_tags, Unset):
            tags = Text2TextBulkDataTags.from_dict(_tags)

        metadata: Union[Text2TextBulkDataMetadata, Unset] = UNSET
        _metadata = d.pop("metadata", UNSET)
        if not isinstance(_metadata, Unset):
            metadata = Text2TextBulkDataMetadata.from_dict(_metadata)

        text2_text_bulk_data = cls(
            records=records,
            tags=tags,
            metadata=metadata,
        )

        text2_text_bulk_data.additional_properties = d
        return text2_text_bulk_data

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
