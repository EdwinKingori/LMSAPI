from fastapi import FastAPI   # type: ignore
from .lms_routers import users, sections, courses


app = FastAPI()

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)


@app.get("/")
async def root():
    return {"message": "Welcome back buddy!"}
