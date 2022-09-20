from typing import Optional, Tuple
from sqlalchemy.orm import Session
from api.models.schemas import ItemCreate
from api.database.models import DbItem


class ItemsService:

    @classmethod
    def create_item_user(
            cls,
            user_id: int,
            item: ItemCreate,
            db: Session
    ) -> Tuple[Optional[DbItem], str]:

        try:

            results = DbItem(**item.dict(), owner_id=user_id)

            if not results:
                db.rollback()
                return None, 'Error'

            db.add(results)

            db.commit()

            db.refresh(results)

            return results, 'Success'

        except Exception as e:
            return None, str(e)

    @classmethod
    def get_items(
            cls,
            db: Session,
            skip: int,
            limit: int
    ):

        try:

            results = db.query(DbItem).offset(skip).limit(limit).all()

            if not results:
                return None, 'Error'

            return results, 'Success'

        except Exception as e:
            return None, str(e)
