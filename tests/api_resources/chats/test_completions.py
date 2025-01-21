# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sambanova import Sambanova, AsyncSambanova
from tests.utils import assert_matches_type
from sambanova.types.chats import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Sambanova) -> None:
        completion = client.chats.completions.create()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Sambanova) -> None:
        completion = client.chats.completions.create(
            max_tokens=0,
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            response_format={"type": "json_object"},
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="string",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {
                            "properties": {},
                            "type": "type",
                        },
                    },
                    "type": "function",
                }
            ],
            top_k=1,
            top_p=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Sambanova) -> None:
        response = client.chats.completions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Sambanova) -> None:
        with client.chats.completions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSambanova) -> None:
        completion = await async_client.chats.completions.create()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSambanova) -> None:
        completion = await async_client.chats.completions.create(
            max_tokens=0,
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            response_format={"type": "json_object"},
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="string",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {
                            "properties": {},
                            "type": "type",
                        },
                    },
                    "type": "function",
                }
            ],
            top_k=1,
            top_p=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSambanova) -> None:
        response = await async_client.chats.completions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSambanova) -> None:
        async with async_client.chats.completions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
