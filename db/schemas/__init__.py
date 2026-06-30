from db.schemas.solutions import create_table as create_solutions_table
from db.schemas.users import create_table as create_users_table

SCHEMAS = [
    create_users_table,
    create_solutions_table
]