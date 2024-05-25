import hashlib

from django.utils.inspect import func_supports_parameter

if func_supports_parameter(hashlib.md5, "usedforsecurity"):
    md5 = hashlib.md5
    new_hash = hashlib.new
else:

    def md5(data=b"", *, usedforsecurity=True):
        return hashlib.md5(data)
