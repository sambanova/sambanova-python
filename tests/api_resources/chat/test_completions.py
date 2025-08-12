# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sambanova import SambaNova, AsyncSambaNova
from tests.utils import assert_matches_type
from sambanova.types.chat import ChatCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: SambaNova) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        )
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: SambaNova) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            max_tokens=0,
            response_format={
                "type": "json_object",
                "json_schema": {"foo": "bar"},
            },
            stop="string",
            stream=False,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="auto",
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {
                        "properties": {"foo": "bar"},
                        "type": "object",
                        "required": ["string"],
                    },
                }
            ],
            top_k=0,
            top_p=0,
        )
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: SambaNova) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: SambaNova) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(ChatCompletionResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: SambaNova) -> None:
        completion_stream = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        )
        completion_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: SambaNova) -> None:
        completion_stream = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
            max_tokens=0,
            response_format={
                "type": "json_object",
                "json_schema": {"foo": "bar"},
            },
            stop="string",
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="auto",
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {
                        "properties": {"foo": "bar"},
                        "type": "object",
                        "required": ["string"],
                    },
                }
            ],
            top_k=0,
            top_p=0,
        )
        completion_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: SambaNova) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: SambaNova) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        )
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncSambaNova) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            max_tokens=0,
            response_format={
                "type": "json_object",
                "json_schema": {"foo": "bar"},
            },
            stop="string",
            stream=False,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="auto",
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {
                        "properties": {"foo": "bar"},
                        "type": "object",
                        "required": ["string"],
                    },
                }
            ],
            top_k=0,
            top_p=0,
        )
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(ChatCompletionResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        completion_stream = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncSambaNova) -> None:
        completion_stream = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
            max_tokens=0,
            response_format={
                "type": "json_object",
                "json_schema": {"foo": "bar"},
            },
            stop="string",
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="auto",
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {
                        "properties": {"foo": "bar"},
                        "type": "object",
                        "required": ["string"],
                    },
                }
            ],
            top_k=0,
            top_p=0,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
