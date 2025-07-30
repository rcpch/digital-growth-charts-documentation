---
title: API Reference
reviewers: Dr Marcus Baw, Dr Simon Chapman, Dr Anchit Chandran
audience: integrators, implementers, technical-architects
---
# API Reference

--8<-- "docs/_assets/_snippets/api-baseurl.md"

<script>
    window.addEventListener("message", (e) => {
        console.log(e.data);

        if(e.data && e.data.type === "swagger-ui-loaded") {
            document.getElementById("swagger-ui").height = e.data.height + 100;
        }
    });
</script>

<iframe id="swagger-ui" src="/_assets/swagger.html" style="width: 100%"></iframe>
