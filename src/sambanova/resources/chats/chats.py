# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .completions import (
    CompletionsResource,
    AsyncCompletionsResource,
    CompletionsResourceWithRawResponse,
    AsyncCompletionsResourceWithRawResponse,
    CompletionsResourceWithStreamingResponse,
    AsyncCompletionsResourceWithStreamingResponse,
)

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    @cached_property
    def completions(self) -> CompletionsResource:
        return CompletionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return ChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sambanova-python#with_streaming_response
        """
        return ChatsResourceWithStreamingResponse(self)


class AsyncChatsResource(AsyncAPIResource):
    @cached_property
    def completions(self) -> AsyncCompletionsResource:
        return AsyncCompletionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sambanova-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sambanova-python#with_streaming_response
        """
        return AsyncChatsResourceWithStreamingResponse(self)


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

    @cached_property
    def completions(self) -> CompletionsResourceWithRawResponse:
        return CompletionsResourceWithRawResponse(self._chats.completions)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithRawResponse:
        return AsyncCompletionsResourceWithRawResponse(self._chats.completions)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

    @cached_property
    def completions(self) -> CompletionsResourceWithStreamingResponse:
        return CompletionsResourceWithStreamingResponse(self._chats.completions)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

    @cached_property
    def completions(self) -> AsyncCompletionsResourceWithStreamingResponse:
        return AsyncCompletionsResourceWithStreamingResponse(self._chats.completions)
