# tuner_second_semester_26
Here’s a clean, professional GitHub README for your project based on the code you shared:

---

# 🎵 Python Audio Tuner

A simple Python-based tuner that detects the pitch of an audio input and compares it to a target musical note, showing whether the sound is in tune, sharp, or flat.

## 🚀 Features

* Detects fundamental frequency using YIN algorithm (via `librosa`)
* Supports natural notes, sharps (`#`), and flats (`b`)
* Calculates pitch deviation in cents
* Identifies the closest octave
* Provides clear tuning feedback:

  * In tune
  * Too sharp
  * Too flat

## 🧠 How It Works

1. User selects a note and accidental
2. Audio file is analyzed to extract the fundamental frequency
3. The detected frequency is compared to the target note frequency
4. The difference is expressed in **cents**
5. The octave is estimated relative to standard tuning (A4 = 440 Hz)

## 📦 Dependencies

Make sure you have the following installed:

```bash
pip install numpy librosa
```

## ▶️ Usage

1. Replace the audio file path in the script:

```python
audio_file = "path/to/your/audio.wav"
```

2. Run the script:

```bash
python tuner.py
```

3. Enter:

* Note (`C, D, E, F, G, A, B`)
* Accidental (`b`, `#`, `natural`)

## 📊 Example Output

```text
Input notes to tune ('C', 'D', 'E', 'F', 'G', 'A', 'B'): A
Input accidental to tune ('b', '#', 'natural'): natural
You chose: A

Fundamental F (Hz): 442.13
In tune (+8.36 cents)
Detected octave: 4
```

## ⚙️ Key Functions

* `extract_f0_yin(audio_path)`
  Extracts the fundamental frequency using the YIN algorithm

* `cents_offset(f_actual, f_target)`
  Calculates tuning difference in cents

* `detect_octave(target_note, f_actual)`
  Estimates the octave of the detected pitch

## 🎯 Future Improvements

* 🎤 Real-time microphone input instead of audio files
* 📱 GUI interface (Tkinter or web app)
* 🎸 Instrument-specific tuning modes (guitar, violin, etc.)
* 📈 Frequency visualization graphs

## ⚠️ Notes

* Best performance with clean, monophonic audio
* YIN detection range is currently limited to 200–550 Hz
* Audio file must contain a clear sustained pitch

## 📜 License

This project is open-source and free to use.
