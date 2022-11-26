from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)


@router.get("")
def get_items():
    return {
        "data": [
            {
                "id": 1,
                "value": "cookies",
            },
            {
                "id": 2,
                "value": "candies",
            },
            {
                "id": 3,
                "value": "chocolates",
            },
        ]
    }


@router.get("/{item_id}")
def get_item(item_id: int):
    return {
        "item": {"id": item_id},
    }


@router.post("")
def create_item(data: dict):
    return {
        "item": data,
    }
