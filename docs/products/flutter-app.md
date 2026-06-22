---
title: dGC App
reviewers: Dr Simon Chapman
audience: developers, integrators
---

# RCPCH Digital Growth Charts App

This is a project written in [Flutter](https://flutter.dev) still in alpha and not in production.

Flutter has been chosen as it is a mature framework that compiles to iOS, Android, Web and Linus from a single codebase.

It is a mobile client wrapper for the dGC API and therefore needs an API key.

## Getting started

See [Github](https://github.com/rcpch/digital-growth-charts-app)

## Development IDE

Android studio is well set up for Flutter development, but VSCode works equally well. It is important first to create a development environment that includes the Android and iOS SDKs. Note that if you are using iOS, you will need to use a Mac and have XCode installed.

## Credentials

These should be stored in a `.env` file in the root of the project and include:

```bash
DGC_BASE_URL=https://api.rcpch.ac.uk/growth/v1
DGC_API_KEY="YOUR-API_KEY"
```

!!! danger "Credentials - Clinical Safety Risk"
    **Do not commit credentials to GitHub**

The Digital Growth Charts App makes API calls to the `/uk-who/calculation` and `/uk-who/chart-coordinates` endpoints. It caches the charts only for those requested measurements for the duration of the session.

## Contribute

This is a new (2025) project. Please post [issues](https://github.com/rcpch/digital-growth-charts-app/issues) and suggestions for improvement.
