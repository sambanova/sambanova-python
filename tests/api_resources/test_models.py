# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sambanova import SambaNova, AsyncSambaNova
from tests.utils import assert_matches_type
from sambanova.types import ModelResponse, ModelsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SambaNova) -> None:
        model = client.models.retrieve(
            "model_id",
        )
        assert_matches_type(ModelResponse, model, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SambaNova) -> None:
        response = client.models.with_raw_response.retrieve(
            "model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SambaNova) -> None:
        with client.models.with_streaming_response.retrieve(
            "model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SambaNova) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_id` but received ''"):
            client.models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: SambaNova) -> None:
        model = client.models.list()
        assert_matches_type(ModelsResponse, model, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SambaNova) -> None:
        response = client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelsResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SambaNova) -> None:
        with client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSambaNova) -> None:
        model = await async_client.models.retrieve(
            "model_id",
        )
        assert_matches_type(ModelResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.models.with_raw_response.retrieve(
            "model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSambaNova) -> None:
        async with async_client.models.with_streaming_response.retrieve(
            "model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSambaNova) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_id` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSambaNova) -> None:
        model = await async_client.models.list()
        assert_matches_type(ModelsResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelsResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSambaNova) -> None:
        async with async_client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelsResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True
