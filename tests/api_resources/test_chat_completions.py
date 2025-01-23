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
    def test_method_create(self, client: Sambanova) -> None:
        chat_completion = client.chat_completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
        )
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Sambanova) -> None:
        chat_completion = client.chat_completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
            frequency_penalty=-2,
            logit_bias={},
            logprobs=True,
            max_completion_tokens=2048,
            max_tokens=2048,
            n=1,
            parallel_tool_calls=True,
            presence_penalty=-2,
            response_format={"type": "json_object"},
            seed=0,
            stop="\n",
            stream=True,
            stream_options={"include_usage": True},
            temperature=0.7,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "type",
                }
            ],
            top_k=5,
            top_logprobs=0,
            top_p=1,
        )
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Sambanova) -> None:
        response = client.chat_completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = response.parse()
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Sambanova) -> None:
        with client.chat_completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = response.parse()
            assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChatCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSambanova) -> None:
        chat_completion = await async_client.chat_completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
        )
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSambanova) -> None:
        chat_completion = await async_client.chat_completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
            frequency_penalty=-2,
            logit_bias={},
            logprobs=True,
            max_completion_tokens=2048,
            max_tokens=2048,
            n=1,
            parallel_tool_calls=True,
            presence_penalty=-2,
            response_format={"type": "json_object"},
            seed=0,
            stop="\n",
            stream=True,
            stream_options={"include_usage": True},
            temperature=0.7,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "type",
                }
            ],
            top_k=5,
            top_logprobs=0,
            top_p=1,
        )
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSambanova) -> None:
        response = await async_client.chat_completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = await response.parse()
        assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSambanova) -> None:
        async with async_client.chat_completions.with_streaming_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = await response.parse()
            assert_matches_type(ChatCompletionCreateResponse, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True
