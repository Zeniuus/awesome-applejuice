import sqlalchemy as sa
from abc import abstractmethod, ABC


metadata = sa.MetaData()

# TODO: add row_id, created_at, updated_at, deleted_at
# columns automatically for every tables.
# TODO: wrap models with API for CRUD operations.


class SimpleSerializer(ABC):
    @classmethod
    def as_dict(cls, items):
        if not isinstance(items, list):
            item = items
            if not item:
                return {}
            return cls.single_item_as_dict(item)
        if isinstance(items, list):
            if not items:
                return []
            return list(map(cls.single_item_as_dict, items))

    @classmethod
    @abstractmethod
    def single_item_as_dict(cls, item):
        pass
