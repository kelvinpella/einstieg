from typing import Callable, Awaitable

from fastapi.requests import Request
from fastapi.responses import JSONResponse


class EinstiegAPIError(Exception):
    """Base exception for Einstieg API errors."""

    def __init__(self, name: str = "Einstieg", message: str = "Service unavailable"):
        self.name = name
        self.message = message
        super().__init__(self.name, self.message)


class InvalidToken(EinstiegAPIError):
    """
    Exception raised when an invalid authentication token is encountered.
    """

    ...


class InternalServerError(EinstiegAPIError):
    """Exception raised for internal server errors."""

    ...


class PydanticRequestValidationError(EinstiegAPIError):
    """
    Exception raised for request validation errors caused by invalid Pydantic model data.
    """

    ...


def create_exception_handler(
    status_code: int, initial_detail: str
) -> Callable[[Request, Exception], Awaitable[JSONResponse]]:
    async def exception_handler(_: Request, exc: Exception) -> JSONResponse:
        message = initial_detail
        if isinstance(exc, EinstiegAPIError):
            if getattr(exc, "message", None):
                message = exc.message  # type: ignore[assignment]
            if getattr(exc, "name", None):
                message = f"{message} [{exc.name}]"
        else:
            extra = str(exc).strip()
            if extra:
                message = f"{message} [{extra}]"

        return JSONResponse(status_code=status_code, content={"detail": message})

    return exception_handler
