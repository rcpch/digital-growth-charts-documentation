---
title: Versioning
reviewers: Dr Marcus Baw, Dr Anchit Chandran
audience: developers
---

# Versioning the API Server's code

We distinguish between:

1. The API version itself
2. The server code which creates API responses

All of this documentation relates to **Version 1** of the RCPCH Digital Growth Charts API.

Server code versions may vary.

## Semantic Versioning

We use [Semantic Versioning (SemVer)](https://semver.org/) to ensure server versions are systematically applied.

## Bump2version

We use `bump2version` tool to simplify versioning in the `digital-growth-charts-server` and `rcpchgrowth-python` packages.

## References

With every deploy of the server, `generate_and_store_chart_data` gets run, which skips centile chart generation from references if they already exist. On the command line though it is possible to override this and rebuild all the centile data files.

```python
python
from main import generate_and_store_chart_data
generate_and_store_chart_data(overwrite=True)
```
