# 01 - Branches Basics: Create, Switch, Delete

## Introduction
Git branches allow you to work on different features or fixes independently.

## Creating a Branch
```bash
git branch feature/new-login
git checkout -b feature/new-login
```

## Switching Branches
```bash
git checkout main
git switch feature/new-login
```

## Deleting Branches
```bash
git branch -d feature/old-branch
git branch -D feature/unmerged-branch
```

## Best Practices
- Use descriptive branch names
- Keep branches short-lived
