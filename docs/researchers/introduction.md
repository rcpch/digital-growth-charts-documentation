---
title: RCPCHGrowth and Research
reviewers: Dr Simon Chapman
audience: researchers
---

# How to Use RCPCHgrowth in Research

It is common to need to calculate z-scores and centiles against children's growth measurements for datasets in research, and using the RCPCH API is not always possible, for example when operating inside a Secure Research Environment (SRE) or when working offline. The RCPCHgrowth python package can be installed inside a Trusted Research Environment or Secure Data Environment and the calculations can be run locally, using familiar tools like Jupyter Notebooks.

## Getting Started

Python notebooks are popular as they combine Markdown-formatted text with computational tools like `pandas` and `scipy` or `numpy`.

The notebooks themselves are their own best documentation. To get them running there are two options: using Docker, or installing directly into your local Python environment.

### Python Environment

Setting up a Python environment is discussed in detail [here](../developer/api-python#managing-python-versions)

Once a virtual environment has been created, RCPCHGrowth can be installed directly:

```console
pip install rcpchgrowth['notebook']
```

The `['notebook']` is optional - it automatically installs all the notebook related dependencies. These are essential if you are planning to use the notebooks. If you already have these installed, you can simply:

```console
pip install rcpchgrowth
```

To access the calculations within the RCPCHGrowth package, import it to access the functions in your `.ipynb` file.

```python
import rcpchgrowth
```

### Docker

The Docker setup helps you easily interact with the notebook examples provided by RCPCH. You will need Docker [installed](../developer/api-python#api-docker.md)

Then from the command line:

```console
s/up
```

This will create a container which will build RCPCHGrowth and in the console you can follow the link:

```bash
...
rcpchgrowth-dev  | [I 2025-08-17 15:32:27.147 ServerApp] jupyterlab | extension was successfully loaded.
rcpchgrowth-dev  | [I 2025-08-17 15:32:27.147 ServerApp] Serving notebooks from local directory: /app/notebooks
rcpchgrowth-dev  | [I 2025-08-17 15:32:27.147 ServerApp] Jupyter Server 2.16.0 is running at:
rcpchgrowth-dev  | [I 2025-08-17 15:32:27.147 ServerApp] http://7f2a9b1a289c:8888/lab
rcpchgrowth-dev  | [I 2025-08-17 15:32:27.147 ServerApp]     http://127.0.0.1:8888/lab
rcpchgrowth-dev  | [I 2025-08-17 15:32:27.147 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
...
```

which will open the notebooks in your browser.
