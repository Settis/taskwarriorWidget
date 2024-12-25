from tw.status import Status, Type

STATUSES = [
    Status(Type.ERROR, 0),
    Status(Type.OVERDUE, 999),
    Status(Type.OVERDUE, 45),
    Status(Type.OVERDUE, 2),
    Status(Type.TODAY, 254),
    Status(Type.TODAY, 70),
    Status(Type.TODAY, 1),
    Status(Type.WEEK, 333),
    Status(Type.WEEK, 84),
    Status(Type.WEEK, 6),
    Status(Type.REVIEW, 657),
    Status(Type.REVIEW, 38),
    Status(Type.REVIEW, 4),
    Status(Type.OK, 0)
]

class StatusGetter:
    def __init__(self):
        self.i = 0

    def get_status(self) -> Status:
        self.i = (self.i + 1) % len(STATUSES)
        return STATUSES[self.i]
