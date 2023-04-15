from OrderedSet import OrderedSet
from typing import Any
import re
   
class Mixer:
    """
    Uses OrderedSet to store unique items in the order they were added.
    """

    def __init__(self):
        self.ordered_set = OrderedSet()

    def add(self, *items: Any) -> None:
        """
        Add an item to the internal ordered set.
        
        :param item: The item to be added to the set.
        """
        for item in items:
            item_x = re.split(r'[ \n,\t]+', item.strip())
            for i in item_x:
                if i not in self.ordered_set:
                    self.ordered_set.add(i)
                else:
                    pass

    def __repr__(self) -> str:
        return f"CustomClass({self.ordered_set})"

