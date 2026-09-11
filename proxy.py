import os
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

TCS_BASE_URL = "https://genailab.tcs.in"

client = httpx.AsyncClient(
    verify=False,
    timeout=300.0,
)

@app.api_route(
    "/{path:path}",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
)
async def proxy(path: str, request: Request):
    body = await request.body()

    headers = dict(request.headers)

    # Don't forward the local Host header
    headers.pop("host", None)

    url = f"{TCS_BASE_URL}/{path}"

    response = await client.request(
        method=request.method,
        url=url,
        headers=headers,
        content=body,
        params=request.query_params,
    )

    excluded_headers = {
        "content-encoding",
        "content-length",
        "transfer-encoding",
        "connection",
    }

    response_headers = {
        k: v
        for k, v in response.headers.items()
        if k.lower() not in excluded_headers
    }

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=response_headers,
        media_type=response.headers.get("content-type"),
    )
