from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_project():
    return f"This is einstieg project or should i spell it for you? {str(list('einstieg')).upper()}"
