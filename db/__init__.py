# Database Initialization
from db.scripts.init_db import init_db, get_connection

# User functions
from db.scripts.db_users import (
    link_user
)

# Solution/Problem Functions
from db.scripts.db_solutions import (
    has_solved_before,
    add_solution,
    clear_user_data,
    clear_all_data
)

# Fetch Functions
from db.scripts.db_fetch import (
    get_leaderboard,
    get_user_stats
)

__all__ = [
    #Database Initialization
    "init_db",
    "get_connection",

    # User functions
    "link_user",

    # Solution/Problem Functions
    "has_solved_before",
    "add_solution",
    "clear_user_data",
    "clear_all_data",

    # Fetch Functions
    "get_leaderboard",
    "get_user_stats"
]
