import numpy as np

# 1. Settings
sample_rate = 16000
duration = 1.0
frequency = 440.0

# We will use a frame size of 400 samples (25 milliseconds) 
# and a hop length of 160 samples (10 milliseconds)
frame_size = 400
hop_length = 160

# 2. Generate the wave (same as before)
time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_wave = np.sin(2 * np.pi * frequency * time)

# 3. Create the Hamming Window
# This is a mathematical formula that looks like a bell curve. 
# It forces the edges of each frame to be close to 0, so there are no sudden jumps.
window = np.hamming(frame_size)

# 4. Chop the audio into frames
num_frames = 1 + int((len(audio_wave) - frame_size) / hop_length)
frames = []

for i in range(num_frames):
    # Get a chunk of 400 samples
    start = i * hop_length
    end = start + frame_size
    chunk = audio_wave[start:end]
    
    # Multiply by the Hamming window
    windowed_chunk = chunk * window
    frames.append(windowed_chunk)

# Convert the list of frames into a NumPy matrix
frames = np.array(frames)

print(f"Original audio shape: {audio_wave.shape}")
print(f"Number of frames created: {num_frames}")
print(f"Shape of our framed audio matrix: {frames.shape}")
print(f"Notice how the shape is now (Time Frames x Frame Size)")