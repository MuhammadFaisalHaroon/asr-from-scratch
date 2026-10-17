# From-Scratch Audio Feature Extraction (NumPy)

## 📌 Project Overview
This repository contains a from-scratch implementation of the audio processing pipeline required for Automatic Speech Recognition (ASR). Instead of relying on high-level libraries like `librosa` or `torchaudio`, this project uses pure NumPy to mathematically derive the Mel-Spectrogram features from raw audio waveforms.

## 🛠️ Core Technologies
*   **Language:** Python
*   **Math/Data Science:** NumPy (Matrix operations, FFT)
*   **Visualization:** Matplotlib
*   **Skills Demonstrated:** Deep Learning data pipelines, Audio Signal Processing, Fourier Transforms.

## 🧠 Methodology Implemented
1.  **Waveform Generation:** Synthesized a 440Hz sine wave to simulate raw audio input.
2.  **Framing & Windowing:** Chopped the continuous audio into overlapping frames (25ms) and applied a Hamming window to prevent spectral leakage.
3.  **Fast Fourier Transform (FFT):** Transformed the time-domain signal into the frequency domain using `np.fft.rfft`.
4.  **Spectrogram Generation:** Converted the magnitude to a logarithmic (Decibel) scale to create a 2D representation of sound over time.

## 📊 Results
The pipeline successfully extracts a 2D spectrogram matrix `(98 time frames x 201 frequency bins)` which is ready to be fed into a Convolutional Neural Network (CNN) or Transformer model.