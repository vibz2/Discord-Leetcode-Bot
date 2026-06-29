from schemas.solutions import create_table as create_solutions_table
from schemas.users import create_table as create_users_table

SCHEMAS = [
    create_users_table,
    create_solutions_table
]