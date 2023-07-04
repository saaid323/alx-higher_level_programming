#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            str_1 = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(str_1)
        super().__setattr__(name, value)
