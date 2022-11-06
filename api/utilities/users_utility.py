from typing import Optional, Tuple, List
from api.database.connection import get_session
from api.schemas.user_schema import UserCreate, User, UserBase, UserLogin
from api.services.users_service import UsersService


class UsersUtility:

    def __init__(self):
        self.users = UsersService()
        self.session_maker = get_session

    def create_user_email(
            self,
            user: UserCreate
    ) -> Tuple[Optional[UserCreate], str]:

        try:
            with self.session_maker() as session:

                results, msg = self.users.get_user_by_email(
                    email=user.UserEmail,
                    db=session
                )

                if results:
                    return None, 'Este Email Consta Na Nossa Base De Usuários. Cadastre-Se Com Outro Email'

                results, msg = self.users.create_user(
                    user=user,
                    db=session
                )

                if not results:
                    session.rollback()
                    return None, msg

                session.expunge(results)

                return results, msg

        except Exception as e:
            raise ConnectionError(str(e))

    def get_user(
            self,
            user_id: int
    ) -> Tuple[Optional[User], str]:

        try:
            with self.session_maker() as session:

                results, msg = self.users.get_user_id(
                    user_id=user_id,
                    db=session
                )

                if not results:
                    session.rollback()
                    return None, msg

                session.expunge_all()

                return results, msg

        except Exception as e:
            raise ConnectionError(str(e))

    def user_authenticate(
            self,
            user: UserLogin
    ) -> Tuple[Optional[User], str]:

        try:
            with self.session_maker() as session:

                results, msg = self.users.get_user_for_auth(
                    user=user,
                    db=session
                )

                if not results:
                    session.rollback()
                    return None, msg

                session.expunge_all()

                return results, msg

        except Exception as e:
            raise ConnectionError(str(e))

    def get_all_users(
            self,
            skip: int,
            limit: int
    ) -> Tuple[Optional[UserBase], str]:

        try:
            with self.session_maker() as session:

                results, msg = self.users.get_users(
                    skip=skip,
                    limit=limit,
                    db=session
                )

                if not results:
                    session.rollback()
                    return None, msg

                session.expunge_all()

                return results, msg

        except Exception as e:
            raise ConnectionError(str(e))

    # def get_contacts_address_by_user_id(
    #         self,
    #         user_id: int
    # ) -> Tuple[Optional[List[User]], str]:
    #
    #     try:
    #         with self.session_maker() as session:
    #
    #             results, msg = self.users.select_contacts_address_by_user_id(
    #                 user_id=user_id,
    #                 db=session
    #             )
    #
    #             if not results:
    #                 session.rollback()
    #                 return None, msg
    #
    #             session.expunge_all()
    #
    #             return results, msg
    #
    #     except Exception as e:
    #         raise ConnectionError(str(e))
