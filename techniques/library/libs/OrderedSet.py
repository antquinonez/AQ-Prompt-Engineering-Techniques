from collections import OrderedDict
from typing import Any, Iterable, Optional


class OrderedSet(OrderedDict):
    """
    A custom class implementing an ordered set based on the OrderedDict class.
    It maintains the insertion order of elements and prevents duplicate items.
    """

    def __init__(self, iterable: Optional[Iterable[Any]] = None):
        """
        Initialize the ordered set with an optional iterable.
        
        :param iterable: An optional iterable containing initial items for the set.
        """
        super().__init__((item, None) for item in iterable) if iterable else super().__init__()

    def add(self, item: Any) -> None:
        """
        Add an item to the ordered set if it is not already present.
        
        :param item: The item to be added to the set.
        """
        if item not in self:
            self[item] = None

    def discard(self, item: Any) -> None:
        """
        Remove an item from the ordered set if it is present.
        
        :param item: The item to be removed from the set.
        """
        self.pop(item, None)

    def __repr__(self) -> str:
        return f"OrderedSet({list(self.keys())})"