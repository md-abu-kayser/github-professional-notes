#!/bin/bash
# Usage: ./create-issue.sh "Title" "Body"
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/$OWNER/$REPO/issues \
  -d "{\"title\":\"$1\",\"body\":\"$2\"}"