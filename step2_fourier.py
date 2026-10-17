import numpy as np

# 1. Generate the exact same 440 Hz audio wave from Step 1
sample_rate = 16000
duration = 1.0
frequency = 440.0
time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_wave = np.sin(2 * np.pi * frequency * time)

# 2. Apply the Fast Fourier Transform (FFT)
# We use np.fft.rfft because our audio is real numbers, not complex numbers
fft_result = np.fft.rfft(audio_wave)

# 3. Calculate the magnitude (volume) of each frequency
# The FFT returns complex numbers, so we take the absolute value to get the strength
magnitude = np.abs(fft_result)

# 4. Find the frequency with the highest magnitude (the "peak")
peak_index = np.argmax(magnitude)

# 5. Convert that index back into Hertz (Hz)
# The total number of frequencies is (sample_rate / 2) + 1
frequencies = np.fft.rfftfreq(len(audio_wave), d=1.0/sample_rate)
detected_frequency = frequencies[peak_index]

print(f"Total frequency bins: {len(magnitude)}")
print(f"The loudest frequency detected is: {detected_frequency:.2f} Hz")