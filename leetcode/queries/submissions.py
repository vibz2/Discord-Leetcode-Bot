from leetcode.client import graphql

def get_recent_submissions(
    username,
    limit=20
):
    query = """
    query ($username: String!, $limit: Int!) {
      recentAcSubmissionList(
        username: $username,
        limit: $limit
      ) {
        title
        titleSlug
        timestamp
      }
    }
    """

    data = graphql(
        query,
        {
            "username": username,
            "limit": limit
        }
    )

    return data["recentAcSubmissionList"]