import swagger from "https://esm.sh/swagger-ui-dist@5";

swagger.SwaggerUIBundle({
    url: 'https://raw.githubusercontent.com/rcpch/digital-growth-charts-server/live/openapi.json',
    dom_id: '#swagger-ui',
});