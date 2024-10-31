#!/usr/bin/env python3

"""Task 1: FIFO caching system."""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching and is a caching system
    following the First-In-First-Out (FIFO) policy.
    """

    def __init__(self):
        """Initialize the FIFOCache class."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign the item value to self.cache_data for the given key.

        If the cache exceeds the maximum number of items, the oldest
        item (first added) is removed to make space.

        Args:
            key: Key of the item to store.
            item: Item to store in the cache.
        """
        if key is None or item is None:
            return

        # Add item to cache and check for maximum cache limit
        if key in self.cache_data:
            del self.cache_data[key]  # Remove the key first to update its order
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Return the value linked to the given key in self.cache_data.

        Args:
            key: Key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key does not exist.
        """
        return self.cache_data.get(key)
