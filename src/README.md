# Python Package Source Code

> [!NOTE]
> This `src` folder houses the *source code* for the Python Package (including all modules, etc.)

## Contents

- [Overview](#overview)
- [Structure](#structure)
- [Notes](#notes)
- [Reference](#reference)

## Overview

> [!NOTE]
> This repository template uses the "src layout" for [Python Packaging](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).

The "src layout" deviates from a "flat layout" by moving the source code that is intended to be importable (i.e. `import pkg`) into the `src` sub-directory.

## Structure

> [!NOTE]
> The structure below is not exactly representative of this repository's structure but instead is a reference to a typical structure. 

```plaintext
src/
├── README.md
├── pkg/
│   ├── __init__.py
│   ├── __main__.py
│   └── ...
└── tools/
    ├── __init__.py
    ├── tool_one.py
    ├── ...
    └── tool_n.py
```

## Notes

Notes about using a "src layout":

- Requires installation of the project to be able to run its code.
- Requires an additional step in the development workflow of the project (i.e. an [editable installation]() is used for development and a regular installation is used for testing).
- Helps prevent accidental usage of the in-development copy of the codebase
- Keeps import packages separate from root directory of the project, ensuring that the installed copy is used during testing and publication.

## Reference

- [src layout vs flat layout - Python Packaging User Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [Packaging and distributing projects - Python Packaging User Guide](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
