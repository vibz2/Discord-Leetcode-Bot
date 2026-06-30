from leetcode.client import graphql


def get_problem(
    title_slug
):
    query = """
    query ($titleSlug: String!) {
      question(
        titleSlug: $titleSlug
      ) {
        questionId
        titleSlug
        difficulty
      }
    }
    """

    data = graphql(
        query,
        {
            "titleSlug": title_slug
        }
    )

    return data["question"]