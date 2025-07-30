---
title: API Reference
reviewers: Dr Marcus Baw, Dr Simon Chapman, Dr Anchit Chandran
audience: integrators, implementers, technical-architects
---
# API Reference

--8<-- "docs/_assets/_snippets/api-baseurl.md"

<!-- Embeds the Swagger UI view of the API reference here -->
<link type="text/css" rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">

<div id="swagger-ui"></div>

<script id="swagger-js" src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js" charset="UTF-8"></script>

<script>
    // Workaround weird behaviour where this script executes before the ui bundle is loaded when
    // mkdocs does a client side navigation between pages
    setTimeout(() => {
        window.SwaggerUIBundle({
            url: 'https://raw.githubusercontent.com/rcpch/digital-growth-charts-server/live/openapi.json',
            dom_id: '#swagger-ui',
        });
    }, 0);
</script>
