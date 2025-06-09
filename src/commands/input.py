import os
import mido
from commands.args import parse_note, parse_duration
from commands.audio import read_audio_file, generate_audio
from plugin import plugin_chain

class Input:
    """
    Class to handle input processing for the plugin.
    It can process MIDI files, MIDI notes, and audio files.
    """

    def __init__(self, midi=None, audio=None, samplerate=48000, duration=1):
        self.midi = midi
        self.audio = audio
        self.samplerate = samplerate
        self.duration = duration

    def get_midi(self):
        return self.midi

    def get_audio(self, samplerate=48000):
        return self.audio


def is_midi_file(file_path):
    """
    Check if the given file path is a valid MIDI file.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is a valid MIDI file, False otherwise.
    """
    try:
        mido.MidiFile(file_path)
        return True
    except (IOError, mido.MidiFileError, Exception):
        return False



def get_midi(input, track = 0):
    """
    Get the input for the plugin based on the type of input.

    Args:
        input (str): The input string, can be a midi note or a midi file.
                     Midi note should be a string like 'A4', 'C#5'.
        track (int): The track number to extract from the MIDI file (default is 0).

    Returns:
        str: The processed input string.
    """

    # try to load midi file
    if os.path.isfile(input):
        if not is_midi_file(input):
            print(f"Error: {input} is not a valid MIDI file.")
            return None
        
        midi = mido.MidiFile(input)
        if track < 0 or track >= len(midi.tracks):
            print(f"Error: Track {track} does not exist in {input}.")
            return None
        
        return [msg for msg in midi.tracks[track]]


    # parse the input as a note or note:time, eg "c4" or "c4:500"
    if ':' in input: 
        # Try to parse as note with time after the colon
        note_input, time_input = input.strip().split(':', 1)

        note = parse_note(note_input)
        duration = parse_duration(time_input)

        return [
            mido.Message('note_on', note=note, velocity=64, time=0), 
            mido.Message('note_off', note=note, velocity=64, time=duration)
        ]
    
    
    else:
        # Try to parse as a note
        return [
            mido.Message('note_on', note=note, velocity=64, time=0), 
            mido.Message('note_off', note=note, velocity=64, time=1000)
        ]



def get_midi_duration(midi_messages):
    """
    Get the duration of the MIDI messages.

    Args:
        midi_messages (list): A list of MIDI messages.

    Returns:
        float: The duration of the MIDI messages in seconds.
    """

    if not midi_messages:
        return 0.0

    # Assuming the last message contains the end time
    last_message = midi_messages[-1]
    return last_message.time if hasattr(last_message, 'time') else 1.0



        

def get_audio(input, samplerate=48000):
    """
    Get the input for the plugin based on the type of input.

    Args:
        input (str): The input string, can be a path to audio file or a note.

    Returns:
        tuple: A tuple containing the audio data and the sample rate.
    """

    # if the first instrument is an effect: 
    #   the input can be a type of noise_type | wave_name:tone | audio_file | midi_file 
    #     input = [ white_noise | pink_noise | brown_noise ]
    #     input = [ sine | saw | square ] : [midi note | frequency] eg 'input sine:a4' or 'input saw:440'

    # if the first instrument is an instrument:  
    #   the input is a single midi note or the name of a midi file
    
    if os.path.isfile(input):
        return read_audio_file(input)
    else:
        return generate_audio(input, samplerate)


def build_input(input_desc, chain: plugin_chain, samplerate):
    """
    Build the input arguments for the plugin based on the input description and chain.

    Args:
        input_desc (str): The input description, can be a type of noise_type | wave_name:tone | audio_file | midi_file.
        chain (PluginChain): The plugin chain to use.
        samplerate (int): The sample rate for the audio processing.

    Returns:
        dict: The input arguments for the plugin.
    """
    
    if chain.first_plugin_is_instrument():
        audio = get_audio(input_desc)
        
        if audio is None:
            print(f"Invalid input for plugin '{chain.get_first_plugin_name()}': {input_desc}")
            return None
        
        return input.Input(audio=audio, samplerate=samplerate)
    else:
        midi = get_midi(input_desc)

        if midi is None:
            print(f"Invalid input for plugin '{chain.get_first_plugin_name()}': {input_desc}")
            return None
        
        return input.Input(midi=midi, duration=get_midi_duration(midi), samplerate=samplerate)