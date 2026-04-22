import math
import librosa
import numpy as np


notes= ["C", "D", "E", "F", "G", "A", "B"] #list that can be accessed as notes[#]
accidentals= ["b", "#", "natural"] #list that can be accessed as accidentals[#]
A4_FREQ = 440.0 #float value - standard tuning reference
#dictionary for all notes frequencues - accessed by key (note_frequency["A"])
note_frequency = {'C':261.63,'C#':277.18,'Db': 277.18, 'D':293.66,'D#':311.13,'Eb': 311.13,'E':329.63,'F':349.23,'F#':369.99,'Gb':369.99, 'G':392,'G#':415.3,'Ab':415.3,'A':440,'A#':466.16,'Bb':466.16,'B':493.88}


def main():
    #user input for note and accidental
    note = input("Intput notes to tune ('C', 'D', 'E', 'F', 'G', 'A', 'B'): ")
    accidental = input("Intput accidental to tune ('b', '#', 'natural': ")
    print(f"You chosed:{note}{accidental}") #prints out user input choice
    
    if accidental == "natural":
        target_note = note
    else:
        target_note = note + accidental
    
    # f_actual should be our input from the microphone
    audio_file = "" #PUT YOUR OWN AUDIO FILE PATH HERE
    f_actual= extract_f0_yin(audio_file) #highest peak frequency of audio_file
    target_oct = detect_octave(target_note, f_actual)
    f_target = note_frequency[target_note]
    offset = cents_offset(f_actual, f_target)
    print("Fundamental F (Hz):", round(f_actual, 2))

    if abs(offset) <= 100:
        print(f"In tune ({offset:+.2f} cents)")
    elif offset > 100:
        print(f"Out of tune, too sharp ({offset:+.2f} cents)")
    elif offset < -100:
        print(f"Out of tune, too flat ({offset:+.2f} cents)")   
    print(f"Detected octave: {target_oct}")

def extract_f0_yin(audio_path): #returns the frequency of the highest peak
    # Load audio file
    y, sr = librosa.load(audio_path, sr=None, mono=True)

    # Run YIN pitch detection
    f0 = librosa.yin(
        y,
        fmin=200,
        fmax=550,
        sr=sr
    )
    
    # Remove NaN values (YIN sometimes returns them)
    f0 = f0[~np.isnan(f0)]

    # If no valid pitch detected
    if len(f0) == 0:
        raise ValueError("No pitch detected in audio file.")

    # Use median instead of max (more stable fundamental)
    frequency_peak = float(np.median(f0))

    return frequency_peak

def cents_offset(f_actual, f_target):
    return 1200 * math.log2(f_actual / f_target)

def detect_octave(target_note, f_actual):
    base_freq = note_frequency[target_note] #gives value of target note in Hz
    # how many times frequency doubled or halved relative to 4th octave
    octave_shift = round(math.log2(f_actual / base_freq))
    detected_oct = 4 + octave_shift #detect 
    return detected_oct

if __name__ == "__main__":
    main()
