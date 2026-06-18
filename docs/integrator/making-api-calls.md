---
title: Making API Calls
reviewers: Dr Marcus Baw, Dr Simon Chapman
audience: integrators, implementers, technical-architects
---

# Making calls to the Digital Growth Charts API

There are as many ways to make an API call as there are software developers, but here are some common ways. We'll start by using **cURL** to get you started but if you prefer a graphical tool, then feel free to skip ahead to the **Postman** section.

--8<-- "docs/_assets/_snippets/api-baseurl.md"

## cURL

`cURL` is a very simple and common tool for making web requests from the command line (also known as the 'terminal' or 'command prompt'). Official documentation for cURL can be found [here](https://everything.curl.dev).

### Installing cURL

Download cURL [here](https://curl.se/download.html). Scroll to the correction download for your Operating System.

!!! tip "Windows download, install, and usage"

    For Windows, please see [this guide](https://linuxhint.com/install-use-curl-windows/) on how to download and install cURL.

    Use the **Git Bash** command line to save headaches regarding formatting.

### Using cURL to make a test request

Copy and paste the following cURL request into your command line, inserting your `Primary key`. This example sends only the **required** parameters - that is all you need to get a centile result back. Optional parameters such as bone age and events are covered in [Optional parameters and advanced features](#optional-parameters-and-advanced-features) below. Use the tab that matches your operating system - the macOS / Linux version uses Bash quoting and `\` line continuations, while the Windows version uses Command Prompt quoting and `^` line continuations.

=== ":material-apple: :material-linux: macOS / Linux"

    ```bash hl_lines="3"
    curl --location --request POST 'https://api.rcpch.ac.uk/growth/v1/uk-who/calculation' \
    --header 'Subscription-Key: YOUR_PRIMARY_API_KEY_GOES_HERE' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "birth_date": "2020-04-12",
        "observation_date": "2028-06-12",
        "observation_value": 115,
        "sex": "female",
        "gestation_weeks": 40,
        "gestation_days": 0,
        "measurement_method": "height"
    }'
    ```

=== ":material-microsoft-windows: Windows"

    Windows **Command Prompt** and **PowerShell** do not understand Bash's `\` line continuations or single-quoted JSON, so the macOS / Linux example will fail if pasted as-is. The version below uses `^` for line continuation and escapes the inner double quotes (`\"`) so the JSON survives Command Prompt's quoting rules. cURL ships with Windows 10 and later.

    ```bat hl_lines="2"
    curl --location --request POST "https://api.rcpch.ac.uk/growth/v1/uk-who/calculation" ^
    --header "Subscription-Key: YOUR_PRIMARY_API_KEY_GOES_HERE" ^
    --header "Content-Type: application/json" ^
    --data-raw "{\"birth_date\": \"2020-04-12\", \"observation_date\": \"2028-06-12\", \"observation_value\": 115, \"sex\": \"female\", \"gestation_weeks\": 40, \"gestation_days\": 0, \"measurement_method\": \"height\"}"
    ```

    !!! tip "Using PowerShell?"
        In PowerShell, `curl` is an alias for `Invoke-WebRequest`, which has different syntax. Call `curl.exe` explicitly to use real cURL, or simply run the command in **Command Prompt** instead.

The response should be a large JSON response like the following (truncated):

```bash
{"birth_data":{"birth_date":"2020-04-12", ... :{"events_text":["Growth hormone start","Growth Hormone Deficiency diagnosis"]}}
```

!!! tip "`jq`"
    A neat tool for pretty-printing JSON in the command line is [`jq`](https://stedolan.github.io/jq/download/). With `jq` installed, you can pipe the `cURL` output to `jq` and get a much easier-to-read response:

```bash hl_lines="12"
curl --location --request POST 'https://api.rcpch.ac.uk/growth/v1/uk-who/calculation' \
--header 'Subscription-Key: YOUR_PRIMARY_API_KEY_GOES_HERE' \
--header 'Content-Type: application/json' \
--data-raw '{
    "birth_date": "2020-04-12",
    "observation_date": "2028-06-12",
    "observation_value": 115,
    "sex": "female",
    "gestation_weeks": 40,
    "gestation_days": 0,
    "measurement_method": "height"
}' | jq
```

You should get a nicely formatted JSON response object:

```bash
{
  "birth_data": {
    "birth_date": "2020-04-12",
    "gestation_weeks": 40,
... # truncated
    "events_text": [
        "Growth hormone start",
        "Growth Hormone Deficiency diagnosis"
    ]
  }
}
```

### A note about dates

The response object from the API contains dates without times in the format `YYYY-MM-DD`. This is the format that the digital growth charts react component library expects. If the output of the API is passed directly to the charts they will render the measurements automatically. RCPCH recommend that the response is persisted, so that an API call is only required for each new measurement.

If in the process of serializing or deserializing the response, the date format is changed, RCPCH advise ensuring that the dates do not change format. In case this happens, the charting component is optimized to process common date types, but will log this as a warning in the console. Any unparseable dates will log as errors.

## Optional parameters and advanced features

The test request above sends only the parameters the API needs to return a centile result:

| Required parameter   | Description                                                       |
| -------------------- | ---------------------------------------------------------------- |
| `birth_date`         | The child's date of birth (`YYYY-MM-DD`).                         |
| `observation_date`   | The date the measurement was taken (`YYYY-MM-DD`).               |
| `observation_value`  | The measurement value (e.g. height in cm, weight in kg).          |
| `sex`                | `male` or `female`.                                               |
| `gestation_weeks`    | Completed weeks of gestation at birth (use `40` for a term baby). |
| `gestation_days`     | Additional days of gestation at birth (use `0` for a term baby). |
| `measurement_method` | `height`, `weight`, `ofc` (head circumference), or `bmi`.         |

Everything else is **optional**. You do not need to send any of the following to get a valid result, and most measurements will not use them. They unlock additional features when you need them:

!!! info "Bone age"
    Bone age is a specialist radiological measurement, usually only performed for a very small minority of children seen in a growth or endocrine clinic. If you send the bone age parameters (`bone_age`, `bone_age_centile`, `bone_age_sds`, `bone_age_text`, `bone_age_type`), the API simply returns them alongside the growth data so the chart component can plot them. The API does not calculate bone age for you.

!!! info "Events"
    `events_text` lets you attach clinical annotations (for example *"Growth hormone start"*) to a measurement. The API passes these straight back in the response so the chart component can display them as event markers against the relevant point. They are purely for annotation and do not affect the centile calculation.

!!! info "Down syndrome and Turner syndrome"
    To plot against the condition-specific references, call the matching endpoint instead of `uk-who` - for example `/growth/v1/trisomy-21/calculation` or `/growth/v1/turner/calculation`. See [Turner and Down Syndrome](turner-down-syndrome.md) for details.

!!! info "Other (non-UK-WHO) references"
    The same calculation request can be sent to other reference endpoints, such as the CDC (US) reference, by changing the reference segment of the URL. The request body stays the same.

Below is the same request as before, this time including the optional bone age and events parameters:

```bash
curl --location --request POST 'https://api.rcpch.ac.uk/growth/v1/uk-who/calculation' \
--header 'Subscription-Key: YOUR_PRIMARY_API_KEY_GOES_HERE' \
--header 'Content-Type: application/json' \
--data-raw '{
    "birth_date": "2020-04-12",
    "observation_date": "2028-06-12",
    "observation_value": 115,
    "sex": "female",
    "gestation_weeks": 40,
    "gestation_days": 0,
    "measurement_method": "height",
    "bone_age": 10,
    "bone_age_centile": 98,
    "bone_age_sds": 2.0,
    "bone_age_text": "This bone age is advanced",
    "bone_age_type": "greulich-pyle",
    "events_text": ["Growth hormone start", "Growth Hormone Deficiency diagnosis"]
}'
```

## Postman :simple-postman:

Postman is a tool for API development. The RCPCH team used Postman extensively during the API development and testing process. Download Postman [here](https://learning.postman.com/docs/getting-started/installation-and-updates/).

We have produced a set of Postman Collections and Environments which can help you explore the dGC API.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/202702-d1daf1c6-3a4c-469d-be2a-e2fcf3d84090?action=collection%2Ffork&collection-url=entityId%3D202702-d1daf1c6-3a4c-469d-be2a-e2fcf3d84090%26entityType%3Dcollection%26workspaceId%3Dd868b72e-0677-4b67-9283-112363b1f5ac#?env%5BLIVE%20api.rcpch.ac.uk%5D=W3sia2V5IjoiYmFzZVVybCIsInZhbHVlIjoiaHR0cHM6Ly9hcGkucmNwY2guYWMudWsvZ3Jvd3RoL3YxIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQiLCJzZXNzaW9uVmFsdWUiOiJodHRwczovL2FwaS5yY3BjaC5hYy51ay9ncm93dGgvdjEiLCJzZXNzaW9uSW5kZXgiOjB9LHsia2V5IjoiYXBpS2V5IiwidmFsdWUiOiJJTlNFUlRfWU9VUl9BUElfS0VZX0hFUkUiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0Iiwic2Vzc2lvblZhbHVlIjoiSU5TRVJUX1lPVVJfQVBJX0tFWV9IRVJFIiwic2Vzc2lvbkluZGV4IjoxfV0=)

## openAPI3 (Swagger) API documentation :simple-swagger:

As we've specified our API documentation in the openAPI3 (formerly known as 'Swagger') format, we can auto-generate API documentation.

The Swagger API reference is [here](api-reference.md).
