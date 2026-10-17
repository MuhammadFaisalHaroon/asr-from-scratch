import numpy as np
import matplotlib.pyplot as plt

# --- 1. Settings ---
sample_rate = 16000
duration = 1.0
frequency = 440.0
frame_size = 400
hop_length = 160

# --- 2. Generate & Frame Audio ---
time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_wave = np.sin(2 * np.pi * frequency * time)
window = np.hamming(frame_size)

num_frames = 1 + int((len(audio_wave) - frame_size) / hop_length)
frames = []
for i in range(num_frames):
    start = i * hop_length
    end = start + frame_size
    frames.append(audio_wave[start:end] * window)
frames = np.array(frames)

# --- 3. The FFT Magic ---
# We apply the Fast Fourier Transform to the rows (axis=1)
fft_result = np.fft.rfft(frames, n=frame_size)

# Calculate the magnitude (strength of each frequency)
magnitude = np.abs(fft_result)

# Convert to a logarithmic scale (Decibels) to represent volume naturally
# We add 1e-10 to avoid log(0) errors
power_spectrogram = 20 * np.log10(magnitude + 1e-10)

# --- 4. Visualize it ---
plt.figure(figsize=(10, 4))
# We use .T (transpose) so Time is on the X-axis and Frequency is on the Y-axis
plt.imshow(power_spectrogram.T, aspect='auto', origin='lower', cmap='viridis')
plt.title('Spectrogram of a 440 Hz Sine Wave')
plt.xlabel('Time Frames')
plt.ylabel('Frequency Bins (Hz)')
plt.colorbar(label='Magnitude (dB)')

# Save the image to your folder!
plt.savefig('my_first_spectrogram.png')
print("Success! Spectrogram saved as 'my_first_spectrogram.png'")