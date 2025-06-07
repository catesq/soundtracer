import re


note_re = re.compile(r'([A-Ga-g])([#b?+-]?)(\d*)')
freq_re = re.compile(r'(\d+(\.\d+)?)([kK]?)')
time_re = re.compile(r'(^\d+(\.\d+)?)(ms)?$')


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



def parse_note(tone_str):
    """
    Parse a note string into its frequency.

    Args:
        tone_str (str): The note string, e.g. A4, C#5, Fb, C, etc.
    
    Returns:
        float: The frequency in Hz.
    """
    
    match = note_re.match(tone_str)
    if match:
        note = match.group(1).upper()
        accidental = match.group(2)
        octave = int(match.group(3) or '4')
        
        note_offset = get_note_offset(note, octave)

        if accidental == '#' or accidental == '+':
            note_offset += 1
        elif accidental == 'b' or accidental == '-':
            note_offset -= 1

        return 440.0 * (2 ** (note_offset / 12.0))

    return None



def parse_frequency(tone_str):
    """
    Parse a frequency string into its numeric value.

    Args:
        tone_str (str): The frequency string, e.g. 440, 880, 1.2k, 2.5k, etc.
    
    Returns:
        float: The frequency in Hz.
    """

    match = freq_re.match(tone_str)
    if match:
        freq_value = float(match.group(1))
        freq_unit = match.group(3)

        if freq_unit.lower() == 'k':
            freq_value *= 1000

        return freq_value

    return None



def parse_duration(duration_str, default_time = 1.0):
    """
    Parse a duration string into its numeric value in seconds.

    Args:
        duration_str (str): The duration string, e.g. 500ms, 1.5s, etc.
    
    Returns:
        float: The duration in seconds.
    """
    match = time_re.match(duration_str, 1.0)

    if match:
        time_val = float(match.group(1))

        if match.group(3):  # if 'ms' is present, convert to seconds
            duration = time_val / 1000.0
        else:
            duration = time_val  # assume seconds if no 'ms'
    else:
        return duration
