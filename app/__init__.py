""" __init__.py transforms the current folder into a package, it is needed to allow imports as modules from anywhere using the same path:
'from app.config.database import create_db_and_tables' (global path), without __init__.py, we would need to import it from the relative
path:  'from .config.database import create_db_and_tables' """
