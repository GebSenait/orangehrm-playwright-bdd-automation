# Branch Strategy

## Branch Structure

This repository uses a two-branch strategy:

### 1. `main` Branch (Default)
- **Purpose:** Production-ready, stable code
- **Status:** Default branch for remote repository
- **Usage:** Contains all completed and tested features
- **Protection:** Should only receive changes via merge from `task-dev-demo`

### 2. `task-dev-demo` Branch (Development)
- **Purpose:** Active development and feature work
- **Status:** Development branch
- **Usage:** All new features, fixes, and improvements are developed here
- **Workflow:** Changes are merged to `main` after stabilization

## Current Branch Status

- ✅ `main` - Created and set as default
- ✅ `task-dev-demo` - Active development branch with all commits

## Workflow

### Development Process

1. **Work on `task-dev-demo`:**
   ```bash
   git checkout task-dev-demo
   # Make changes, commit
   git add .
   git commit -m "Description of changes"
   ```

2. **Merge to `main` when ready:**
   ```bash
   git checkout main
   git merge task-dev-demo --no-edit
   git push origin main
   ```

3. **Continue development:**
   ```bash
   git checkout task-dev-demo
   # Continue working...
   ```

## Setting Up Remote Repository

When you're ready to push to a remote repository:

### Initial Push

```bash
# Add remote (replace with your repository URL)
git remote add origin <your-repository-url>

# Push main branch and set as upstream
git push -u origin main

# Push task-dev-demo branch
git checkout task-dev-demo
git push -u origin task-dev-demo
```

### Setting Default Branch on GitHub/GitLab

1. Go to repository settings
2. Navigate to "Branches" or "Default branch"
3. Set `main` as the default branch
4. Optionally protect `main` branch (require pull requests)

## Branch Commands Reference

```bash
# Switch to main
git checkout main

# Switch to task-dev-demo
git checkout task-dev-demo

# Create new feature branch from task-dev-demo
git checkout task-dev-demo
git checkout -b feature/new-feature

# Merge task-dev-demo into main
git checkout main
git merge task-dev-demo

# View all branches
git branch -a

# View branch history
git log --oneline --graph --all
```

## Best Practices

1. ✅ Keep `main` clean and stable
2. ✅ Do all development on `task-dev-demo` or feature branches
3. ✅ Test thoroughly before merging to `main`
4. ✅ Use descriptive commit messages
5. ✅ Merge `task-dev-demo` to `main` after feature completion

