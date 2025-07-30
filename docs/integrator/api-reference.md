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

<script id="swagger-js"></script>

<script>
    // We enable instant navigation in mkdocs-material which does a client-side JS replacement of the page
    // rather than loading it fresh. It simulates reloading script tags but it does so in parallel.
    // (https://github.com/squidfunk/mkdocs-material/blob/9d958543d01ccedd0b6531f8129cfb76ef3d812a/src/templates/assets/javascripts/integrations/instant/index.ts#L222)
    // This is not the same as how the browser would load the script tags initially, blocking on the first
    // one before loading the second. The effect is that the Swagger UI loads fine if you load this page
    // directly but crashes on a client side navigation.
    // Work around this by listening to the `load` event on the swagger dist script.

    // Defining scriptTag at the top level caused an error but only in the Azure build who even knows
    // > Uncaught SyntaxError: Failed to execute 'replaceWith' on 'Element': Identifier 'scriptTag' has already been declared
    // so wrap it in an IIFE since we can't use ES modules because the same mkdocs-material instant loading
    // code strips out all attributes from script tags unless they have src
    (() => {
        const scriptTag = document.getElementById("swagger-js");

        scriptTag.addEventListener("load", () => {
            window.SwaggerUIBundle({
                url: 'https://raw.githubusercontent.com/rcpch/digital-growth-charts-server/live/openapi.json',
                dom_id: '#swagger-ui',
            });
        });

        scriptTag.src = "https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js";
    })();
</script>
