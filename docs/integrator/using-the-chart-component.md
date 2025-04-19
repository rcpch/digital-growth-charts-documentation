---
title: Using the chart component
reviewers: Dr Simon Chapman
audience: integrators, implementers, technical-architects
---

## Installing the chart component

The API and the charting component have been build to work together, but stand separately. The API returns centiles and SDS against measurements as a structure JSON `Measurement` object. Most users want to chart these. 

The chart component is written in typescript and react and accepts the API response as a prop. There is a [`storybook` instance](https://live--6732292d6f3624b0036f84b4.chromatic.com/) as a demonstration and an [interactive demonstration](https://growth.rcpch.ac.uk/)


https://cdn.jsdelivr.net/npm/@rcpch/digital-growth-charts-react-component-library@latest/build/umd/sri-hash.txt