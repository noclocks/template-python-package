# Documentation

> [!NOTE]
> The `docs/` folder houses plain-text, markdown files with technical documentation about the project.

## Contents

- [Overview](#overview)
- [Structure](#structure)
- [Notes](#notes)
- [Reference](#reference)

## Overview

> [!NOTE]
> This project is documented using [MkDocs](), a static-site generator written in Python.

## Structure

```plaintext
docs/
├── index.md               # (this file)
├── about.md               # about the project
├── assets/                # static assets
│   ├── img/               # images
│   ├── styles/*.css       # custom CSS styles
│   ├── scripts/*.js       # custom JS scripts
│   └── ...                # fonts, animations, favicons, icons, data, metadata, etc. 
├── decisions/             # architecture decision record docs
│   ├── index.md           # decision records index
│   ├── 00-template.md     # default decision record template
│   ├── 01-Decision.md     # (example, doesn't actually exist)
│   └── ...                # ordered decision records
├── development/           # development docs
│   ├── index.md           # development docs index
│   ├── setup.md           # project setup docs
│   ├── techstack.md       # project tech-stack docs
│   └── ...                # contributing, code-of-conduct, changelog, etc.
├── reference/             # reference (generated) docs
│   ├── index.md           # reference docs index
│   └── pkg/               # python package reference
│      ├── ...             # module-level and function-level docs
└── overrides/*/*.html     # mkdocs overrides (i.e. analytics.html)
```

## Notes

- `mkdocs` configuration stored in [`mkdocs.yml`](../mkdocs.yml).
- Uses `mkdocs-material` add-on library
- Deployed via [`.github/workflows/mkdocs.yml`](../.github/workflows/mkdocs.yml) to GitHub Pages using the `gh-pages` branch
- Deployed to No Clocks' sub-domain: `docs.noclocks.dev/template-python-package/*` URL

## Reference

- [MkDocs Documentation]()
- [MkDocs Material Documentation]()

***

(c) [No Clocks, LLC](https://github.com/noclocks/) | 2024
