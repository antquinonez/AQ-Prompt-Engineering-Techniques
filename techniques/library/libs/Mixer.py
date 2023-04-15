from OrderedSet import OrderedSet
from typing import Any, Iterable, Optional
import re
import PromptLogs

class Mixer:
    """
    Uses OrderedSet to store unique items in the order they were added.
    """

    def __init__(self) -> None:
        self.ordered_set = OrderedSet()
        self._iterator = iter(self.ordered_set)

    def add(self, *items: Any) -> None:
        """
        Add an item or items to the internal ordered set.
        If the item is passed as string of multiple items, it will be split by space, newline, comma and tab.

        :param items: One or more items to be added to the set.
        """
        for item in items:
            item_x = re.split(r'[ \n,\t]+', item.strip())
            for i in item_x:
                if i not in self.ordered_set:
                    self.ordered_set.add(i)
                    self._iterator = iter(self.ordered_set)
                else:
                    pass

    def remove(self, *items: Any) -> None:
        """
        Remove an item or items from the internal ordered set.

        :param items: One or more items to be removed from the set.
        """
        for item in items:
            item_x = re.split(r'[ \n,\t]+', item.strip())
            for i in item_x:
                if i in self.ordered_set:
                    self.ordered_set.remove(i)
                    self._iterator = iter(self.ordered_set)
                else:
                    pass

    def get_ordered_set(self) -> OrderedSet:
        """
        Return the internal ordered set.

        :return: The OrderedSet instance.
        """
        return self.ordered_set

    def next_item(self) -> Optional[Any]:
        """
        Return the next item from the ordered set.

        :return: The next item in the ordered set or None if there are no more items.
        """
        try:
            return next(self._iterator)
        except StopIteration:
            return None

    def __repr__(self) -> str:
        return f"CustomClass({self.ordered_set})"
