from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response

class Error_handler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return Response(content=str(e), status_code=500)