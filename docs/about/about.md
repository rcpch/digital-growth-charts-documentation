---
title: About the dGC
reviewers: Dr Marcus Baw, Dr Anchit Chandran
audience: all
tags:
  - Overview
---

# The RCPCH Growth Charts Project

## From MVP to global product :fontawesome-solid-earth-europe:

The RCPCH dGC project team was originally commissioned by the NHS in early 2020 to produce a Minimum Viable Product (MVP) to generate reliable results for growth data from children aged 1 year and below. The project team began work in May 2020. In development, the project developers found it was feasible and practical to extend the scope of the MVP to include children of **all** ages.

Since those early days, our platform has developed into the world's only Digital Growth Charts API, and we now provide digital growth charting functions for a wide range of customers across the world.

## Open Source :material-open-source-initiative:

For transparency, accuracy, and maximum reuse, our Growth Charts API and associated libraries are 100% open source. We welcome code reviews, feedback, issues and pull requests. [Check us out on GitHub](https://github.com/rcpch) - we're the first Royal College to have clinical code in its own GitHub organisation!

## Gold Standard :material-gold:

Working with the UK's top experts in growth monitoring, growth charts, centile and SDS calculation, and child development, we've created an API that takes away the heavy lifting of calculating child growth parameters. You get instant reliable and safe results.

The API allows the returned structured data to be displayed in a number of different ways, depending on the clinician's needs. It also allows for the data to be saved, charted, and trended within the EPR.

## Implementation toolkits :material-toolbox:

To help you implement the API, our team has built reference implementations and reusable UI components to help take the pain out of displaying an RCPCH standards-compliant Growth Chart, as well as simplifying and standardising the integration process. These tools are all **open source** and **permissively licensed** to allow code reuse in your application without affecting the Intellectual Property rights of your developed solution. For more information on licensing see [Licensing and Copyright](../legal/licensing-copyright.md).

## Videos :material-video-vintage:

We now have a series of videos explaining the Digital Growth Charts, these are now on their own page at [Videos](videos.md).

## Current Scope :fontawesome-solid-binoculars:

Currently, the specification is to provide reliable growth calculations for children in the UK for height centile, weight centile, body mass index (BMI) centile and head circumference (*'OccipitoFrontal Circumference'* or OFC) centile.

To this base specification, we added bone age, midparental heights, and specialist charts for Turner and Down syndrome.

### API Features

In addition to calculating SDS, centiles and corrected decimal ages against a child's birth date, sex and gestation, the API also offers the following features to users:

- fictional growth data on an individual child: this can be used to test and demonstrate the API.
- the raw data required for constructing the centile lines in a growth chart. This is offered either in the standard 9 centile format, or can generate custom centiles if requested.
- mid-parental height calculation.

These features are offered for all 5 growth references - UK-WHO (preterm and child references), Down syndrome (UK and US versions), Turner syndrome and WHO 2006/7.

### Chart Features

Alongside the API, RCPCH offer a charting component built to receive the results from the API. It has been built to meet the exact standards of the RCPCH Growth Chart committee and includes:

- corrected and chronological age plotting
- mid-parental height
- bone age
- event tracking
- tool tips for contextual information customisable based on user type
- zoom in/out
- life-course view
- cut/paste
- choices of RCPCH-designed themes
- customisable styling

### Supported References

- UK-WHO
- Down Syndrome (UK)
- Down Syndrome (USA) - American Academy of Pediatrics *added 2024* - **under testing**
- Turner Syndrome  
- CDC (USA) - *added 2024* - **under testing**
- WHO - *added 2024* - **under testing**

## Future Scope

We have plans to incorporate other growth references and tools to the platform in the future.

!!! info "Get involved in setting our roadmap"
    You can create GitHub Issues which can help set the agenda for the features we will develop next in the API. [See our Issues on GitHub :simple-github:](https://github.com/rcpch/digital-growth-charts-server/issues)

    You can also join our online forum community to learn more about Growth Charts and discuss the future of the API. [Join our community :simple-discourse: ](https://forum.rcpch.tech).
