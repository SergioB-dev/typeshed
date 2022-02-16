from _typeshed import Self
from collections.abc import Iterator, MutableMapping
from dbm import _TFlags
from types import TracebackType
from typing import TypeVar, overload

_T = TypeVar("_T")
_VT = TypeVar("_VT")

class Shelf(MutableMapping[str, _VT]):
    def __init__(
        self, dict: MutableMapping[bytes, bytes], protocol: int | None = ..., writeback: bool = ..., keyencoding: str = ...
    ) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    @overload
    def get(self, key: str) -> _VT | None: ...
    @overload
    def get(self, key: str, default: _T) -> _VT | _T: ...
    def __getitem__(self, key: str) -> _VT: ...
    def __setitem__(self, key: str, value: _VT) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __contains__(self, key: str) -> bool: ...  # type: ignore[override]
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def close(self) -> None: ...
    def sync(self) -> None: ...

class BsdDbShelf(Shelf[_VT]):
    def set_location(self, key: str) -> tuple[str, _VT]: ...
    def next(self) -> tuple[str, _VT]: ...
    def previous(self) -> tuple[str, _VT]: ...
    def first(self) -> tuple[str, _VT]: ...
    def last(self) -> tuple[str, _VT]: ...

class DbfilenameShelf(Shelf[_VT]):
    def __init__(self, filename: str, flag: _TFlags = ..., protocol: int | None = ..., writeback: bool = ...) -> None: ...

def open(filename: str, flag: _TFlags = ..., protocol: int | None = ..., writeback: bool = ...) -> Shelf[object]: ...
