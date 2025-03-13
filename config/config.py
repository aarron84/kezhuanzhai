# -*- coding: utf-8 -*-
# config.py
import os

config_dir = os.path.dirname(os.path.abspath(__file__))
app_directory = os.path.dirname(config_dir )
logging_config_path = os.path.join(config_dir, "logging_config.json")

class AppConfig:    
    app_directory = app_directory
    logging_config_path = logging_config_path


    



