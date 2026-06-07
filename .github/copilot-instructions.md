# Repo Guidance for AI Assistants

This repository is a collection of audio-processing examples, not a single application.

When a task needs a plan, save it in the root `plans/` folder using a file name like `YYYY-MM-DD-simple-title.md`. Use the current date, keep the title short and lowercase, and separate words with hyphens.

Before making changes or suggesting commands, inspect the local example folder first and use the closest existing docs and tool files as the source of truth. Prefer the example's `README.md`, `justfile`, `pyproject.toml`, `Pipfile`, or similar local configuration over repo-wide assumptions.

The workspace uses mixed tooling across subprojects, including Python, `just`, `uv`, `pipenv`, `nix`, and standalone binary artifacts. Do not assume one build system applies everywhere.

Treat Max for Live folders as artifact-centric unless source files are present. If a folder only contains `.amxd` files, do not invent source code or a build pipeline; ask for the source workflow or work from the available artifact and nearby documentation.

When helping with a task, first identify the relevant example directory, then stay within that scope unless the user asks for cross-repo changes.