---
title: RCPCHGrowth and Research
reviewers: Dr Simon Chapman
audience: researchers
---

# How to Use RCPCHGrowth in Research

The RCPCHGrowth algorithm builds on [LMSGrowth](https://www.healthforallchildren.com/t/191) excel plug in developed by Prof Tim Cole and Huiqi Pan.

It is common to need to calculate z-scores and centiles against children's growth measurements for datasets in research, and using the RCPCH API is not always possible.

To preserve security RCPCHGrowth can be installed on a local machine and the calculations can be run using familiar tools interacting with it.

## Getting Started

Python notebooks are popular as they combine the convenience of markdown with access to tools like pandas and scipy or numpy. RCPCHGrowth can be used in the same way.

### Python Environment

Setting up a python environment is discussed in detail [here](/docs/developer/api-python.md#managing-python-versions)

Once a virtual environment has been created, RCPCHGrowth can be installed directly:

```console
pip install rcpchgrowth['notebook'] 
```

The `['notebook']` is optional - it automatically installs all the notebook related dependencies ("pandas>=1.5", "matplotlib>=3.7", "jupyterlab", "ipykernel"). If you have these already then you can simply:

```console
pip install rcpchgrowth
```

To access the calculations within the RCPCHGrowth package, import it to access the functions.

```python
import rcpchgrowth
```

For examples and more documentation visit our [Binder](https://mybinder.org/v2/gh/rcpch/rcpchgrowth-python/live?labpath=notebooks%2FQuickstart.ipynb)