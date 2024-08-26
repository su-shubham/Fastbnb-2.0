from fastapi import APIRouter

property = APIRouter(
    prefix="/properties",
    tags=["properties"],
)

# property.get("/property/category")
# async def get_property_category():
#     category = await collection.distinct("property_type")
