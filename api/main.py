from fastapi import FastAPI, status

from .errors import (
    InternalServerError,
    InvalidToken,
    PydanticRequestValidationError,
    create_exception_handler,
)

from .dependencies import authenticated_user_dependency

from .routers import locations

from .routers import users


app = FastAPI(dependencies=[authenticated_user_dependency])

app.include_router(users.router)
app.include_router(locations.router)


@app.get("/")
def root():
    return "Hello from Einstieg!"


app.add_exception_handler(
    InvalidToken,
    create_exception_handler(
        status_code=status.HTTP_401_UNAUTHORIZED, initial_detail="Invalid token"
    ),
)
app.add_exception_handler(
    InternalServerError,
    create_exception_handler(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        initial_detail="Internal Server Error",
    ),
)
app.add_exception_handler(
    PydanticRequestValidationError,
    create_exception_handler(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        initial_detail="Request validation error",
    ),
)
