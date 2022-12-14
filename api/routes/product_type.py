from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException

from ..schemas.prod_type_schema import ProductType
from ..utilities.prod_type_utility import TypeUtility

router = APIRouter()


@router.post('/add/new/product/type')
async def create_new_type(product_type: Optional[ProductType]):
    try:
        type_utility = TypeUtility()

        results, msg = type_utility.create_product_type(product_type=product_type)

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'results': results, 'detail': msg}

    except Exception as e:
        msg = str(e)
        raise HTTPException(status_code=400, detail=msg)


@router.get('/get/all/product/types')
def get_all_types():
    try:
        type_utility = TypeUtility()

        results, msg = type_utility.get_all_product_types()

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'results': results, 'detail': msg}

    except Exception as e:
        msg = str(e)
        raise HTTPException(status_code=400, detail=msg)


@router.get('/get/product/type/{product_type_id}')
def get_all_types(product_type_id: int):
    try:
        type_utility = TypeUtility()

        results, msg = type_utility.get_product_type_by_id(product_type_id=product_type_id)

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'results': results, 'detail': msg}

    except Exception as e:
        msg = str(e)
        raise HTTPException(status_code=400, detail=msg)
