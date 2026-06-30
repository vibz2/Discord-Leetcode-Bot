import requests

URL = "https://leetcode.com/graphql"


def graphql(query, variables=None):
    response = requests.post(
        URL,
        json={
            "query": query,
            "variables": variables or {}
        }
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        raise Exception(data["errors"])

    return data["data"]