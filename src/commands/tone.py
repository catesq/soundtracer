from plugin import plugin_wrappers, load_chain

from commands.input import build_input
from commands.args import parse_note, parse_frequency



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

    freq_match = parse_frequency(tone_str)
    if freq_match is not None:
        return freq_match
        
    # If it doesn't match frequency, try to parse as a note

    note_match = parse_note(tone_str)
    if note_match is not None:
        return note_match
    
    return None



def matcher(tone, plugin_name, input_desc, qfactor, harmonics, samplerate = 48000, wrap_type=plugin_wrappers.pedalboard):
    """
    Match a tone with a plugin.

    Args:
        tone (str): The tone to match, can be a note or frequency.
        plugin_name (str): The name of the plugin(s) to use for matching.
    
    Returns:
        None

    If the first instrument is an effect: 
       the input can be a type of noise_type | wave_name:tone | audio_file | midi_file 
         input = [ white_noise | pink_noise | brown_noise ]
         input = [ sine | saw | square ] : [midi note | frequency] eg 'input sine:a4' or 'input saw:440'

    If the first instrument is an instrument:  
       the input is a single midi note or the name of a midi file
    """
    
    freq = parse_tone(tone)

    if freq is None:
        print(f"Invalid tone: {tone}")
        return

    chain = load_chain(plugin_name, wrap_type)

    if chain.get_size() == 0:
        print(f"No plugins found for '{plugin_name}'")
        return
    
    # dict with the midi/audio input and samplerate for pedalboard.externalplugin.process()
    input = build_input(input_desc, chain, samplerate)

    audio_gen = chain.process(input)
    
    

    