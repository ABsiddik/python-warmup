print("Here’s a single Python script that creates variables of all the common built-in types and prints their values and types:")

# Numbers
int_var = 42
float_var = 3.14
complex_var = 2 + 3j

# Boolean
bool_var = True

# Text
str_var = "welcome"

# Sequence types
list_var = [1, 2, 3]
tuple_var = (1, 2, 3)
range_var = range(5)

# Set types
set_var = {1, 2, 3}
frozenset_var = frozenset({1, 2, 3})

# Mapping type
dict_var = {"a": 1, "b": 2}

# Binary types
bytes_var = b"hello"
bytearray_var = bytearray(5)
memoryview_var = memoryview(b"hello")

# None
none_var = None

# Print all variables with their type
variables = {
    "int_var": int_var,
    "float_var": float_var,
    "complex_var": complex_var,
    "bool_var": bool_var,
    "str_var": str_var,
    "list_var": list_var,
    "tuple_var": tuple_var,
    "range_var": range_var,
    "set_var": set_var,
    "frozenset_var": frozenset_var,
    "dict_var": dict_var,
    "bytes_var": bytes_var,
    "bytearray_var": bytearray_var,
    "memoryview_var": memoryview_var,
    "none_var": none_var,
}

for name, value in variables.items():
    print(f"{name} = {value!r}, type: {type(value)}")
