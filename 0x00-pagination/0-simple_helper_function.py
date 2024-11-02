#!/usr/bin/env python3
"""
Simple Helper Function
"""


def index_range(page: int, page_size: int):
    """
    Return a tuple of size two containing a start index and an end index
    """
    # Calculate the offset and limit
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return(start_index, end_index)

    # if __name__ == '__main__':
