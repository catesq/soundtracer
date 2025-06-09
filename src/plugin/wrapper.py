from pedalboard import Pedalboard


class plugin_wrappers:
    pedalboard = 'pedalboard'

class plugin_paramater:
    def __init__(self, name, value, index):
        """
        Initialize a plugin parameter with a name and value.
        
        Args:
            name (str): The name of the parameter.
            value (any): The value of the parameter.
        """
        self.name = name
        self.value = value
        self.index = index

    def __repr__(self):
        return f"{self.name}={self.value}"
    

class plugin_wrapper:
    def get_paramaters(self):
        """
        Get the parameters of the plugin.
        
        Returns:
            list: A list of parameters for the plugin.
        """
        return []


# paramaters counted from 0 to num_paramaters-1
class plugin_parameters:
    def __init__(self, plugin: plugin_wrapper):
        self.params = plugin.get_parameters()

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

        self.pedalboard = Pedalboard(self.plugins)


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

    def get_first_plugin_name(self):
        """
        Get the name of the first plugin in the chain.
        
        Returns:
            str: The name of the first plugin if it exists, None otherwise.
        """
        if len(self.plugins) > 0:
            return self.plugins[0].get_name()
        else:
            return None


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
        

    def process(self, input):
        """
        Process the input through the chain of plugins.
        
        Args:
            input (dict): The input to process, typically containing audio or MIDI data.
        
        Returns:
            generator: A generator yielding processed audio data.
        """
        if len(self.plugins) == 0:
            raise ValueError("No plugins in the chain to process input.")

        # Start processing with the first plugin
        if self.first_plugin_is_instrument():
            args = {
                'midi_messages': input.get_midi(),
                'samplerate': input.samplerate,
                'duration': input.duration
            }
        else:
            args = {
                'input_array': input.get_audio(),
                'samplerate': input.samplerate
            }

        return self.pedalboard.process()
