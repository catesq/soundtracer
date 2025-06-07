import re
import numpy as np
import soundfile as sf
from commands.args import parse_note, parse_frequency

audio_re = re.compile(r'(noise|sine|saw|square)(?::(\w+))?')




def read_audio_file(file_name):
    """
    Read an audio file and return its content.

    Args:
        file_name (str): The path to the audio file.

    Returns:
        tuple: A tuple containing the audio data and the sample rate.
    """

    data, samplerate = sf.read(file_name)

    if data.ndim == 1:
        data = np.expand_dims(data, axis=1)

    return data, samplerate




def generate_audio(input, duration = 1, samplerate=48000):
    """
    Generate audio based on the input string.

    Args:
        input (str): The input string, can be a type of noise_type | wave_name:tone.
        duration (float): The duration of the generated audio in seconds (default is 1.0).
        samplerate (int): The sample rate for the generated audio (default is 48000).

    Returns:
        tuple: A tuple containing the generated audio data and the sample rate.
    """

    # Placeholder for actual audio generation logic
    # For now, we will return a dummy signal
    duration = 1.0  # 1 second duration
    
    input = input.lower().strip()
    match = audio_re.match(input)
    if not match:
        print(f"Invalid input format: {input}")
        return None, samplerate
    

    audio_type = match.group(1)
    tone = match.group(2)

    if audio_type in ['sine', 'saw', 'square']:
        if tone is None:
            frequency = 440.0  # Default to A4 note
        else:
            frequency = parse_note(tone) or parse_frequency(tone) or 440.0

        if audio_type == 'sine':
            audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
        elif audio_type == 'saw':
            audio_data = 0.5 * (2 * (t * frequency - np.floor(t * frequency + 0.5)))
        elif audio_type == 'square':
            audio_data = 0.5 * np.sign(np.sin(2 * np.pi * frequency * t))

        return audio_data.astype(np.float32), samplerate

    else:
        t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
        audio = np.random.normal(0, 0.5, t.shape)
        
        return audio.astype(np.float32), samplerate