STATUS_ACTIVE = 1
STATUS_INACTIVE = 2
STATUS_PENDING = 3
STATUS_CANCELLED = 4
STATUS_COMPLETED = 5


def update_user_status(user_id: int, status: int):
    if status == STATUS_ACTIVE:
        print("Activating user")
    elif status == STATUS_INACTIVE:
        print("Inactivating user")
    # etc


update_user_status(123, STATUS_ACTIVE)
