from fastapi import FastAPI

from .dependencies import authenticated_user_dependency

from .routers import locations

from .routers import users


app = FastAPI(dependencies=[authenticated_user_dependency])

app.include_router(users.router)
app.include_router(locations.router)


@app.get("/")
def root():
    return "Hello from Einstieg!"
