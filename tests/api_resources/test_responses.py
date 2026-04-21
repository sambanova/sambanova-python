# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sambanova import SambaNova, AsyncSambaNova
from tests.utils import assert_matches_type
from sambanova.types import ResponseCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: SambaNova) -> None:
        response = client.responses.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: SambaNova) -> None:
        response = client.responses.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                            "annotations": [
                                {
                                    "end_index": 0,
                                    "start_index": 0,
                                    "type": "url_citation",
                                    "url": "url",
                                    "title": "title",
                                }
                            ],
                            "logprobs": [
                                {
                                    "token": " Hello",
                                    "logprob": -0.00012340000000000002,
                                    "top_logprobs": {
                                        "token": " Hello",
                                        "logprob": -0.00012340000000000002,
                                        "bytes": [32, 72, 101, 108, 108, 111],
                                    },
                                    "bytes": [32, 72, 101, 108, 108, 111],
                                }
                            ],
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
            ],
            model="gpt-oss-120b",
            background=True,
            frequency_penalty=-2,
            instructions="instructions",
            max_output_tokens=1024,
            max_tool_calls=0,
            metadata={"foo": "string"},
            parallel_tool_calls=True,
            presence_penalty=-2,
            previous_response_id="previous_response_id",
            reasoning={"effort": "low"},
            service_tier="service_tier",
            store=True,
            stream=False,
            temperature=0.7,
            text={"format": {"type": "text"}},
            tool_choice={
                "name": "get_weather",
                "type": "function",
            },
            tools=[
                {
                    "name": "get_weather",
                    "type": "function",
                    "description": "Get the current weather for a given location.",
                    "parameters": {
                        "type": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "additionalProperties": "bar",
                    },
                    "strict": None,
                }
            ],
            top_k=5,
            top_logprobs=0,
            top_p=1,
            truncation="auto",
            user="user",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: SambaNova) -> None:
        http_response = client.responses.with_raw_response.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: SambaNova) -> None:
        with client.responses.with_streaming_response.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseCreateResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: SambaNova) -> None:
        response_stream = client.responses.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
            stream=True,
        )
        response_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: SambaNova) -> None:
        response_stream = client.responses.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                            "annotations": [
                                {
                                    "end_index": 0,
                                    "start_index": 0,
                                    "type": "url_citation",
                                    "url": "url",
                                    "title": "title",
                                }
                            ],
                            "logprobs": [
                                {
                                    "token": " Hello",
                                    "logprob": -0.00012340000000000002,
                                    "top_logprobs": {
                                        "token": " Hello",
                                        "logprob": -0.00012340000000000002,
                                        "bytes": [32, 72, 101, 108, 108, 111],
                                    },
                                    "bytes": [32, 72, 101, 108, 108, 111],
                                }
                            ],
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
            ],
            model="gpt-oss-120b",
            stream=True,
            background=True,
            frequency_penalty=-2,
            instructions="instructions",
            max_output_tokens=1024,
            max_tool_calls=0,
            metadata={"foo": "string"},
            parallel_tool_calls=True,
            presence_penalty=-2,
            previous_response_id="previous_response_id",
            reasoning={"effort": "low"},
            service_tier="service_tier",
            store=True,
            temperature=0.7,
            text={"format": {"type": "text"}},
            tool_choice={
                "name": "get_weather",
                "type": "function",
            },
            tools=[
                {
                    "name": "get_weather",
                    "type": "function",
                    "description": "Get the current weather for a given location.",
                    "parameters": {
                        "type": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "additionalProperties": "bar",
                    },
                    "strict": None,
                }
            ],
            top_k=5,
            top_logprobs=0,
            top_p=1,
            truncation="auto",
            user="user",
        )
        response_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: SambaNova) -> None:
        response = client.responses.with_raw_response.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: SambaNova) -> None:
        with client.responses.with_streaming_response.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.responses.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.responses.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                            "annotations": [
                                {
                                    "end_index": 0,
                                    "start_index": 0,
                                    "type": "url_citation",
                                    "url": "url",
                                    "title": "title",
                                }
                            ],
                            "logprobs": [
                                {
                                    "token": " Hello",
                                    "logprob": -0.00012340000000000002,
                                    "top_logprobs": {
                                        "token": " Hello",
                                        "logprob": -0.00012340000000000002,
                                        "bytes": [32, 72, 101, 108, 108, 111],
                                    },
                                    "bytes": [32, 72, 101, 108, 108, 111],
                                }
                            ],
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
            ],
            model="gpt-oss-120b",
            background=True,
            frequency_penalty=-2,
            instructions="instructions",
            max_output_tokens=1024,
            max_tool_calls=0,
            metadata={"foo": "string"},
            parallel_tool_calls=True,
            presence_penalty=-2,
            previous_response_id="previous_response_id",
            reasoning={"effort": "low"},
            service_tier="service_tier",
            store=True,
            stream=False,
            temperature=0.7,
            text={"format": {"type": "text"}},
            tool_choice={
                "name": "get_weather",
                "type": "function",
            },
            tools=[
                {
                    "name": "get_weather",
                    "type": "function",
                    "description": "Get the current weather for a given location.",
                    "parameters": {
                        "type": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "additionalProperties": "bar",
                    },
                    "strict": None,
                }
            ],
            top_k=5,
            top_logprobs=0,
            top_p=1,
            truncation="auto",
            user="user",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        http_response = await async_client.responses.with_raw_response.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        async with async_client.responses.with_streaming_response.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseCreateResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        response_stream = await async_client.responses.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
            stream=True,
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncSambaNova) -> None:
        response_stream = await async_client.responses.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                            "annotations": [
                                {
                                    "end_index": 0,
                                    "start_index": 0,
                                    "type": "url_citation",
                                    "url": "url",
                                    "title": "title",
                                }
                            ],
                            "logprobs": [
                                {
                                    "token": " Hello",
                                    "logprob": -0.00012340000000000002,
                                    "top_logprobs": {
                                        "token": " Hello",
                                        "logprob": -0.00012340000000000002,
                                        "bytes": [32, 72, 101, 108, 108, 111],
                                    },
                                    "bytes": [32, 72, 101, 108, 108, 111],
                                }
                            ],
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                    "id": "id",
                    "status": "in_progress",
                },
            ],
            model="gpt-oss-120b",
            stream=True,
            background=True,
            frequency_penalty=-2,
            instructions="instructions",
            max_output_tokens=1024,
            max_tool_calls=0,
            metadata={"foo": "string"},
            parallel_tool_calls=True,
            presence_penalty=-2,
            previous_response_id="previous_response_id",
            reasoning={"effort": "low"},
            service_tier="service_tier",
            store=True,
            temperature=0.7,
            text={"format": {"type": "text"}},
            tool_choice={
                "name": "get_weather",
                "type": "function",
            },
            tools=[
                {
                    "name": "get_weather",
                    "type": "function",
                    "description": "Get the current weather for a given location.",
                    "parameters": {
                        "type": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "additionalProperties": "bar",
                    },
                    "strict": None,
                }
            ],
            top_k=5,
            top_logprobs=0,
            top_p=1,
            truncation="auto",
            user="user",
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.responses.with_raw_response.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        async with async_client.responses.with_streaming_response.create(
            input=[
                {
                    "content": "What is the weather in San Francisco?",
                    "role": "user",
                    "type": "message",
                },
                {
                    "content": [
                        {
                            "text": "The weather in San Francisco is 65°F and partly cloudy.",
                            "type": "output_text",
                        }
                    ],
                    "role": "assistant",
                    "type": "message",
                },
                {
                    "content": "What should I wear?",
                    "role": "user",
                    "type": "message",
                },
            ],
            model="gpt-oss-120b",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
