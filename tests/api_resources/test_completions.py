# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sambanova import SambaNova, AsyncSambaNova
from tests.utils import assert_matches_type
from sambanova.types import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: SambaNova) -> None:
        completion = client.completions.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: SambaNova) -> None:
        completion = client.completions.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
            do_sample=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=2048,
            max_tokens=2048,
            n=1,
            presence_penalty=-2,
            seed=0,
            stop="\n",
            stream=False,
            stream_options={"include_usage": True},
            temperature=0.7,
            top_k=5,
            top_logprobs=0,
            top_p=1,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: SambaNova) -> None:
        response = client.completions.with_raw_response.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: SambaNova) -> None:
        with client.completions.with_streaming_response.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: SambaNova) -> None:
        completion_stream = client.completions.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
            stream=True,
        )
        completion_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: SambaNova) -> None:
        completion_stream = client.completions.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
            stream=True,
            do_sample=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=2048,
            max_tokens=2048,
            n=1,
            presence_penalty=-2,
            seed=0,
            stop="\n",
            stream_options={"include_usage": True},
            temperature=0.7,
            top_k=5,
            top_logprobs=0,
            top_p=1,
        )
        completion_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: SambaNova) -> None:
        response = client.completions.with_raw_response.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: SambaNova) -> None:
        with client.completions.with_streaming_response.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
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
        completion = await async_client.completions.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncSambaNova) -> None:
        completion = await async_client.completions.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
            do_sample=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=2048,
            max_tokens=2048,
            n=1,
            presence_penalty=-2,
            seed=0,
            stop="\n",
            stream=False,
            stream_options={"include_usage": True},
            temperature=0.7,
            top_k=5,
            top_logprobs=0,
            top_p=1,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        completion_stream = await async_client.completions.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
            stream=True,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncSambaNova) -> None:
        completion_stream = await async_client.completions.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
            stream=True,
            do_sample=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=2048,
            max_tokens=2048,
            n=1,
            presence_penalty=-2,
            seed=0,
            stop="\n",
            stream_options={"include_usage": True},
            temperature=0.7,
            top_k=5,
            top_logprobs=0,
            top_p=1,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="string",
            prompt="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\ncreate a poem using palindromes<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
