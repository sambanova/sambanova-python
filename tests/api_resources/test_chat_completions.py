# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sambanova import Sambanova, AsyncSambanova
from tests.utils import assert_matches_type
from sambanova.types import ChatCompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChatCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Sambanova) -> None:
        chat_completion = client.chat_completions.create()
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Sambanova) -> None:
        chat_completion = client.chat_completions.create(
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
            stream=False,
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
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Sambanova) -> None:
        response = client.chat_completions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = response.parse()
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Sambanova) -> None:
        with client.chat_completions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = response.parse()
            assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Sambanova) -> None:
        chat_completion_stream = client.chat_completions.create(
            stream=True,
        )
        chat_completion_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Sambanova) -> None:
        chat_completion_stream = client.chat_completions.create(
            stream=True,
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
        chat_completion_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: Sambanova) -> None:
        response = client.chat_completions.with_raw_response.create(
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Sambanova) -> None:
        with client.chat_completions.with_streaming_response.create(
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncChatCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncSambanova) -> None:
        chat_completion = await async_client.chat_completions.create()
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncSambanova) -> None:
        chat_completion = await async_client.chat_completions.create(
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
            stream=False,
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
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncSambanova) -> None:
        response = await async_client.chat_completions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = await response.parse()
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncSambanova) -> None:
        async with async_client.chat_completions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = await response.parse()
            assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncSambanova) -> None:
        chat_completion_stream = await async_client.chat_completions.create(
            stream=True,
        )
        await chat_completion_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncSambanova) -> None:
        chat_completion_stream = await async_client.chat_completions.create(
            stream=True,
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
        await chat_completion_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncSambanova) -> None:
        response = await async_client.chat_completions.with_raw_response.create(
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncSambanova) -> None:
        async with async_client.chat_completions.with_streaming_response.create(
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
