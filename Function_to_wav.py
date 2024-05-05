import numpy as np
import scipy.special as spec
import scipy.io.wavfile as wavfile

def generate_wav_from_function(function, duration, sample_rate, output_file):
    # Calculate the number of samples based on the duration and sample rate
    num_samples = int(duration * sample_rate)

    # Generate the time values for the samples
    t = np.linspace(0, duration, num_samples)

    # Calculate the function values based on the mathematical function
    y = function(t)

    # Scale the values to fit within the range of a 16-bit audio signal
    y_scaled = np.int16(y * (2 ** 13))

    # Write the WAV file
    wavfile.write(output_file, sample_rate, y_scaled)

# Define the mathematical function
def math_function(t):
    #return np.exp(np.sin(2 * np.pi * 440 * t))-(np.e+1/np.e)/2
    #return np.sin(np.sin(2 * np.pi * 440 * t)+np.sin(2 * np.pi * 220 * t)) + np.sin(np.sin(2 * np.pi * 110 * t)+np.sin(2 * np.pi * 880 * t))
    #return (np.sin(np.sin(2 * np.pi * 440 * t)+np.sin(2 * np.pi * 220 * t)) + np.sin(np.sin(2 * np.pi * 110 * t)+np.sin(2 * np.pi * 880 * t))) * 2**(np.sin(2 * np.pi * t))
    #return (np.exp(np.sin(2 * np.pi * 440 * t))-(np.e+1/np.e)/2) * (np.sin(np.sin(2 * np.pi * 440 * t)+np.sin(2 * np.pi * 220 * t)+np.sin(2 * np.pi * 110 * t)))
    #return np.sin(np.sin(2 * np.pi * 413 * t)+np.sin(2 * np.pi * 220 * t)) + np.sin(10 * np.sin(2 * np.pi * 110 * t)+np.sin(2 * np.pi * 2137 * t)) + np.sin(3 * np.sin(2 * np.pi * 60 * t))
    #return (np.sin(np.sin(2 * np.pi * 413 * t)+np.sin(2 * np.pi * 220 * t)) + np.sin(10 * np.sin(2 * np.pi * 110 * t)+np.sin(2 * np.pi * 2137 * t))) * np.sin(3 * np.sin(2 * np.pi * 60 * t))
    #return np.sin(np.sin(2 * np.pi * 413 * t)+np.sin(2 * np.pi * 220 * t)) * np.sin(10 * np.sin(2 * np.pi * 110 * t)+np.sin(2 * np.pi * 2137 * t)) + np.sin(3 * np.sin(2 * np.pi * 60 * t))
    #return np.sin(2**(t*np.sqrt(12)*0.5))
    #return np.sin(12/t)
    return np.sin(2**(t*np.sqrt(12)*0.5)) + np.sin(12/t)
    #return np.sin(2**(t*np.sqrt(12)*0.5)) * np.sin(12/t) * 2
    #return np.sin(t**t/5*spec.gamma(t))
    #return np.sin(2*np.pi*440*t)**3 + np.sin(np.pi*30*t**3)
    #return np.sin(2*np.pi*440*t)**2*(np.cos(t)) + (t**2/34)*np.cos(t**3)

# Set the duration, sample rate, and output file name
duration = 10  # 2 seconds
sample_rate = 88200  # 44.1 kHz
output_file = "output_func.wav"

# Generate the WAV file
generate_wav_from_function(math_function, duration, sample_rate, output_file)
