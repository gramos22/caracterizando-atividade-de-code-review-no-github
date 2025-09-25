SEARCH_REPOSITORIES = """
query($q:String!, $first:Int!) {
  search(query: $q, type: REPOSITORY, first: $first) {
    nodes {
      ... on Repository {
        name
        owner { login }
        stargazerCount
        url
        description
      }
    }
  }
}
"""

GET_PULL_REQUESTS = """
query($owner:String!, $name:String!, $first:Int!) {
  repository(owner:$owner, name:$name) {
    pullRequests(states:CLOSED, first:$first, orderBy:{field:CREATED_AT, direction:DESC}) {
      nodes {
        number
        title
        author { login }
        createdAt
        closedAt
        merged
        mergedAt
        additions
        deletions
        changedFiles
        bodyText
        url
        participants { totalCount }
        comments { totalCount }
        reviews(first:10) {
          nodes {
            author { login }
            submittedAt
          }
        }
      }
    }
  }
}
"""
