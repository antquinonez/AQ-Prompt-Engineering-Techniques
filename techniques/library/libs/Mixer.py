from OrderedSet import OrderedSet
from typing import Any

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
            self.ordered_set.add(item)

    def __repr__(self) -> str:
        return f"CustomClass({self.ordered_set})"


# Usage example
mx = Mixer()
mx.add(1)
mx.add(2)
mx.add(2,2,3,4)  # This will not be added again.
print(mx)  # Output: CustomClass(OrderedSet([1, 2]))
