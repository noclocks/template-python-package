# Python Package Template

> [!NOTE]
> This repository serves as a template for creating Python Projects that follow the Python Standards declared in [PEP 621](https://peps.python.org/pep-0621/) for *storing project metadata in pyproject.toml*.

## Contents

## Overview

This template project utilizes a `pyproject.toml` file to configure the project and [Flit](https://github.com/pypa/flit/) to simplify the build process and publish to [PyPI](pypi.org).

Flit simplifies the build and packaging process for Python projects by eliminating the need for separate `setup.py` and `setup.cfg` files.

With Flit, you can manage all relevant configurations within the `pyproject.toml` file, streamlining development and promoting maintainability by centralizing project metadata, dependencies, and build specifications in one place.

## Structure

The project structure is as follows:

```plaintext
```

- `.github/workflows`: Contains GitHub Actions workflows for the project.
- `.devcontainer/`: Contains development container configurations.
- `.vscode/`: Contains Visual Studio Code configurations.
- `src/`: Contains the source code for the project.
- `tests/`: Contains test files for the project.
- `docs/`: Contains project documentation.
- `pyproject.toml`: Contains project metadata and build configurations.

### pyproject.toml

The `pyproject.toml` file is a centralized configuration file for modern Python projects. It streamlines the development process by managing project metadata, dependencies, and development tool configurations in a single, structured file. This approach ensures consistency and maintainability, simplifying project setup and enabling developers to focus on writing quality code. Key components include project metadata, required and optional dependencies, development tool configurations (e.g., linters, formatters, and test runners), and build system specifications.

In this particular pyproject.toml file, the [build-system] section specifies that the Flit package should be used to build the project. The [project] section provides metadata about the project, such as the name, description, authors, and classifiers. The [project.optional-dependencies] section lists optional dependencies, like pyspark, while the [project.urls] section supplies URLs for project documentation, source code, and issue tracking.

The file also contains various configuration sections for different tools, including bandit, black, coverage, flake8, pyright, pytest, tox, and pylint. These sections specify settings for each tool, such as the maximum line length for flake8 and the minimum code coverage percentage for coverage.

#### Tools

#### black

#### coverage

#### pytest

#### pylint

#### pyright


#### flake8

#### tox

## Development
