---
title: API Reference
reviewers: Dr Marcus Baw, Dr Simon Chapman, Dr Anchit Chandran
audience: integrators, implementers, technical-architects
tags:
  - API
  - API Reference
  - Integration
---
# API Reference

This page provides the interactive Swagger UI documentation for the RCPCH Digital Growth Charts API. Use this reference to explore available endpoints, request/response schemas, and to try out API calls directly.

!!! danger "Persist calculation provenance"

    Successful calculation responses identify the exact calculation-engine and API-server versions and commits that produced the result. Implementers are expected to store this complete `provenance` object unchanged with every persisted measurement result. See [Persisting API Results And Provenance](persisting-api-results.md).

--8<-- "docs/_assets/_snippets/api-baseurl.md"

<script>
    window.addEventListener("message", (e) => {
        if(e.data && e.data.type === "swagger-ui-loaded") {
            document.getElementById("swagger-ui").height = e.data.height + 100;
        }
    });
</script>

<iframe id="swagger-ui" src="/_assets/swagger.html" style="width: 100%"></iframe>
