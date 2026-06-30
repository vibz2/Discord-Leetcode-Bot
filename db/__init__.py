# Initialize Database
from db.scripts.init_db import (
    get_connection,
    init_db
)

# User functions
from db.scripts.db_users import (
    link_user,
    get_leetcode_username
)

# Solution/Problem Functions
from db.scripts.db_solutions import (
    submission_exists,
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
    # Initialize Database
    "get_connection",
    "init_db",

    # User functions
    "link_user",
    "get_leetcode_username",

    # Solution/Problem Functions
    "submission_exists",
    "has_solved_before",
    "add_solution",
    "clear_user_data",
    "clear_all_data",

    # Fetch Functions
    "get_leaderboard",
    "get_user_stats"
]
