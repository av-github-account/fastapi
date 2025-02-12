from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# print(settings.database_username)
# # подключение библиотеки bcrypt и if ... необходим для исключения ошибки
# #  File "/Users/av/Dropbox/__CODE/av_01/.venv/lib/python3.13/site-packages/passlib/handlers/bcrypt.py", line 620, in _load_backend_mixin
# #    version = _bcrypt.__about__.__version__
# #              ^^^^^^^^^^^^^^^^^
# # AttributeError: module 'bcrypt' has no attribute '__about__'
# import bcrypt

# if not hasattr(bcrypt, "__about__"):
#     bcrypt.__about__ = type("about", (object,), {"__version__": bcrypt.__version__})


# models.Base.metadata.create_all(bind=engine)

origins = ["https://www.google.com"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello world!"}
