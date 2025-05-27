
import re

note_re = re.compile(r'([A-Ga-g]?)([#b?+-]?)(\d*)')
freq_re = re.compile(r'(\d+(\.\d+)?)([kK]?)')        

note_offsets = {
    'C': -9, 'D': -7, 
    'E': -5, 'F': -4, 'G': -2,
    'A': 0,  'B': 2
}



def get_note_offset(note, octave):
    """
    Get the note offset relative to A4.

    Args:
        note (str): The note name, e.g. A, C#, Fb, etc.
        octave (int): The octave number, default is 4.

    Returns:
        int: The note offset relative to A4, where A4 is 0.
    """

    note_offset = note_offsets.get(note, 0)
    note_offset += (octave - 4) * 12

    return note_offset



def parse_tone(tone_str):
    """
    The tone can be in hz, khz or a note name.
    Examples:
        A4, C#5, Fb, C, 440, 880, 1.2k, 2.5k

    Args:
        tone (str): The tone to parse
    
    Returns:
        float: frequency in hz
    """

    freq_match = freq_re.match(tone_str)
    if freq_match:
        freq_value = float(freq_match.group(1))
        freq_unit = freq_match.group(3)
        
        if freq_unit.lower() == 'k':
            freq_value *= 1000
        
        return freq_value

    note_match = note_re.match(tone_str)
    if note_match:
        note = note_match.group(1).upper()
        octave = int(note_match.group(3) or '4')
        note_offset = get_note_offset(note, octave)

        accidental = note_match.group(2)
        if accidental == '#' or accidental == '+':
            note_offset += 1
        elif accidental == 'b' or accidental == '-':
            note_offset -= 1

        return 440.0 * (2 ** (note_offset / 12.0))

    return None

def matcher(tone, plugin_name):
    """
    Match a tone with a plugin.

    Args:
        tone (str): The tone to match, can be a note or frequency.
        plugin_name (str): The name of the plugin to use for matching.
    
    Returns:
        None
    """
    
    freq = parse_tone(tone)
    if freq is None:
        print(f"Invalid tone: {tone}")
        return

    print(f"Matching tone '{tone}' ({freq:.2f} Hz) with plugin '{plugin_name}'")