# Workspace Rules: Conventional Commit Messages

All git commit messages in this repository must strictly adhere to the Conventional Commits specification.

## Structure
Every commit message must follow this format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Allowed Types
* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Changes to documentation
* **style**: Formatting, white-space, missing semi-colons (no production code changes)
* **refactor**: Code changes that neither fix a bug nor add a feature
* **perf**: Code changes that improve performance
* **test**: Adding or correcting tests (no production code changes)
* **build**: Changes that affect the build system or external dependencies
* **ci**: Changes to CI configuration files and scripts
* **chore**: Other changes that don't modify src or test files
* **revert**: Reversion of a previous commit

## Rules & Constraints
1. The commit message header must be concise and ideally under 50 characters.
2. The description must be in lowercase.
3. Use the imperative mood in the description (e.g., "add feature" instead of "added feature" or "adds feature").
4. No trailing period at the end of the description.
5. Breaking changes must be indicated by a `!` after the type/scope (e.g., `feat!: drop support for Python 3.8`) or in the footer as `BREAKING CHANGE: <description>`.

