# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sambanova import SambaNova, AsyncSambaNova
from tests.utils import assert_matches_type
from sambanova.types import (
    MessageCreateResponse,
    MessageCountTokensResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: SambaNova) -> None:
        message = client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: SambaNova) -> None:
        message = client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            container="container",
            metadata={"user_id": "user_id"},
            service_tier="auto",
            stop_sequences=["string"],
            stream=False,
            system="string",
            temperature=1,
            thinking={"type": "disabled"},
            tool_choice={
                "type": "auto",
                "disable_parallel_tool_use": True,
            },
            tools=[
                {
                    "name": "name",
                    "allowed_callers": ["string"],
                    "cache_control": {
                        "type": "ephemeral",
                        "ttl": "ttl",
                    },
                    "defer_loading": True,
                    "description": "description",
                    "eager_input_streaming": True,
                    "input_examples": [{"foo": "bar"}],
                    "input_schema": {"foo": "bar"},
                    "strict": True,
                    "type": "custom",
                }
            ],
            top_k=0,
            top_p=0,
            anthropic_version="2023-06-01",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: SambaNova) -> None:
        response = client.messages.with_raw_response.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: SambaNova) -> None:
        with client.messages.with_streaming_response.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: SambaNova) -> None:
        message_stream = client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            stream=True,
        )
        message_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: SambaNova) -> None:
        message_stream = client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            stream=True,
            container="container",
            metadata={"user_id": "user_id"},
            service_tier="auto",
            stop_sequences=["string"],
            system="string",
            temperature=1,
            thinking={"type": "disabled"},
            tool_choice={
                "type": "auto",
                "disable_parallel_tool_use": True,
            },
            tools=[
                {
                    "name": "name",
                    "allowed_callers": ["string"],
                    "cache_control": {
                        "type": "ephemeral",
                        "ttl": "ttl",
                    },
                    "defer_loading": True,
                    "description": "description",
                    "eager_input_streaming": True,
                    "input_examples": [{"foo": "bar"}],
                    "input_schema": {"foo": "bar"},
                    "strict": True,
                    "type": "custom",
                }
            ],
            top_k=0,
            top_p=0,
            anthropic_version="2023-06-01",
        )
        message_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: SambaNova) -> None:
        response = client.messages.with_raw_response.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: SambaNova) -> None:
        with client.messages.with_streaming_response.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_count_tokens(self, client: SambaNova) -> None:
        message = client.messages.count_tokens(
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        )
        assert_matches_type(MessageCountTokensResponse, message, path=["response"])

    @parametrize
    def test_method_count_tokens_with_all_params(self, client: SambaNova) -> None:
        message = client.messages.count_tokens(
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            system="string",
            thinking={"type": "disabled"},
            tool_choice={
                "type": "auto",
                "disable_parallel_tool_use": True,
            },
            tools=[
                {
                    "name": "name",
                    "allowed_callers": ["string"],
                    "cache_control": {
                        "type": "ephemeral",
                        "ttl": "ttl",
                    },
                    "defer_loading": True,
                    "description": "description",
                    "eager_input_streaming": True,
                    "input_examples": [{"foo": "bar"}],
                    "input_schema": {"foo": "bar"},
                    "strict": True,
                    "type": "custom",
                }
            ],
            anthropic_version="2023-06-01",
        )
        assert_matches_type(MessageCountTokensResponse, message, path=["response"])

    @parametrize
    def test_raw_response_count_tokens(self, client: SambaNova) -> None:
        response = client.messages.with_raw_response.count_tokens(
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCountTokensResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_count_tokens(self, client: SambaNova) -> None:
        with client.messages.with_streaming_response.count_tokens(
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCountTokensResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        message = await async_client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncSambaNova) -> None:
        message = await async_client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            container="container",
            metadata={"user_id": "user_id"},
            service_tier="auto",
            stop_sequences=["string"],
            stream=False,
            system="string",
            temperature=1,
            thinking={"type": "disabled"},
            tool_choice={
                "type": "auto",
                "disable_parallel_tool_use": True,
            },
            tools=[
                {
                    "name": "name",
                    "allowed_callers": ["string"],
                    "cache_control": {
                        "type": "ephemeral",
                        "ttl": "ttl",
                    },
                    "defer_loading": True,
                    "description": "description",
                    "eager_input_streaming": True,
                    "input_examples": [{"foo": "bar"}],
                    "input_schema": {"foo": "bar"},
                    "strict": True,
                    "type": "custom",
                }
            ],
            top_k=0,
            top_p=0,
            anthropic_version="2023-06-01",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.messages.with_raw_response.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        async with async_client.messages.with_streaming_response.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        message_stream = await async_client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            stream=True,
        )
        await message_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncSambaNova) -> None:
        message_stream = await async_client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            stream=True,
            container="container",
            metadata={"user_id": "user_id"},
            service_tier="auto",
            stop_sequences=["string"],
            system="string",
            temperature=1,
            thinking={"type": "disabled"},
            tool_choice={
                "type": "auto",
                "disable_parallel_tool_use": True,
            },
            tools=[
                {
                    "name": "name",
                    "allowed_callers": ["string"],
                    "cache_control": {
                        "type": "ephemeral",
                        "ttl": "ttl",
                    },
                    "defer_loading": True,
                    "description": "description",
                    "eager_input_streaming": True,
                    "input_examples": [{"foo": "bar"}],
                    "input_schema": {"foo": "bar"},
                    "strict": True,
                    "type": "custom",
                }
            ],
            top_k=0,
            top_p=0,
            anthropic_version="2023-06-01",
        )
        await message_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.messages.with_raw_response.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        async with async_client.messages.with_streaming_response.create(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_count_tokens(self, async_client: AsyncSambaNova) -> None:
        message = await async_client.messages.count_tokens(
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        )
        assert_matches_type(MessageCountTokensResponse, message, path=["response"])

    @parametrize
    async def test_method_count_tokens_with_all_params(self, async_client: AsyncSambaNova) -> None:
        message = await async_client.messages.count_tokens(
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
            system="string",
            thinking={"type": "disabled"},
            tool_choice={
                "type": "auto",
                "disable_parallel_tool_use": True,
            },
            tools=[
                {
                    "name": "name",
                    "allowed_callers": ["string"],
                    "cache_control": {
                        "type": "ephemeral",
                        "ttl": "ttl",
                    },
                    "defer_loading": True,
                    "description": "description",
                    "eager_input_streaming": True,
                    "input_examples": [{"foo": "bar"}],
                    "input_schema": {"foo": "bar"},
                    "strict": True,
                    "type": "custom",
                }
            ],
            anthropic_version="2023-06-01",
        )
        assert_matches_type(MessageCountTokensResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_count_tokens(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.messages.with_raw_response.count_tokens(
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCountTokensResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_count_tokens(self, async_client: AsyncSambaNova) -> None:
        async with async_client.messages.with_streaming_response.count_tokens(
            messages=[
                {
                    "content": "Hello, Claude!",
                    "role": "user",
                }
            ],
            model="DeepSeek-V3.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCountTokensResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True
