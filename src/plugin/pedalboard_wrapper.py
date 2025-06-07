from .wrapper import plugin_wrapper
import pedalboard

class pedalboard_wrapper(plugin_wrapper):
    def __init__(self, plugin_name):
        """
        Initialize the pedalboard wrapper with the plugin name.

        Args:
            plugin_name (str): The name of the plugin to wrap.
        """
        self.plugin_name = plugin_name
        # Additional initialization logic can go here
        print(f"Initialized pedalboard wrapper for plugin: {self.plugin_name}")
        # Load the plugin using the plugin_wrapper base class
        self._plugin = pedalboard.load_plugin(self.plugin_name)
        
    def is_instrument(self):
        """
        Check if the wrapped plugin is an instrument.

        Returns:
            bool: True if the plugin is an instrument, False otherwise.
        """
        # Assuming pedalboard plugins have an 'is_instrument' attribute
        return self._plugin.is_instrument()
