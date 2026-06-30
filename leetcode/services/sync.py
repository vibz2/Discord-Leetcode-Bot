from db import get_leetcode_username, submission_exists, add_solution

from leetcode import get_recent_submissions, get_problem


def sync_user(discord_user_id):
    leetcode_username = get_leetcode_username(discord_user_id)
    

    if not leetcode_username:
        raise ValueError(
            "No linked LeetCode account."
        )

    submissions = (get_recent_submissions(leetcode_username))

    imported = 0
    skipped = 0
    points_earned = 0

    for submission in submissions:
        problem_slug = (submission["titleSlug"])
        timestamp = int(submission["timestamp"])

        if submission_exists(discord_user_id, problem_slug, timestamp):
            skipped += 1
            continue

        problem = get_problem(problem_slug)

        points = add_solution(user_id=discord_user_id, problem_id=int(problem["questionId"]),
                              problem_slug=problem_slug, difficulty=problem["difficulty"],
                              timestamp=timestamp)

        imported += 1
        points_earned += points

    return {
        "imported": imported,
        "skipped": skipped,
        "points": points_earned
    }