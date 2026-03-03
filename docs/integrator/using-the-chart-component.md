---
title: Using the chart component
reviewers: Dr Simon Chapman
audience: integrators, implementers, technical-architects
---

## Installing the RCPCH Digital Growth Charts React Component

The API and the charting component have been built to work together, but exist separately. The [RCPCH Digital Growth Charts API calculation endpoint](https://growth.rcpch.ac.uk/integrator/api-reference/) returns centiles and SDS against children's growth measurements in the form of a structured JSON `Measurement` object. Most users want to chart these.

The [RCPCH Digital Growth Charts React Component Library](https://github.com/rcpch/digital-growth-charts-react-component-library) is written in typescript and react and accepts the RCPCH Digital Growth Charts API response as a prop. There is a [Storybook](https://live--6732292d6f3624b0036f84b4.chromatic.com/) and an [interactive demonstration](https://growth.rcpch.ac.uk/).

The RCPCH Digital Growth Charts React Component Library has a list of [features](https://growth.rcpch.ac.uk/products/react-component/#why-a-chart-library) for a diverse range of use cases. The charts can be customized to be viewed by families and children, or by clinicians, from health visitors and midwives, to paediatric endocrinology growth specialists.

Currently the RCPCH Digital Growth Charts React Component Library do not support mobile screens. It is likely that chart visualisation will need to be reimagined for the smaller screen. This is on the RCPCH roadmap.

### React

The best way to implement the RCPCH Digital Growth Charts React Component Library is to embed it in a react application. The library is hosted on [npm](https://www.npmjs.com/package/@rcpch/digital-growth-charts-react-component-library) and can be added to the dependencies in the `package.json` of your application. There is a working [RCPCH Digital Growth Charts React client](https://growth.rcpch.ac.uk/) which includes a simple data entry form and RCPCH Digital Growth Charts React Component Library implementation which can be used as a starter if required. The client calls the API and passes the response into the RCPCH Digital Growth Charts React Component Library for charting. The code can be found on [Github](https://github.com/rcpch/digital-growth-charts-react-client).

The RCPCH Digital Growth Charts React Component Library is written in [React 18.2](https://18.react.dev/) and will be periodically updated to support later versions of React as they are published.

#### Versioning

The charts are versioned using the [semver](https://semver.org/) system. Documentation is published with each new release, though breaking changes are uncommon. Note users will need to update and rebuild their application as and when new releases are published.

#### Styling

The charts are deliberately shipped with a monochrome theme. In addition to this RCPCH offer four other themes (Traditional, Tanner 1, Tanner 2, Tanner 3), but custom styles can be applied to the base monochrome theme to alter most aspects of the look and feel.  There is extensive documentation in the [Storybook docs](https://live--6732292d6f3624b0036f84b4.chromatic.com/?path=/docs/rcpchchart--docs) on which props the charts accept and how to wire the charts up to your React project.

Note that the RCPCH logo and chart version appears by default in the top left hand corner. For implementers who prefer less prominence of the logo, an RCPCH acknowledgement statement can be used instead at the foot of the chart using the `logoVariant` prop.

##### Theme Builder 🎨 - NEW IN 2025

For those who want to customize the chart, the style props can be overridden if the `custom` theme option is selected. This exposes a variety of styles, from font and colour to line and background colour. Use the Storybook Theme Builder to customize the elements you need and click to save the settings object to the clipboard to be attached to the `customThemeStyles` prop. <br/>
![theme-builder](../_assets/_images/theme-builder.png)

### What if I can't use React?

It is common in healthcare environments not to be able to use frameworks like React. For this reason RCPCH have published the charts on [jsdeliver](https://www.jsdelivr.com/package/npm/@rcpch/digital-growth-charts-react-component-library) and [unpkg](https://unpkg.com/@rcpch/digital-growth-charts-react-component-library@latest/build/rcpch-digital-growth-charts.umd.js). This allows implementers to import the javascript in the head tag of their page. This gives access to the `RCPCHGrowthCharts` wrapper which accepts all the props detailed above for instantiating a single chart, as well as the id of the div in the DOM where the charts are to be located, within the `render` attribute.

```html
<!doctype html>
<html>
    <head>
        <title>Growth Chart Example</title>
        <!-- React dependencies. Must come first -->
        <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js" defer></script>
        <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" defer></script>
        <!-- RCPCH Growth Charts library -->
        <!-- You must use the integrity check to ensure you are using the expected code as this component   -->
        <!-- can render patient data. You can get the value from this file, adjusting the version as needed -->
        <!-- https://cdn.jsdelivr.net/npm/@rcpch/digital-growth-charts-react-component-library@7.5.0/build/sri-hash.txt -->
        <script 
            src="https://cdn.jsdelivr.net/npm/@rcpch/digital-growth-charts-react-component-library@7.5.0/build/rcpch-digital-growth-charts.umd.min.js" 
            integrity="sha384-yu1MIbRclkM3UCyciRAULihnERx26NqFKjP/EuddYVumiom3Oy5p9KBGSUHABc8g" 
            crossorigin="anonymous"
            defer>
        </script>
        <script defer>
            document.addEventListener('DOMContentLoaded', function () {
                const demoMeasurements = [ /* RCPCH digital growth charts API response goes here */ ];
                window.RCPCHGrowthCharts.render({
                    targetElementId: 'growth-chart-container',
                    title: 'Demo UK-WHO Growth Chart for Children',
                    measurementMethod: 'height',
                    reference: 'uk-who',
                    sex: 'female',
                    measurements: { height: demoMeasurements },
                    midParentalHeightData: {},
                    enableZoom: false,
                    chartType: 'centile',
                    enableExport: false,
                    clinicianFocus: false,
                    theme: 'tanner3',
                    height: 800,
                    width: 800,
                });
            });
        </script>
    </head>
    <body>
        <div id="growth-chart-container"></div> <!-- The charts will appear here -->
    </body>
</html>
```
