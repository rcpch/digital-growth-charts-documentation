!!! warning "API baseURL"

    For all API calls to the Growth Charts API, you should use the baseURL
    ```
    https://api.rcpch.ac.uk/growth/v1
    ```

    * **path**: Our API path naming policy (`growth`) is designed to allow the same baseUrl to be used for other APIs in the future.
    
    * **versioning**: We have versioned the API `v1` to allow for future versions to be developed without interfering with existing integrations.

    * **relative**: All API requests should be made to this URL, and the endpoints described in the API definition are relative to this base URL.

    * **authentication**: The API will return Unauthorized or Not Found (4xx) responses if the request does not include a valid API key.