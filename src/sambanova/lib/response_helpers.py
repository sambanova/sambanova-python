# This directory is not modified by the Stainless generator.
# Place SDK extensions and convenience helpers here.
#
# This module patches generated response models with convenience properties
# for OpenAI SDK compatibility. It is imported automatically at package load
# time via `src/sambanova/__init__.py`, so no explicit import is needed —
# the properties are available on the model instances as soon as `sambanova`
# is imported.
#
# To add further helpers, define a @property function below and assign it to
# the target model class in the same way as `output_text`.

from typing import List

from ..types.response_response import (
    ResponseResponse,
    OutputResponseMessageContentContentPartArrayResponseTextContent,
)

__all__ = ["ResponseResponse"]


@property  # type: ignore[misc]
def _output_text(self: ResponseResponse) -> str:
    """Aggregates all output_text content parts from the response output array.

    Iterates over every output item, filters to `type == "message"` items,
    then collects the `text` from every content part whose `type` is
    `"output_text"`. Parts are joined in order with no separator.

    Returns an empty string if the response contains no output_text parts
    (e.g. the model only produced a function call or a reasoning item).

    Mirrors the `output_text` property on the OpenAI Python SDK's `Response`
    class for drop-in compatibility.
    """
    texts: List[str] = []
    for output in self.output:
        if output.type == "message":
            content = output.content
            if isinstance(content, list):
                for part in content:
                    if (
                        isinstance(part, OutputResponseMessageContentContentPartArrayResponseTextContent)
                        and part.type == "output_text"
                    ):
                        texts.append(part.text)
    return "".join(texts)


ResponseResponse.output_text = _output_text  # type: ignore[attr-defined]
