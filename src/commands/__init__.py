from pedalboard_pluginary import PedalboardPlugins


from . import (
    file, tone
)


def list_plugins(type=None):
    """
    List available plugins or tones.
    If type is specified, list only that type.
    """
    plugins = PedalboardPlugins()
    
    if type is None:
        return plugins.as_list()
    elif type in ['vst3', 'aufx']:
        return [p for p in plugins.as_list() if p['type'] == type]
    else:
        return []



__all__ = [
    'file',
    'tone',
    'list_plugins'
]