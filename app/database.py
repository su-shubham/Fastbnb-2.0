import motor.motor_asyncio
from .models import BnB
from .config import settings
from typing import Any, Dict
from bson import ObjectId, Decimal128


try:
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongoDB_url)    
    collection = client.sample_airbnb
except Exception as e:
    print(e)

def serialize_document(document: Dict[str, Any]) -> Dict[str, Any]:
    serialized_doc = {}
    for key, value in document.items():
        if isinstance(value, ObjectId):
            serialized_doc[key] = str(value)
        elif isinstance(value, Decimal128):
            serialized_doc[key] = float(value.to_decimal())
        elif isinstance(value, dict):
            serialized_doc[key] = serialize_document(value)  # Recursively handle nested documents
        elif isinstance(value, list):
            serialized_doc[key] = [serialize_document(item) if isinstance(item, dict) else item for item in value]
        else:
            serialized_doc[key] = value
    return serialized_doc

async def get_data():
    response=[]
    cursor = collection.listingsAndReviews.find({'cleaning_fee':{'$exists': True}}, limit=15)
    async for data in cursor:
        response.append(
            BnB(
              data['_id'],
              data['name'], 
              data['summary'], 
              data['address']['street'], 
              str(data['price']), 
              str(data['cleaning_fee']),
              str(data['accommodates']),
              data['images']['picture_url'],
              data['amenities'],
              data['property_type']
            )
        ) 
    return response

async def get_individual_info(id:str)->dict:
    data= await collection.listingsAndReviews.find_one({'_id': id})
    response=BnB(
              data['_id'],
              data['name'], 
              data['summary'], 
              data['address']['street'], 
              str(data['price']), 
              str(data['cleaning_fee']),
              str(data['accommodates']),
              data['images']['picture_url'],
              data['amenities'],
            data['property_type']
            )
    return response

async def confirm_book(id:str)->dict:
    confirm_data= await collection.bookings.insert_one({'property': id})
    return confirm_data

async def search_data(query:str):
    search_results = collection.listingsAndReviews.find({"name": {"$regex": query,"$options":"i"}},{"name":1})
    suggestions = [doc["name"]  for doc in await search_results.to_list(length=30)]
    return suggestions