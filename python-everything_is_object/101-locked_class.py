#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
"""Doesn't allow the creation of other attributes"""


    __slots__ = ["first_name"]
