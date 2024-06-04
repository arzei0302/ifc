# from fastapi import FastAPI, Depends, HTTPException, Request
# from fastapi.responses import JSONResponse
# from sqlalchemy.ext.asyncio import AsyncSession
# from typing import List
# from starlette.middleware.sessions import SessionMiddleware
# from babel.support import Translations, NullTranslations
# import os
# import logging

# from app import crud, models, schemas
# from app.database import engine, get_db

# # Настройка логирования
# logging.basicConfig(level=logging.INFO)

# app = FastAPI()

# # Путь к файлам перевода
# LOCALE_DIR = os.path.join(os.path.dirname(__file__), '../locale')
# logging.info(f"LOCALE_DIR: {LOCALE_DIR}")

# # Функция для выбора локали
# def get_locale(request: Request):
#     lang_header = request.headers.get('Accept-Language', 'ru')
#     logging.info(f"Received Accept-Language header: {lang_header}")
#     lang = lang_header.split(',')[0] if lang_header else 'ru'
#     logging.info(f"Selected language: {lang}")
#     return lang

# # Middleware для сессий (необходимо для сохранения языка)
# app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# @app.middleware("http")
# async def add_translation(request: Request, call_next):
#     logging.info(f"Request headers: {request.headers}")
#     lang = get_locale(request)
#     logging.info(f"Using language: {lang}")

#     translations = None

#     try:
#         translations = Translations.load(LOCALE_DIR, [lang])
#         logging.info(f"Translations loaded for language: {lang}")
#     except Exception as e:
#         logging.error(f"Error loading translations for language {lang}: {e}")

#     # Fallback to general language if specific language translation is not available
#     if not translations or isinstance(translations, NullTranslations):
#         try:
#             general_lang = lang.split('-')[0]
#             if general_lang != lang:  # Проверка, чтобы не fallback на тот же язык
#                 translations = Translations.load(LOCALE_DIR, [general_lang])
#                 logging.info(f"Fallback to general language translations: {general_lang}")
#         except Exception as e:
#             logging.error(f"Error loading general language translations for {general_lang}: {e}")

#     # Fallback to Russian translations if no translation is available
#     if not translations or isinstance(translations, NullTranslations):
#         translations = Translations.load(LOCALE_DIR, ['ru'])
#         logging.info("Fallback to Russian translations")

#     logging.info(f"Translations object: {translations}")
#     request.state.translations = translations
#     response = await call_next(request)
#     return response

# @app.get("/")
# async def read_root(request: Request):
#     logging.info(f"Headers: {request.headers}")
#     _ = request.state.translations.gettext
#     logging.info(f"Translation function: {request.state.translations.gettext}")
#     greeting = _("Hello, world!")
#     logging.info(f"Greeting: {greeting}")
#     return {"message": greeting}

# @app.get("/goodbye")
# async def read_goodbye(request: Request):
#     logging.info(f"Headers: {request.headers}")
#     _ = request.state.translations.gettext
#     farewell = _("Goodbye!")
#     logging.info(f"Farewell: {farewell}")
#     return {"message": farewell}

# @app.on_event("startup")
# async def on_startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(models.Base.metadata.create_all)

# @app.exception_handler(HTTPException)
# async def http_exception_handler(request: Request, exc: HTTPException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"detail": exc.detail},
#     )

# @app.post("/ifcnews/", response_model=schemas.IfcNews)
# async def create_ifc_news(news: schemas.IfcNewsCreate, db: AsyncSession = Depends(get_db)):
#     logging.info(f"Creating news with data: {news}")
#     return await crud.create_ifc_news(db=db, news=news)

# @app.get("/ifcnews/{news_id}", response_model=schemas.IfcNews)
# async def read_ifc_news(news_id: int, db: AsyncSession = Depends(get_db)):
#     logging.info(f"Reading news with id: {news_id}")
#     db_news = await crud.get_ifc_news(db=db, news_id=news_id)
#     if db_news is None:
#         raise HTTPException(status_code=404, detail="IfcNews not found")
#     return db_news

# @app.get("/ifcnews/", response_model=List[schemas.IfcNews])
# async def read_ifc_news_list(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
#     logging.info(f"Reading news list with skip: {skip}, limit: {limit}")
#     return await crud.get_ifc_news_list(db=db, skip=skip, limit=limit)

# @app.put("/ifcnews/{news_id}", response_model=schemas.IfcNews)
# async def update_ifc_news(news_id: int, news: schemas.IfcNewsUpdate, db: AsyncSession = Depends(get_db)):
#     logging.info(f"Updating news with id: {news_id} and data: {news}")
#     db_news = await crud.update_ifc_news(db=db, news_id=news_id, news=news)
#     if db_news is None:
#         raise HTTPException(status_code=404, detail="IfcNews not found")
#     return db_news

# @app.delete("/ifcnews/{news_id}", response_model=schemas.IfcNews)
# async def delete_ifc_news(news_id: int, db: AsyncSession = Depends(get_db)):
#     logging.info(f"Deleting news with id: {news_id}")
#     db_news = await crud.delete_ifc_news(db=db, news_id=news_id)
#     if db_news is None:
#         raise HTTPException(status_code=404, detail="IfcNews not found")
#     return db_news


