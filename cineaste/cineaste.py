from core.config_manager.ConfigManager import ConfigManager

config = open('cineaste_template.config').read()

x = ConfigManager(config)
