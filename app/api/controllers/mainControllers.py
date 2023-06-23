from app.api.config.db import db
import requests
import json

class BillsController():
    
    def get_json_from_url(self, json_str: str):
        try:
            # Obtener el contenido JSON de la respuesta
            json_data = json.loads(json_str)
            
            # Convertir el JSON en una cadena codificada
            encoded_json = json.dumps(json_data)
            print(encoded_json)
            # Verificar si el JSON es un objeto o una lista de documentos
            if isinstance(json_data, dict):
                # Si es un objeto, conviértelo en una lista de un solo elemento
                documentos = [encoded_json]
            elif isinstance(json_data, list):
                # Si es una lista, utiliza directamente los documentos
                documentos = [encoded_json]
            else:
                raise ValueError("El JSON no representa un objeto válido o una lista de documentos.")
            
            # Insertar los documentos en la colección de MongoDB
            db.facturas.insert_many(documentos)
            
            return {"message": "Se insertaron documentos en la base de datos."}
        
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error al realizar la solicitud HTTP: {e}")
        
        except ValueError as e:
            raise ValueError(f"Error al decodificar el JSON: {e}")
