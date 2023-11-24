from enum import Enum


class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2
    PENDING = 3
    CANCELLED = 4
    COMPLETED = 5


def update_user_status(user_id: int, status: Status):
    if status is Status.ACTIVE:
        print("Activating user")
    elif status is Status.INACTIVE:
        print("Inactivating user")
    # etc


update_user_status(123, Status.INACTIVE)
