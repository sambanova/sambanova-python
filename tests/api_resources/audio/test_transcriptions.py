# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sambanova import SambaNova, AsyncSambaNova
from tests.utils import assert_matches_type
from sambanova.types.audio import TranscriptionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: SambaNova) -> None:
        transcription = client.audio.transcriptions.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: SambaNova) -> None:
        transcription = client.audio.transcriptions.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            language="es",
            prompt="Please transcribe carefully, including pauses and hesitations.",
            response_format="json",
            stream=False,
            stream_options={"include_usage": True},
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: SambaNova) -> None:
        response = client.audio.transcriptions.with_raw_response.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: SambaNova) -> None:
        with client.audio.transcriptions.with_streaming_response.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = response.parse()
            assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: SambaNova) -> None:
        transcription_stream = client.audio.transcriptions.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            stream=True,
        )
        transcription_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: SambaNova) -> None:
        transcription_stream = client.audio.transcriptions.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            stream=True,
            language="es",
            prompt="Please transcribe carefully, including pauses and hesitations.",
            response_format="json",
            stream_options={"include_usage": True},
        )
        transcription_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: SambaNova) -> None:
        response = client.audio.transcriptions.with_raw_response.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: SambaNova) -> None:
        with client.audio.transcriptions.with_streaming_response.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncTranscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        transcription = await async_client.audio.transcriptions.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncSambaNova) -> None:
        transcription = await async_client.audio.transcriptions.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            language="es",
            prompt="Please transcribe carefully, including pauses and hesitations.",
            response_format="json",
            stream=False,
            stream_options={"include_usage": True},
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.audio.transcriptions.with_raw_response.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = await response.parse()
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncSambaNova) -> None:
        async with async_client.audio.transcriptions.with_streaming_response.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = await response.parse()
            assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        transcription_stream = await async_client.audio.transcriptions.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            stream=True,
        )
        await transcription_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncSambaNova) -> None:
        transcription_stream = await async_client.audio.transcriptions.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            stream=True,
            language="es",
            prompt="Please transcribe carefully, including pauses and hesitations.",
            response_format="json",
            stream_options={"include_usage": True},
        )
        await transcription_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        response = await async_client.audio.transcriptions.with_raw_response.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncSambaNova) -> None:
        async with async_client.audio.transcriptions.with_streaming_response.create(
            file=b"raw file contents",
            model="Whisper-Large-v3",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
