from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException

from ..schemas.provider_schema import Provider
from ..utilities.provider_utility import ProviderUtility

router = APIRouter()


@router.post('/add/new/provider')
async def create_new_provider(provider: Optional[Provider]):
    
    try:
        provider_utility = ProviderUtility()

        results, msg = provider_utility.create_new_provider(provider=provider)

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'results': results, 'detail': msg}

    except Exception as e:
        raise HTTPException(status_code=400, detail=e.detail)


@router.get('/get/all/providers')
def get_all_providers():
    
    try:
        provider_utility = ProviderUtility()

        results, msg = provider_utility.get_all_providers(skip=0, limit=100)

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'results': results, 'detail': msg}

    except Exception as e:
        raise HTTPException(status_code=400, detail=e.detail)


@router.get('/get/provider/{provider_id}')
def get_product_by_provider_id(provider_id: int):
    
    try:
        provider_utility = ProviderUtility()

        results, msg = provider_utility.get_provider_by_id(
            provider_id=provider_id
        )

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'results': results, 'detail': msg}

    except Exception as e:
        raise HTTPException(status_code=400, detail=e.detail)
