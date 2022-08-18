import re
from typing import List, Optional, Type

from .types import (
    Integer,
    Int8,
    Int16,
    Int32,
    Int64,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
)


def get_type(
    size: Optional[int] = None,
    signed: Optional[bool] = None,
    type_name: Optional[str] = None,
) -> Type[Integer]:
    """Get type int with specified size and signed."""
    if type_name is not None:
        match = re.match(r"(u*)int(\d+)", type_name)
        if not match:
            raise ValueError("Match type failed")

        nbits = int(match.group(2))
        if nbits % 8:
            raise ValueError("Match type failed")

        signed = not bool(match.group(1))
        size = nbits // 8

    int_types: List[Type[Integer]] = [
        Int8,
        Int16,
        Int32,
        Int64,
        UInt8,
        UInt16,
        UInt32,
        UInt64,
    ]

    for int_type in int_types:
        if int_type.get_size() == size and int_type.get_signed() == signed:
            return int_type

    raise ValueError("Match type failed")
