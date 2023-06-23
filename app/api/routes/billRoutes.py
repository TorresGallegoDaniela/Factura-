from fastapi import APIRouter, Request
from app.api.controllers.mainControllers import BillsController

# Create API router
bill = APIRouter()

@bill.post("/get_json")
async def get_json(request: Request):
    try:
        # Obtén los datos JSON desde la URL utilizando la función get_json_from_url
        json_data = BillsController().get_json_from_url(request)
        
        if json_data is not None:
            return {"message": f"Se obtuvieron los datos JSON desde la URL."}
        else:
            return {"message": "No se pudo obtener los datos JSON desde la URL."}
     
    except ValueError as e:
        return {"message": str(e)}