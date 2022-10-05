from typing import Optional
from fastapi import HTTPException

from ..utilities.category_utility import CategoryUtility
from ..models.schemas import Category
from fastapi import APIRouter

router = APIRouter()


@router.post('/new/category')
async def add_new_category(category: Optional[Category]):
    try:
        cat_utility = CategoryUtility()

        results, msg = cat_utility.create_new_category(category)

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'detail': results, 'msg': msg}

    except Exception as e:
        msg = str(e)
        raise HTTPException(status_code=400, detail=msg)


@router.get('/get/all/categories')
def get_all_categories():
    try:
        cat_utility = CategoryUtility()

        results, msg = cat_utility.get_all_categories()

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'detail': results, 'msg': msg}

    except Exception as e:
        msg = str(e)
        raise HTTPException(status_code=400, detail=msg)


@router.get('/get/category/{category_id}')
def get_all_categories(category_id: int):
    try:
        cat_utility = CategoryUtility()

        results, msg = cat_utility.get_category_by_id(category_id=category_id)

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'detail': results, 'msg': msg}

    except Exception as e:
        msg = str(e)
        raise HTTPException(status_code=400, detail=msg)