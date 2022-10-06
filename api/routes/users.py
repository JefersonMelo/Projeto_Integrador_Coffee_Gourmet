from typing import Optional
from fastapi import HTTPException

from ..utilities.users_utility import UsersUtility
from ..schemas.user_schema import UserCreate, UserLogin
from fastapi import APIRouter

router = APIRouter()


@router.post('/create/user/')
async def create_user(user: Optional[UserCreate] = None):
    msg = None
    try:
        users = UsersUtility()

        results, msg = users.create_user_email(
            user=user
        )

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'detail': results, 'message': msg}

    except Exception:
        raise HTTPException(status_code=400, detail=msg)


@router.get('/user/id/{user_id}')
async def get_user(user_id: int):
    msg = None
    try:
        users = UsersUtility()

        results, msg = users.get_user(user_id=user_id)

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'detail': results, 'message': msg}

    except Exception:
        raise HTTPException(status_code=400, detail=msg)


@router.post('/login')
async def user_login(user: Optional[UserLogin] = None):
    msg = None
    try:
        users = UsersUtility()

        results, msg = users.user_authenticate(user=user)

        if not results:
            raise HTTPException(status_code=400, detail=msg)

        return {'userid': results.id, 'username': results.name, 'token': '@coffee-token', 'msg': msg}

    except Exception:
        raise HTTPException(status_code=400, detail=msg)
