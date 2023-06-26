from fastapi import FastAPI  # Import FastAPI module
from app.api.routes.billRoutes import bill
from app.docs import tags_metadata  # Import tags_metadata from docs package

from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware from fastapi.middleware package

 # Load environment variables from .env file

# Create an instance of the FastAPI class
app = FastAPI(
    openapi_url='/api/v1/bills/openapi.json',
    docs_url='/api/v1/bills/docs',
    title="API Bills",  # Name of the API
    description='<p>Esta API permite obtener información relacionada con los códigos de departamentos y municipios de Colombia. <br> Proporciona endpoints para consultar regiones, municipios y departamentos utilizando diferentes criterios.</p>',  # Description of the API
    version="0.0.1",  # Version of the API
)

# Set the allowed origins for CORS requests
origins = ['*']

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Register the endpoints for each route
app.include_router(bill, prefix='/api/v1/bills')  # Register the endpoints for user management