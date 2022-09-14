import sys
import types
from _typeshed import Incomplete, ReadableBuffer, WriteableBuffer
from collections.abc import Callable, Hashable
from typing import Any, ClassVar, Protocol, TypeVar, overload
from typing_extensions import Literal, TypeAlias, final

_T = TypeVar("_T")

class _Allocator(Protocol):
    def __call__(self, cdecl: str | CType, init: Any = ...) -> _CDataBase: ...

FFI_CDECL: int
FFI_DEFAULT_ABI: int
RTLD_DEEPBIND: int
RTLD_GLOBAL: int
RTLD_LAZY: int
RTLD_LOCAL: int
RTLD_NODELETE: int
RTLD_NOLOAD: int
RTLD_NOW: int

@final
class CField:
    bitshift: Incomplete
    bitsize: Incomplete
    flags: Incomplete
    offset: Incomplete
    type: Incomplete

@final
class CLibrary:
    def close_lib(self, *args, **kwargs): ...
    def load_function(self, *args, **kwargs): ...
    def read_variable(self, *args, **kwargs): ...
    def write_variable(self, *args, **kwargs): ...

@final
class CType:
    abi: Incomplete
    args: Incomplete
    cname: Incomplete
    elements: Incomplete
    ellipsis: Incomplete
    fields: Incomplete
    item: Incomplete
    kind: Incomplete
    length: Incomplete
    relements: Incomplete
    result: Incomplete
    def __dir__(self): ...

class FFI:
    CData: TypeAlias = _CDataBase
    CType: TypeAlias = CType
    buffer: TypeAlias = buffer

    class error(Exception): ...
    NULL: ClassVar[CData] = ...
    RTLD_DEEPBIND: ClassVar[int] = ...
    RTLD_GLOBAL: ClassVar[int] = ...
    RTLD_LAZY: ClassVar[int] = ...
    RTLD_LOCAL: ClassVar[int] = ...
    RTLD_NODELETE: ClassVar[int] = ...
    RTLD_NOLOAD: ClassVar[int] = ...
    RTLD_NOW: ClassVar[int] = ...

    errno: int

    def __init__(
        self,
        module_name: str = ...,
        _version: int = ...,
        _types: str = ...,
        _globals: tuple[str | int, ...] = ...,
        _struct_unions: tuple[tuple[str, ...], ...] = ...,
        _enums: tuple[str, ...] = ...,
        _typenames: tuple[str] = ...,
        _includes: tuple[FFI, ...] = ...,
    ) -> None: ...
    @overload
    def addressof(self, __cdata: CData, *field_or_index: str | int) -> CData: ...
    @overload
    def addressof(self, __library: Lib, __name: str) -> CData: ...
    def alignof(self, __cdecl: str | CType | CData) -> int: ...
    @overload
    def callback(
        self,
        cdecl: str | CType,
        python_callable: None = ...,
        error: Any = ...,
        onerror: Callable[[Exception, Any, Any], None] | None = ...,
    ) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
    @overload
    def callback(
        self,
        cdecl: str | CType,
        python_callable: Callable[..., _T],
        error: Any = ...,
        onerror: Callable[[Exception, Any, Any], None] | None = ...,
    ) -> Callable[..., _T]: ...
    def cast(self, cdecl: str | CType, value: CData) -> CData: ...
    def def_extern(
        self, name: str = ..., error: Any = ..., onerror: Callable[[Exception, Any, types.TracebackType], Any] = ...
    ) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
    def dlclose(self, __lib: Lib) -> None: ...
    if sys.platform == "win32":
        def dlopen(self, __libpath: str | CData, __flags: int = ...) -> Lib: ...
    else:
        def dlopen(self, __libpath: str | CData | None = ..., __flags: int = ...) -> Lib: ...

    @overload
    def from_buffer(self, cdecl: ReadableBuffer, require_writable: Literal[False] = ...) -> CData: ...
    @overload
    def from_buffer(self, cdecl: WriteableBuffer, require_writable: Literal[True]) -> CData: ...
    @overload
    def from_buffer(self, cdecl: str | CType, python_buffer: ReadableBuffer, require_writable: Literal[False] = ...) -> CData: ...
    @overload
    def from_buffer(self, cdecl: str | CType, python_buffer: WriteableBuffer, require_writable: Literal[True]) -> CData: ...
    def from_handle(self, __x: CData) -> Any: ...
    @overload
    def gc(self, cdata: CData, destructor: Callable[[CData], Any], size: int = ...) -> CData: ...
    @overload
    def gc(self, cdata: CData, destructor: None, size: int = ...) -> None: ...
    def getctype(self, cdecl: str | CType, replace_with: str = ...) -> str: ...
    if sys.platform == "win32":
        def getwinerror(self, code: int = ...) -> tuple[int, str]: ...

    def init_once(self, func: Callable[[], Any], tag: Hashable) -> Any: ...
    def integer_const(self, name: str) -> int: ...
    def list_types(self) -> tuple[list[str], list[str], list[str]]: ...
    def memmove(self, dest: CData | WriteableBuffer, src: CData | ReadableBuffer, n: int) -> None: ...
    def new(self, cdecl: str | CType, init: Any = ...) -> CData: ...
    @overload
    def new_allocator(self, alloc: None = ..., free: None = ..., should_clear_after_alloc: bool = ...) -> _Allocator: ...
    @overload
    def new_allocator(
        self, alloc: Callable[[int], CData], free: None = ..., should_clear_after_alloc: bool = ...
    ) -> _Allocator: ...
    @overload
    def new_allocator(
        self, alloc: Callable[[int], CData], free: Callable[[CData], Any], should_clear_after_alloc: bool = ...
    ) -> _Allocator: ...
    def new_handle(self, __x: Any) -> CData: ...
    def offsetof(self, __cdecl: str | CType, __field_or_index: str | int, *__fields_or_indexes: str | int) -> int: ...
    def release(self, __cdata: CData) -> None: ...
    def sizeof(self, __cdecl: str | CType | CData) -> int: ...
    def string(self, cdata: CData, maxlen: int) -> bytes | str: ...
    def typeof(self, cdecl: str | CData) -> CType: ...
    def unpack(self, cdata: CData, length: int) -> bytes | str | list[Any]: ...

@final
class Lib:
    def __delattr__(self, name): ...
    def __dir__(self): ...
    def __setattr__(self, name, value): ...

@final
class _CDataBase:
    __name__: ClassVar[str] = ...
    def __add__(self, other): ...
    def __bool__(self): ...
    def __call__(self, *args, **kwargs): ...
    def __complex__(self): ...
    def __delattr__(self, name): ...
    def __delitem__(self, other): ...
    def __dir__(self): ...
    def __enter__(self): ...
    def __eq__(self, other): ...
    def __exit__(self, type, value, traceback): ...
    def __float__(self): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __int__(self): ...
    def __iter__(self): ...
    def __le__(self, other): ...
    def __len__(self): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...
    def __radd__(self, other): ...
    def __rsub__(self, other): ...
    def __setattr__(self, name, value): ...
    def __setitem__(self, index, object): ...
    def __sub__(self, other): ...

@final  # type: ignore[misc]
class __CDataFromBuf(_CDataBase): ...

@final  # type: ignore[misc]
class __CDataGCP(_CDataBase):
    def __del__(self, *args, **kwargs): ...

@final  # type: ignore[misc]
class __CDataOwn(_CDataBase):
    def __delitem__(self, other): ...
    def __getitem__(self, index): ...
    def __len__(self): ...
    def __setitem__(self, index, object): ...

@final  # type: ignore[misc]
class __CDataOwnGC(__CDataOwn): ...

@final
class __CData_iterator:
    def __iter__(self): ...
    def __next__(self): ...

@final
class __FFIGlobSupport: ...

@final
class buffer:
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __init__(self, *args, **kwargs) -> None: ...
    def __delitem__(self, other): ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __len__(self): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...
    def __setitem__(self, index, object): ...

def alignof(__cdecl: CType) -> int: ...
def callback(
    __cdecl: CType,
    __python_callable: Callable[..., _T],
    __error: Any = ...,
    __onerror: Callable[[Exception, Any, Any], None] | None = ...,
) -> Callable[..., _T]: ...
def cast(self, __cdecl: CType, __value: _CDataBase) -> _CDataBase: ...
def complete_struct_or_union(
    __cdecl: CType,
    __fields: list[tuple[str, CType, int, int]],
    __ignored: Any,
    __total_size: int,
    __total_alignment: int,
    __sflags: int,
    __pack: int,
) -> None: ...
@overload
def from_buffer(__cdecl: CType, __python_buffer: ReadableBuffer, require_writable: Literal[False] = ...) -> _CDataBase: ...
@overload
def from_buffer(__cdecl: CType, __python_buffer: WriteableBuffer, require_writable: Literal[True]) -> _CDataBase: ...
def from_handle(__x: _CDataBase) -> Any: ...
@overload
def gcp(cdata: _CDataBase, destructor: Callable[[_CDataBase], Any], size: int = ...) -> _CDataBase: ...
@overload
def gcp(cdata: _CDataBase, destructor: None, size: int = ...) -> None: ...
def get_errno() -> int: ...
def getcname(__cdecl: CType, __replace_with: str) -> str: ...

if sys.platform == "win32":
    def getwinerror(code: int = ...) -> tuple[int, str]: ...

if sys.platform == "win32":
    def load_library(__libpath: str | _CDataBase, __flags: int = ...) -> CLibrary: ...

else:
    def load_library(__libpath: str | _CDataBase | None = ..., __flags: int = ...) -> CLibrary: ...

def memmove(dest: _CDataBase | WriteableBuffer, src: _CDataBase | ReadableBuffer, n: int) -> None: ...
def new_array_type(__cdecl: CType, __length: int | None) -> CType: ...
def new_enum_type(__name: str, __enumerators: tuple[str], __enumvalues: tuple[Any], __basetype: CType) -> CType: ...
def new_function_type(__args: tuple[CType], __result: CType, __ellipsis: int, __abi: int) -> CType: ...
def new_pointer_type(__cdecl: CType) -> CType: ...
def new_primitive_type(__name: str) -> CType: ...
def new_struct_type(__name: str) -> CType: ...
def new_union_type(__name: str) -> CType: ...
def new_void_type() -> CType: ...
def newp(__cdecl: CType, __init: Any = ...) -> _CDataBase: ...
def newp_handle(__cdecl: CType, __x: Any) -> _CDataBase: ...
def rawaddressof(__cdecl: CType, __cdata: _CDataBase, __offset: int) -> _CDataBase: ...
def release(__cdata: _CDataBase) -> None: ...
def set_errno(__errno: int) -> None: ...
def sizeof(__cdecl: CType | _CDataBase) -> int: ...
def string(cdata: _CDataBase, maxlen: int) -> bytes | str: ...
def typeof(__cdata: _CDataBase) -> CType: ...
def typeoffsetof(__cdecl: CType, __fieldname: str | int, __following: bool) -> tuple[CType, int]: ...
def unpack(cdata: _CDataBase, length: int) -> bytes | str | list[Any]: ...