import os
import logging
from urllib import response
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from starlette.middleware.sessions import SessionMiddleware
from babel.support import Translations

from app import crud, models, schemas
from app.database import engine, get_db

# Настройка логирования
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Путь к файлам перевода
LOCALE_DIR = os.path.join(os.path.dirname(__file__), '../locale')
logging.info(f"LOCALE_DIR: {LOCALE_DIR}")

# Функция для выбора локали
def get_locale(request: Request):
    lang_header = request.headers.get('Accept-Language', 'ru')
    logging.info(f"Received Accept-Language header: {lang_header}")
    lang = lang_header.split(',')[0] if lang_header else 'ru'
    logging.info(f"Selected language: {lang}")
    return lang

# Middleware для сессий (необходимо для сохранения языка)
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

@app.middleware("http")
async def add_translation(request: Request, call_next):
    logging.info(f"Request headers: {request.headers}")
    lang = get_locale(request)
    logging.info(f"Using language: {lang}")

    translations = None
    general_lang = lang.split('-')[0]  # Инициализация general_lang сразу

    # Проверка наличия файлов перевода
    lang_path = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'messages.mo')
    general_lang_path = os.path.join(LOCALE_DIR, general_lang, 'LC_MESSAGES', 'messages.mo')
    logging.info(f"Checking for translation files at {lang_path} and {general_lang_path}")

    if os.path.exists(lang_path):
        logging.info(f"Found translation file at {lang_path}")
        try:
            translations = Translations.load(LOCALE_DIR, [lang])
            logging.info(f"Translations loaded for language: {lang}")
            logging.info(f"Loaded translations catalog: {translations._catalog}")
        except Exception as e:
            logging.error(f"Error loading translations for language {lang}: {e}")
    else:
        logging.warning(f"Translation file not found at {lang_path}")

    if not isinstance(translations, Translations) or not translations._catalog:
        if os.path.exists(general_lang_path):
            logging.info(f"Found general translation file at {general_lang_path}")
            if general_lang != lang:  # Проверка, чтобы не fallback на тот же язык
                try:
                    translations = Translations.load(LOCALE_DIR, [general_lang])
                    logging.info(f"Fallback to general language translations: {general_lang}")
                    logging.info(f"Loaded translations catalog: {translations._catalog}")
                except Exception as e:
                    logging.error(f"Error loading general language translations for {general_lang}: {e}")
        else:
            logging.warning(f"General translation file not found at {general_lang_path}")

    if not isinstance(translations, Translations) or not translations._catalog:
        try:
            translations = Translations.load(LOCALE_DIR, ['ru'])
            logging.info("Fallback to Russian translations")
            logging.info(f"Loaded translations catalog: {translations._catalog}")
        except Exception as e:
            logging.error(f"Error loading fallback Russian translations: {e}")

    logging.info(f"Translations object: {translations}")
    request.state.translations = translations
    response = await call_next(request)
    return response

@app.get("/")
async def read_root(request: Request):
    logging.info(f"Headers: {request.headers}")
    _ = request.state.translations.gettext
    logging.info(f"Translation function: {request.state.translations.gettext}")
    greeting = _("Hello, world!")
    logging.info(f"Greeting: {greeting}")
    return {"message": greeting}

@app.get("/goodbye")
async def read_goodbye(request: Request):
    logging.info(f"Headers: {request.headers}")
    _ = request.state.translations.gettext
    farewell = _("Goodbye!")
    logging.info(f"Farewell: {farewell}")
    return {"message": farewell}

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.post("/ifcnews/", response_model=schemas.IfcNews)
async def create_ifc_news(news: schemas.IfcNewsCreate, db: AsyncSession = Depends(get_db)):
    logging.info(f"Creating news with data: {news}")
    return await crud.create_ifc_news(db=db, news=news)

@app.get("/ifcnews/{news_id}", response_model=schemas.IfcNews)
async def read_ifc_news(news_id: int, db: AsyncSession = Depends(get_db)):
    logging.info(f"Reading news with id: {news_id}")
    db_news = await crud.get_ifc_news(db=db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="IfcNews not found")
    return db_news

@app.get("/ifcnews/", response_model=List[schemas.IfcNews])
async def read_ifc_news_list(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    logging.info(f"Reading news list with skip: {skip}, limit: {limit}")
    return await crud.get_ifc_news_list(db=db, skip=skip, limit=limit)

@app.put("/ifcnews/{news_id}", response_model=schemas.IfcNews)
async def update_ifc_news(news_id: int, news: schemas.IfcNewsUpdate, db: AsyncSession = Depends(get_db)):
    logging.info(f"Updating news with id: {news_id} and data: {news}")
    db_news = await crud.update_ifc_news(db=db, news_id=news_id, news=news)
    if db_news is None:
        raise HTTPException(status_code=404, detail="IfcNews not found")
    return db_news


@app.delete("/ifcnews/{news_id}", response_model=schemas.IfcNews)
async def delete_ifc_news(news_id: int, db: AsyncSession = Depends(get_db)):
    logging.info(f"Deleting news with id: {news_id}")
    db_news = await crud.delete_ifc_news(db=db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="IfcNews not found")
    return db_news
