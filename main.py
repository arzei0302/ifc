# import os
# import logging
# from contextlib import asynccontextmanager
# import uvicorn
# from fastapi import FastAPI, Request
# from fastapi.responses import ORJSONResponse
# from babel.support import Translations
# from starlette.middleware.sessions import SessionMiddleware
# from core.config import settings
# from api import router as api_router
# from core import db_helper

# logging.basicConfig(level=logging.INFO)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # startup
#     yield
#     # shutdown
#     await db_helper.dispose()

# main_app = FastAPI(
#     default_response_class=ORJSONResponse,
#     lifespan=lifespan,
# )
# main_app.include_router(
#     api_router, 
#     prefix=settings.api.prefix,
# )

# LOCALE_DIR = os.path.join(os.path.dirname(__file__), './locale')
# logging.info(f"LOCALE_DIR: {LOCALE_DIR}")

# # Функция для выбора локали
# def get_locale(request: Request):
#     lang_header = request.headers.get('Accept-Language', 'ru')
#     logging.info(f"Received Accept-Language header: {lang_header}")
#     lang = lang_header.split(',')[0] if lang_header else 'ru'
#     logging.info(f"Selected language: {lang}")
#     return lang

# # Middleware для сессий (необходимо для сохранения языка)
# main_app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# @main_app.middleware("http")
# async def add_translation(request: Request, call_next):
#     logging.info(f"Request headers: {request.headers}")
#     lang = get_locale(request)
#     logging.info(f"Using language: {lang}")

#     translations = None
#     general_lang = lang.split('-')[0]  # Инициализация general_lang сразу

#     # Проверка наличия файлов перевода
#     lang_path = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'messages.mo')
#     general_lang_path = os.path.join(LOCALE_DIR, general_lang, 'LC_MESSAGES', 'messages.mo')
#     logging.info(f"Checking for translation files at {lang_path} and {general_lang_path}")

#     if os.path.exists(lang_path):
#         logging.info(f"Found translation file at {lang_path}")
#         try:
#             translations = Translations.load(LOCALE_DIR, [lang])
#             logging.info(f"Translations loaded for language: {lang}")
#             logging.info(f"Loaded translations catalog: {translations._catalog}")
#         except Exception as e:
#             logging.error(f"Error loading translations for language {lang}: {e}")
#     else:
#         logging.warning(f"Translation file not found at {lang_path}")

#     if not isinstance(translations, Translations) or not translations._catalog:
#         if os.path.exists(general_lang_path):
#             logging.info(f"Found general translation file at {general_lang_path}")
#             if general_lang != lang:  # Проверка, чтобы не fallback на тот же язык
#                 try:
#                     translations = Translations.load(LOCALE_DIR, [general_lang])
#                     logging.info(f"Fallback to general language translations: {general_lang}")
#                     logging.info(f"Loaded translations catalog: {translations._catalog}")
#                 except Exception as e:
#                     logging.error(f"Error loading general language translations for {general_lang}: {e}")
#         else:
#             logging.warning(f"General translation file not found at {general_lang_path}")

#     if not isinstance(translations, Translations) or not translations._catalog:
#         try:
#             translations = Translations.load(LOCALE_DIR, ['ru'])
#             logging.info("Fallback to Russian translations")
#             logging.info(f"Loaded translations catalog: {translations._catalog}")
#         except Exception as e:
#             logging.error(f"Error loading fallback Russian translations: {e}")

#     logging.info(f"Translations object: {translations}")
#     request.state.translations = translations
#     response = await call_next(request)
#     return response

# @main_app.get("/")
# async def read_root(request: Request):
#     logging.info(f"Headers: {request.headers}")
#     _ = request.state.translations.gettext
#     logging.info(f"Translation function: {request.state.translations.gettext}")
#     greeting = _("Hello, world!")
#     logging.info(f"Greeting: {greeting}")
#     return {"message": greeting}

# @main_app.get("/goodbye")
# async def read_goodbye(request: Request):
#     logging.info(f"Headers: {request.headers}")
#     _ = request.state.translations.gettext
#     farewell = _("Goodbye!")
#     logging.info(f"Farewell: {farewell}")
#     return {"message": farewell}

