from fastapi import APIRouter, Request
from app.api.controllers.mainControllers import BillsController
from fastapi.responses import JSONResponse
from app.api.config.db import db

# Create API router
bill = APIRouter()

@bill.post("/get_json")
async def get_json(request: Request):
    try:
        # Instancia del controlador de facturas
        bills_controller = BillsController()

        # Obtén los datos JSON desde la URL utilizando la función get_json_from_url
        json_data = bills_controller.get_json_from_url(request)
        
        if json_data is not None:
            return {"message": f"Se obtuvieron los datos JSON desde la URL."}
        else:
            return {"message": "No se pudo obtener los datos JSON desde la URL."}
     
    except ValueError as e:
        return {"message": str(e)}