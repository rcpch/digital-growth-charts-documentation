---
title: RCPCHGrowth and Research
reviewers: Dr Simon Chapman
audience: researchers
---

# How to Use RCPCHGrowth in Research

The RCPCHGrowth algorithm is inspire by the [LMSGrowth](https://www.healthforallchildren.com/t/191) excel plug-in developed by Prof Tim Cole and Huiqi Pan.

It is common to need to calculate z-scores and centiles against children's growth measurements for datasets in research, and using the RCPCH API is not always possible.

To preserve security RCPCHGrowth can be installed on a local machine and the calculations can be run using familiar tools interacting with it.

## Getting Started

Python notebooks are popular as they combine the convenience of markdown with access to tools like pandas and scipy or numpy. RCPCHGrowth can be used in the same way.

The notebooks themselves are their own best documentation. To get them running there are two options: using docker, or installing directly into your local python environment.

### Python Environment

Setting up a python environment is discussed in detail [here](/docs/developer/api-python.md#managing-python-versions)

Once a virtual environment has been created, RCPCHGrowth can be installed directly:

```console
pip install rcpchgrowth['notebook'] 
```

The `['notebook']` is optional - it automatically installs all the notebook related dependencies ("pandas>=1.5", "matplotlib>=3.7", "jupyterlab", "ipykernel"). These are essential if you are planning to use the notebooks. If you already have these installed, you can simply:

```console
pip install rcpchgrowth
```

To access the calculations within the RCPCHGrowth package, import it to access the functions in your `.ipynb` file.

```python
import rcpchgrowth
```

### Docker

This is if you want to view the notebook examples provided by RCPCH. You will need docker [installed](/docs/developer/api-python.md#api-docker.md)

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