# if __name__ == "__main__":
#     uvicorn.run(
#         "main:main_app",
#         host=settings.run.host,
#         port=settings.run.port,
#         reload=True,
#     )



# import os
# import logging
# from contextlib import asynccontextmanager
# import uvicorn
# from fastapi import FastAPI, Request
# from fastapi.responses import ORJSONResponse
# from babel.support import Translations
# from starlette.middleware.sessions import SessionMiddleware
# from core.config import settings
# from api import router as api_router
# from core import db_helper

# logging.basicConfig(level=logging.INFO)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # startup
#     yield
#     # shutdown
#     await db_helper.dispose()

# main_app = FastAPI(
#     default_response_class=ORJSONResponse,
#     lifespan=lifespan,
# )
# main_app.include_router(
#     api_router, 
#     prefix=settings.api.prefix,
# )

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
# main_app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# @main_app.middleware("http")
# async def add_translation(request: Request, call_next):
#     logging.info(f"Request headers: {request.headers}")
#     lang = get_locale(request)
#     logging.info(f"Using language: {lang}")

#     translations = None
#     general_lang = lang.split('-')[0]  # Инициализация general_lang сразу

#     # Проверка наличия файлов перевода
#     lang_path = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'messages.mo')
#     general_lang_path = os.path.join(LOCALE_DIR, general_lang, 'LC_MESSAGES', 'messages.mo')
#     logging.info(f"Checking for translation files at {lang_path} and {general_lang_path}")

#     if os.path.exists(lang_path):
#         logging.info(f"Found translation file at {lang_path}")
#         try:
#             translations = Translations.load(LOCALE_DIR, [lang])
#             logging.info(f"Translations loaded for language: {lang}")
#             logging.info(f"Loaded translations catalog: {translations._catalog}")
#         except Exception as e:
#             logging.error(f"Error loading translations for language {lang}: {e}")
#     else:
#         logging.warning(f"Translation file not found at {lang_path}")

#     if not isinstance(translations, Translations) or not translations._catalog:
#         if os.path.exists(general_lang_path):
#             logging.info(f"Found general translation file at {general_lang_path}")
#             if general_lang != lang:  # Проверка, чтобы не fallback на тот же язык
#                 try:
#                     translations = Translations.load(LOCALE_DIR, [general_lang])
#                     logging.info(f"Fallback to general language translations: {general_lang}")
#                     logging.info(f"Loaded translations catalog: {translations._catalog}")
#                 except Exception as e:
#                     logging.error(f"Error loading general language translations for {general_lang}: {e}")
#         else:
#             logging.warning(f"General translation file not found at {general_lang_path}")

#     if not isinstance(translations, Translations) or not translations._catalog:
#         try:
#             translations = Translations.load(LOCALE_DIR, ['ru'])
#             logging.info("Fallback to Russian translations")
#             logging.info(f"Loaded translations catalog: {translations._catalog}")
#         except Exception as e:
#             logging.error(f"Error loading fallback Russian translations: {e}")

#     logging.info(f"Translations object: {translations}")
#     request.state.translations = translations
#     response = await call_next(request)
#     return response

# @main_app.get("/")
# async def read_root(request: Request):
#     logging.info(f"Headers: {request.headers}")
#     _ = request.state.translations.gettext
#     logging.info(f"Translation function: {request.state.translations.gettext}")
#     greeting = _("Hello, world!")
#     logging.info(f"Greeting: {greeting}")
#     return {"message": greeting}

# @main_app.get("/goodbye")
# async def read_goodbye(request: Request):
#     logging.info(f"Headers: {request.headers}")
#     _ = request.state.translations.gettext
#     farewell = _("Goodbye!")
#     logging.info(f"Farewell: {farewell}")
#     return {"message": farewell}

# if __name__ == "__main__":
#     uvicorn.run(
#         "main:main_app",
#         host=settings.run.host,
#         port=settings.run.port,
#         reload=True,
#     )
