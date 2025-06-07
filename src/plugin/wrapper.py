
class plugin_wrappers:
    pedalboard = 'pedalboard'


class plugin_wrapper:
    pass


# one or more plugins
class plugin_chain:
    def __init__(self, plugins):
        """
        Initialize the plugin chain with a list of plugins.
        
        Args:
            plugins (plugin | list): A plugin or list of plugins .
        """
        if isinstance(plugins, list):
            self.plugins = plugins
        elif isinstance(plugins, plugin_wrapper):
            self.plugins = [plugins]
        else:
            self.plugins = []


    def get_size(self):
        """
        Get the number of plugins in the chain.
        
        Returns:
            int: The number of plugins in the chain.
        """
        return len(self.plugins)
    

    def first_plugin_is_instrument(self):
        """
        Check if the first plugin in the chain is an instrument.
        
        Returns:
            bool: True if the first plugin is an instrument, False otherwise.
        """
        if len(self.plugins) > 0:
            return self.plugins[0].is_instrument()

        return False

    

    def get_plugin(self, index):
        """
        Get a plugin by its name from the chain.
        
        Args:
            index (str): The name of the plugin to retrieve.
        
        Returns:
            object: The plugin instance if found, None otherwise.
        """
        if index >= 0 or index < len(self.plugins):
            return self.plugins[index]
        else:
            return None