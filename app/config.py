import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://ifcadmin:1234@localhost/ifc_db")
