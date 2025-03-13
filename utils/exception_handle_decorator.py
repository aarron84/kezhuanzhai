# -*- coding: utf-8 -*-
# utils/exception_handle_decorator.py
from functools import wraps
from . import  appLogger
def exception_handle(func):   
    @wraps(func)
    def wrapss(*args,  **kwargs):
        try:
            result = func(*args,  **kwargs)
            return result
        except Exception as e:
            appLogger.exception(e)
    return wrapss
 
