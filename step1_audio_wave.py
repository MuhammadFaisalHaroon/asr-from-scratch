import numpy as np

# 1. Define our settings
sample_rate = 16000  # 16,000 measurements per second
duration = 1.0       # 1 second of audio
frequency = 440.0    # 440 Hz (The "A" note)

# 2. Create the time axis. 
# np.linspace creates a list of numbers from 0 to 1.0, with 16000 steps.
time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# 3. Generate the sine wave using math!
# 2 * pi * frequency * time gives us the angle at any given millisecond
audio_wave = np.sin(2 * np.pi * frequency * time)

# 4. Print the results to see what the computer sees
print(f"Total number of data points: {len(audio_wave)}")
print(f"First 10 numbers of the audio wave:\n{audio_wave[:10]}")
print(f"The minimum value: {audio_wave.min():.2f}")
print(f"The maximum value: {audio_wave.max():.2f}")