from app.api.config.db import db
import requests
from urllib.parse import unquote
import json

class BillsController():
    
    def get_json_from_url(self, url: str):
        try:
            # Decodificar la URL
            decoded_url = unquote(url)
            
            response = requests.get(decoded_url)
            response.raise_for_status()
            
            # Obtener el contenido JSON de la respuesta
            json_data = response.json()
            
            # Verificar si el JSON es un objeto o una lista de documentos
            if isinstance(json_data, dict):
                print("aca")
                # Si es un objeto, conviértelo en una lista de un solo elemento
                documentos = [json_data]
                #print(documentos)
            elif isinstance(json_data, list):
                # Si es una lista, utiliza directamente los documentos
                documentos = json_data
            else:
                raise ValueError("El JSON no representa un objeto válido o una lista de documentos.")
            
            # Inserta los documentos en la colección de MongoDB
            db.facturas.insert_many(documentos)
            
            return {"message": f"Se insertaron documentos en la base de datos."}
        
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error al realizar la solicitud HTTP: {e}")
        
        except ValueError as e:
            raise ValueError(f"Error al decodificar el JSON: {e}")
