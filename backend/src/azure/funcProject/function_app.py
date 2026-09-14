import azure.functions as func
import datetime
import json
import logging

from fastapi import Request
from fastapi.responses import Response
from fastapi_app import app as fastapi_app
from azure.functions._http_asgi import AsgiMiddleware


function_app = func.FunctionApp()

#Create ASGI middleware to connect Azure Function to FastAPI
asgi_middleware = AsgiMiddleware(fastapi_app)

## Route all HTTP traffic to FastAPI
@function_app.route(route="{*routes}", auth_level=func.AuthLevel.ANONYMOUS)
async def fastapi_handler(req: func.HttpRequest) -> func.HttpResponse:
    """Proxy all HTTP traffic to FastAPI."""
    return await asgi_middleware.handle_async(req)


# ## Initial function to test the Azure Function App
# app = func.FunctionApp()

# @app.route(route="MyHttpFunction", auth_level=func.AuthLevel.ANONYMOUS)
# def MyHttpFunction(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )