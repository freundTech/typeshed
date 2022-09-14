from _typeshed import Incomplete

from .error import VerificationError as VerificationError

class CffiOp:
    op: Incomplete
    arg: Incomplete
    def __init__(self, op, arg) -> None: ...
    def as_c_expr(self): ...
    def as_python_bytes(self): ...

def format_four_bytes(num): ...

OP_PRIMITIVE: int
OP_POINTER: int
OP_ARRAY: int
OP_OPEN_ARRAY: int
OP_STRUCT_UNION: int
OP_ENUM: int
OP_FUNCTION: int
OP_FUNCTION_END: int
OP_NOOP: int
OP_BITFIELD: int
OP_TYPENAME: int
OP_CPYTHON_BLTN_V: int
OP_CPYTHON_BLTN_N: int
OP_CPYTHON_BLTN_O: int
OP_CONSTANT: int
OP_CONSTANT_INT: int
OP_GLOBAL_VAR: int
OP_DLOPEN_FUNC: int
OP_DLOPEN_CONST: int
OP_GLOBAL_VAR_F: int
OP_EXTERN_PYTHON: int
PRIM_VOID: int
PRIM_BOOL: int
PRIM_CHAR: int
PRIM_SCHAR: int
PRIM_UCHAR: int
PRIM_SHORT: int
PRIM_USHORT: int
PRIM_INT: int
PRIM_UINT: int
PRIM_LONG: int
PRIM_ULONG: int
PRIM_LONGLONG: int
PRIM_ULONGLONG: int
PRIM_FLOAT: int
PRIM_DOUBLE: int
PRIM_LONGDOUBLE: int
PRIM_WCHAR: int
PRIM_INT8: int
PRIM_UINT8: int
PRIM_INT16: int
PRIM_UINT16: int
PRIM_INT32: int
PRIM_UINT32: int
PRIM_INT64: int
PRIM_UINT64: int
PRIM_INTPTR: int
PRIM_UINTPTR: int
PRIM_PTRDIFF: int
PRIM_SIZE: int
PRIM_SSIZE: int
PRIM_INT_LEAST8: int
PRIM_UINT_LEAST8: int
PRIM_INT_LEAST16: int
PRIM_UINT_LEAST16: int
PRIM_INT_LEAST32: int
PRIM_UINT_LEAST32: int
PRIM_INT_LEAST64: int
PRIM_UINT_LEAST64: int
PRIM_INT_FAST8: int
PRIM_UINT_FAST8: int
PRIM_INT_FAST16: int
PRIM_UINT_FAST16: int
PRIM_INT_FAST32: int
PRIM_UINT_FAST32: int
PRIM_INT_FAST64: int
PRIM_UINT_FAST64: int
PRIM_INTMAX: int
PRIM_UINTMAX: int
PRIM_FLOATCOMPLEX: int
PRIM_DOUBLECOMPLEX: int
PRIM_CHAR16: int
PRIM_CHAR32: int
PRIMITIVE_TO_INDEX: Incomplete
F_UNION: int
F_CHECK_FIELDS: int
F_PACKED: int
F_EXTERNAL: int
F_OPAQUE: int
G_FLAGS: Incomplete
CLASS_NAME: Incomplete
