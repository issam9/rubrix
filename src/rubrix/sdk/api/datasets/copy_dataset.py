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

from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.copy_dataset_request import CopyDatasetRequest
from ...models.dataset import Dataset
from ...models.error_message import ErrorMessage
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    name: str,
    json_body: CopyDatasetRequest,
    team: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/datasets/{name}:copy".format(client.base_url, name=name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "team": team,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Dataset, ErrorMessage, ErrorMessage, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = Dataset.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ErrorMessage.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ErrorMessage.from_dict(response.json())

        return response_500
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Dataset, ErrorMessage, ErrorMessage, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str,
    json_body: CopyDatasetRequest,
    team: Union[Unset, str] = UNSET,
) -> Response[Union[Dataset, ErrorMessage, ErrorMessage, HTTPValidationError]]:
    kwargs = _get_kwargs(
        client=client,
        name=name,
        json_body=json_body,
        team=team,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: str,
    json_body: CopyDatasetRequest,
    team: Union[Unset, str] = UNSET,
) -> Optional[Union[Dataset, ErrorMessage, ErrorMessage, HTTPValidationError]]:
    """Creates a dataset copy and its tags/metadata info

    Parameters
    ----------
    name:
        The dataset name
    copy_request:
        The copy request data
    ds_params:
        Common dataset query params
    service:
        The datasets service
    current_user:
        The current user"""

    return sync_detailed(
        client=client,
        name=name,
        json_body=json_body,
        team=team,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str,
    json_body: CopyDatasetRequest,
    team: Union[Unset, str] = UNSET,
) -> Response[Union[Dataset, ErrorMessage, ErrorMessage, HTTPValidationError]]:
    kwargs = _get_kwargs(
        client=client,
        name=name,
        json_body=json_body,
        team=team,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str,
    json_body: CopyDatasetRequest,
    team: Union[Unset, str] = UNSET,
) -> Optional[Union[Dataset, ErrorMessage, ErrorMessage, HTTPValidationError]]:
    """Creates a dataset copy and its tags/metadata info

    Parameters
    ----------
    name:
        The dataset name
    copy_request:
        The copy request data
    ds_params:
        Common dataset query params
    service:
        The datasets service
    current_user:
        The current user"""

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            json_body=json_body,
            team=team,
        )
    ).parsed
