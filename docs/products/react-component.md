---
title: React Chart Component
reviewers: Dr Marcus Baw, Dr Simon Chapman, Dr Anchit Chandran
---

{% set repository_name="rcpch/digital-growth-charts-react-component-library" -%}
[digital-growth-charts-react-component-library](https://github.com/rcpch/digital-growth-charts-react-component-library) is a React 18.2 Typescript component library which 'knows' how to display the results from the REST API, as a familiar digital growth chart.<br/>
![NPM Version](https://img.shields.io/npm/v/%40rcpch%2Fdigital-growth-charts-react-component-library?style=flat-square&labelColor=%2311a7f2&color=%230d0d58)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/rcpch/digital-growth-charts-react-component-library?style=flat-square&labelColor=%2311a7f2&color=%230d0d58)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/rcpch/digital-growth-charts-react-component-library?style=flat-square&labelColor=%2311a7f2&color=%230d0d58)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rcpch/digital-growth-charts-react-component-library?style=flat-square&labelColor=%2311a7f2&color=%230d0d58)
![GitHub Repo stars](https://img.shields.io/github/stars/RCPCH/digital-growth-charts-react-component-library?style=flat-square&labelColor=%2311a7f2&color=%230d0d58)

[:octicons-mark-github-16: GitHub repository](https://github.com/{{ repository_name }})

[:material-web: Online Demo](https://growth.rcpch.ac.uk/)

## Features

* Calculation and display of height, weight, BMI, head circumference, and BMI centiles.
* Support for Trisomy 21 (Down syndrome) and Turner syndrome. **Now includes CDC (US) reference as of November 2024**
* Automatic gestational age correction, throughout the life course.
* Zoomable, scrollable charts.
* Event logging - clinical events can be associated with measurements.
* Bone age integration.
* Mid-parental heights with mid-parental centile lines (at +2 and -2 SDS).
* SDS (Standard Deviation Score) charts.
* Decimal age support.
* Customisable chart colours.
* Save chart image to clipboard.
* Tooltip information which can be optimised for clinicians or families.
* 'Whole Life Course' toggle to view only measurements or whole chart.

![height-chart-girl-component](../_assets/_images/height-chart-girl-component.png)

You can use the component as-is in a React app, or include it in plain HTML or any other JavaScript framework.

## Supported Features

* Corrected/Chronological age with toggle
* Zoom with zoom reset (optional prop)
* Event logging - events associated with measurements
* Bone ages
* Mid-parental heights with mid-parental centile lines (at +2 and -2 SDS)

### Version 7 new features

* Update to react 18.2
* Centile label toggle
* React testing with Jest
* Deprecate styles in favour of themes (custom theme can be supplied)
* **In 7.1, includes CDC (US) reference as of November 2024**

### Version 6 new features

* Rework the data structure to match that from API to prevent persisting data in the component in future
* BMI SDS lines
* SDS charts
* Save to clipboard

### New in 6.1

* Dates included in tooltips
* `clinicianFocus` (optional prop) to toggle between advice strings aimed at clinicians or those aimed at families / children & young people
* Toggle button to allow user to constrain viewable chart to measurements or view the whole chart

## Background

### Why a Chart library?

In the process of building the API, we realised the difficulty for developers unfamiliar with growth charts to produce one acceptable to clinicians.

For example, charts typically have 9 main centile lines (though there are other formats), each of which can be rendered as a series. However, the UK-WHO chart is made of several growth references, each from different datasets, and it is a stipulation that they must not overlap. This means that for the four datasets which make up UK-WHO, the developer must render 36 separate 'sections' of centile lines, marrying them up correctly.

Even then, there are certain rules which are key, published by the RCPCH project board. These relate to usability of the charts. For example, the 50th centile should be de-emphasised. These and other rules are listed on the [Client Specification](../integrator/client-specification.md).

Given the complexity, we decided to create a React component library for developers to use. We designed it to be customisable for direct use, but also as a demonstration for developers wanting to build the charts from the ground up.

For this reason, we have produced a permissively-licensed, open-source React component, which aims to simplify the process of creating a chart from the chart data received from the API. It makes the job of drawing a vector-graphic centile chart much easier.

If you want to see how the library is implemented, we have built a full client for the RCPCHGrowth API in React, which uses this component library, and can be found [here](https://github.com/rcpch/digital-growth-charts-react-client).

### Why use React?

React is a popular UI library for Javascript. It has endured well and seems like a popular choice for developers. Importantly, unlike some other Javascript frameworks which are primarily designed for Single Page Applications, React doesn't expect to have the entire webpage to itself. It can be used as a small component in any other web page, even if the main framework being used is completely different.

!!! question "Tell us what you think"
    Let us know what you think of our design decisions, on this or any other area of the dGC Project, by chatting to us on our [dGC Forum](https://forum.rcpch.tech/) :fontawesome-brands-discourse:.

### What about other frameworks/UI libraries?

If you need us to develop a charting component in a different language or framework, we may be able to do this with you or your company. We would need to discuss the requirements and quote for this service. You should be aware that all such RCPCH-developed artefacts will also be open source. We ensure the licensing of open source components is compatible with commercial use.

!!! note "Contact us"
    To contact us for this service, email <mailto:commercial@rcpch.ac.uk>.

## Contributing and Implementing

See [Contributing](../developer/contributing.md) for information on how to get involved in the project or how to implement the digital growth charts component into a project.

You can get in touch with the primary developers to talk about the project using any of the methods on our [contact page](../about/contact.md).

## Acknowledgements

This Typescript library was built from the starter created by [Harvey Delaney](https://blog.harveydelaney.com/creating-your-own-react-component-library/)

The charts are built using [Victory Charts](https://formidable.com/open-source/victory/docs/victory-chart/) for React. We tried several chart packages for React, but we chose Victory because of their documentation and their ability to customise components.

## Licensing

This chart component software is is subject to copyright and is owned by the RCPCH, but is released under the MIT license.
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

There is important chart line rendering data bundled in the component, which subject to copyright and is owned by the RCPCH. It is specifically excluded from the MIT license mentioned above. If you wish to use this software, please [contact the RCPCH](../about/contact.md) so we can ensure you have the correct license for use. Subscribers to the Digital Growth Charts API will automatically be assigned licenses for the chart plotting data.
