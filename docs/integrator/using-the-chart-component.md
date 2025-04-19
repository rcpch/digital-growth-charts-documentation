---
title: Using the chart component
reviewers: Dr Simon Chapman
audience: integrators, implementers, technical-architects
---

## Installing the chart component

The API and the charting component have been build to work together, but stand separately. The API returns centiles and SDS against measurements as a structure JSON `Measurement` object. Most users want to chart these.

The chart component is written in typescript and react and accepts the RCPCH digital growth chartsAPI response as a prop. There is a [`storybook` instance](https://live--6732292d6f3624b0036f84b4.chromatic.com/) an [interactive demonstration](https://growth.rcpch.ac.uk/)

There is list of [features](https://growth.rcpch.ac.uk/products/react-component/#why-a-chart-library) for a diverse range of use cases. They can be customized to viewed by families and children, or clinicians, from health visitors and midwives, to paediatric endocrinology growth specialists.

### React

The best way to interact with the chart is to embed them in a react application. The package is hosted on [npm](https://www.npmjs.com/package/@rcpch/digital-growth-charts-react-component-library) and can be added to the dependencies in the `package.json` of your application. There is working [RCPCH Digital Growth Charts React client](https://growth.rcpch.ac.uk/) which includes a simple data entry form and chart implementation which can be used as a starter if required. The code can be found on [Github](https://github.com/rcpch/digital-growth-charts-react-client).

They are written in React 18.2 and will be periodically updated to support later versions of React as they are published.

#### Versioning

The charts are versioned using the [semver](https://semver.org/) system. Documentation is published with each new release, though breaking changes are uncommon. Note users will need to update and rebuild their application as and when new releases are published.

#### Styling

The charts are deliberately shipped in monochrome theme. In addition to this there are 4 themes offered by RCPCH (Traditional, Tanner 1, Tanner 2, Tanner 3), but custom styles can be applied to the base monochrome theme to alter most aspects of the look and feel. There is extensive documentation in the [Storybook docs](https://live--6732292d6f3624b0036f84b4.chromatic.com/?path=/docs/rcpchchart--docs) on which props the charts accept and how to wire the charts up to your React project.

### What if I can't use React?

It is common in healthcare environments not to be able to use frameworks like React. For this reason RCPCH have published the charts on [jsdeliver](https://www.jsdelivr.com/package/npm/@rcpch/digital-growth-charts-react-component-library). This allows implementers to import the javascript in the head tag of their page. This gives access the `RCPCHGrowthCharts` wrapper which accepts all the props detailed above for instantiating a single chart, as well as the id of the div in the DOM where the charts are to be located, within the `render` attribute.

```html
<!doctype html>
<html>
    <head>
        <title>Growth Chart Example</title>
    </head>
    <body>
        <div id="growth-chart-container"></div> <!--- The charts will appear here -->
        <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
        <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@rcpch/digital-growth-charts-react-component-library@latest/build/umd/rcpch-digital-growth-charts.umd.js"  integrity="sha384-Te61Ux4WqUzrwMJb8pDAtE92B3sYPlsR31W91KLAA6geskluSC40Z+wT14We0ngF" defer></script> <!--- Note the order of the imports: React must be version 18, and come before the library -->
        <script>
            window.onload = function () {
                const demoMeasurements = [ /* RCPCH digital growth charts API response goes here. Note must be associated with one of height, weight, ofc or bmi */];
                window.RCPCHGrowthCharts.render({
                    targetElementId: 'growth-chart-container', /* the id of the div you intend the charts to appear */
                    title: 'Demo UK-WHO Growth Chart for Children',
                    measurementMethod: 'height',
                    reference: 'uk-who',
                    sex: 'female',
                    measurements: { height: demoMeasurements },
                    midParentalHeightData: {},
                    enableZoom: false,
                    chartType: 'centile',
                    enableExport: false,
                    exportChartCallback: {},
                    clinicianFocus: false,
                    theme: 'tanner3',
                    height: 800,
                    width: 800,
                });
            };
        </script>
    </body>
</html>
```

For security reasons you may wish to include the SRI (Subresource Integrity) as above. This can be found at [https://cdn.jsdelivr.net/npm/@rcpch/digital-growth-charts-react-component-library@7.3.3/build/umd/sri-hash.txt]('https://cdn.jsdelivr.net/npm/@rcpch/digital-growth-charts-react-component-library@7.3.3/build/umd/sri-hash.txt')