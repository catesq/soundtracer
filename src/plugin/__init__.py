from .wrapper import plugin_wrappers, plugin_chain
from . import pedalboard_wrapper

def get_wrapper_class(wrap_type):
    """
    Get the wrapper class based on the specified type.

    Args:
        wrap_type (str): The type of wrapper to retrieve.

    Returns:
        class: The wrapper class corresponding to the specified type.
    """
    if wrap_type == plugin_wrappers.pedalboard:
        return pedalboard_wrapper.pedalboard_wrapper
    
    raise ValueError(f"Unsupported wrapper type: {wrap_type}")


def load_chain(plugin_name, wrap_type):
    """
    Load a plugin or list of plugins. 

    Args:
        plugin_name (str|list): The file name of the plugin or plugins to load.
        wrap_type (str): The type of wrapper to use for the plugin.

    Returns:
        object: The loaded plugin instance.
    """
    if isinstance(plugin_name, list):
        plugins = [get_wrapper_class(wrap_type)(name) for name in plugin_name]
        return plugin_chain(plugins)
    elif isinstance(plugin_name, str):
        return plugin_chain(get_wrapper_class(wrap_type)(plugin_name))
    else:
        raise TypeError("plugin_name must be a string or a list of strings")    
