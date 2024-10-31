#!/usr/bin/env python3
"""Task 3: Deletion-resilient hypermedia pagination."""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start and end indices for a given page and page size."""
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE =

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from a file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Create an indexed dataset for deletion-resilient pagination."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(dataset)}
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data."""
        assert isinstance(page, int) and isinstance(page_size, int),
        assert page > 0 and page_size > 0,

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Retrieve info about a page starting from a specific index."""
        data = self.indexed_dataset()
        assert 0 <= index < len(data),

        page_data = []
        next_index = index
        data_count = 0

        while data_count < page_size and next_index < len(data):
            item = data.get(next_index)
            if item is not None:
                page_data.append(item)
                data_count += 1
            next_index += 1

        return {
            'index': index,
            'next_index': next_index if next_index < len(data) else None,
            'page_size': len(page_data),
            'data': page_data,
        }
