---
title: React Chart Component
reviewers: Dr Marcus Baw, Dr Simon Chapman, Dr Anchit Chandran
audience: developers
---

## Getting started

```console
npm i --save @rcpch/digital-growth-charts-react-component-library
```

### Circular import errors

Victory Charts are a dependency (see below), built on top of D3.js. On build, it is likely you will get an error relating to circular dependencies for some files in the d3-interpolate module. This issue is logged [here](https://github.com/d3/d3-interpolate/issues/58).

### Build error

v7.0.0 uses Rollup 4.11, and has the following build script in `package.json`: `"build": "ROLLUP_WATCH=false rollup -c --bundleConfigAsCjs",`
If users are using later versions, this has has changed and should be `“build”: “ROLLUP -w -c --bundleConfigAsCjs”,` (thanks to Caroline Kirkhope at System C for noticing this)

### Running the Charts Package locally

To run the package locally alongside the React client, there are some extra steps. Since the Chart library and the React client both use React, the Charts will throw an error if you import them in the ```package.json``` of your app from a folder on your local machine.

To develop the charts you can use Storybook:
`npm run storybook`

or to run the client and charts together:

1. in the root of the chart library: `npm link`
2. in the root of the client: `npm link @rcpch/digital-growth-charts-react-component-library`
3. Note that you need to be running the same version of node (>=20) in both consoles for this symlink to work
4. If you get a 'hooks error' on running the client, delete react and react-dom from the node_modules folder in the library. Note you will need to reinstall it if you later run storybook.
5. For changes to appear in the client, in the library console: `npm run build`

## Structure

This library has been written in Typescript. The main component is `<RCPCHChart>`: this returns the whole chart (either centiles or SDS), including toggle buttons. It takes the following `props`. Note that each component will only render a single chart type instance, so if you wanted to render a weight *and* a height chart, these must be done as two separate instances of the component.

### RCPCH Digital Growth Charts React Component Library

Documentation for this has moved into the [Storybook](https://live--6732292d6f3624b0036f84b4.chromatic.com/?path=/docs/rcpchchart--docs)

The RCPCH Digital Growth Charts React Component Library supports both Centile Charts and SDS Charts. Each chart is created on instantiation for the `<RCPCHChart />` component with the relevant props. Note that there needs to be a single instance of the component for each chart rendered - for example, if height and weight charts are requested, two instances of the component are required.

More detail on props, particularly for themes or individual styles, is found in the Storybook docs. RCPCH provide 4 supported themes that include the traditional pink and blue charts, a monochrome theme as well as themes in line with RCPCH colours. For those who have more specific requirements, a custom theme is also provided where developers can override individual styles.

To support this, a [Theme Builder](https://live--6732292d6f3624b0036f84b4.chromatic.com/?path=/story/rcpchchart--theme-builder) is provided to generate the necessary style props.

!!! example "Requests for additional functionality in props"
    In time, more props can be added if users request them. If you have requests, please post issues on our [GitHub](https://github.com/rcpch/digital-growth-charts-react-component-library/issues) or get involved to contribute as below.

#### What if I can't use React?

Colleagues in health care environments are often not easily able to use React. A further option offered is to import React, React-Dom and the RCPCH Digital Growth Charts React Component Library in the head tag from a CDN.

This is addressed [here](https://growth.rcpch.ac.uk/integrator/using-the-chart-component/#what-if-i-cant-use-react)

### Mid-Parental Height

`midParentalHeightData`: This is the return value from the RCPCH API and takes the structure:

??? note "`midParentalHeightData`"
    ```js
    export interface MidParentalHeightObject {
        mid_parental_height?: number;
        mid_parental_height_sds?: number;
        mid_parental_height_centile?: number;
        mid_parental_height_centile_data?: Reference[]
        mid_parental_height_upper_centile_data?: Reference[]
        mid_parental_height_lower_centile_data?: Reference[]
        mid_parental_height_lower_value?: number
        mid_parental_height_upper_value?: number
    }
    ```

This returns a mid-parental height, mid-parental SDS and centile, along with the centile data if the user wishes to plot a mid-parental centile. The structure of the Reference and Centile interfaces is:

??? note "`Reference` and `Centile` interface structures"
    export interface Reference {
        [name: string]: ISexChoice
    }
    export interface ICentile {
        centile: number,
        data: IPlottedCentileMeasurement[],
        sds: number
    }
    export interface IPlottedCentileMeasurement {
        "l": string | number,
        "x": number,
        "y": number
    }
    export interface ISexChoice {
        male: IMeasurementMethod,
        female: IMeasurementMethod
    }
    export interface IMeasurementMethod{
        height?: ICentile[],
        weight?: ICentile[],
        bmi?: ICentile[],
        ofc?: ICentile[],
    }

Centile data are returned from the RCPCH API in this same structure, though no API call is made from this component - all the centile data for all the references is included.
