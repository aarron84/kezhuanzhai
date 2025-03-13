# -*- coding: utf-8 -*-
# utils/logger.py
import  logging
import logging.config
import json
from typing import Dict,  Optional
from config import AppConfig
import logging
logging.basicConfig(level=logging.DEBUG)
class Logger:
    _is_init = False
   
    @classmethod
    def  init(cls,  config: Optional[Dict] = None):
        logging.debug(f"_is_init={cls._is_init}")
        if not cls._is_init:            
            try:
                config_file = AppConfig.logging_config_path    

                if config_file:              
                    with open(config_file,  'r') as f:                    
                        config = json.load(f)
                
                if config is None:
                    config = cls.default_config()            
                logging.config.dictConfig(config)
                cls._is_init = True                
            except Exception as e:
                logging.exception(e)              
    
    @classmethod
    def  default_config(cls):
        return{
           "version":1,
           "disable_existing_loggers":false,
           "formatters":{                
                "default":{
                    "format": "%(asctime)s  %(levelname)-7s  %(name)-25s %(message)s"
                }
           },
           "handlers":{
                "console":{
                    "class":"logging.StreamHandler",
                    "level":"DEBUG",
                    "formatter":"default"
                },         
           },
           "root":{
                "level":"DEBUG",
                "handlers":["console"]
           }
        }
    
    @classmethod
    def get_logger(cls, name:  str = None) -> logging.Logger:
        return logging.getLogger(name)

