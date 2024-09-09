import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt
from torch.nn import functional as F

# Function to calculate the squared Euclidean distance
def calculate_squared_euclidean(predicted, actual):
    return torch.sum((predicted - actual) ** 2).item()

# Modify the probability score function to generate predictions using the generator
def calculate_probability_and_predict(generator, discriminator, signal_slice):
    # Pad the signal to match the expected size (1824)
    padded_signal = np.pad(signal_slice.values, (0, 1824 - len(signal_slice)), mode='constant')

    signal_tensor = torch.tensor(padded_signal, dtype=torch.float32)
    signal_tensor = signal_tensor.unsqueeze(0).unsqueeze(1)

    # Set the models to evaluation mode
    discriminator.eval()
    generator.eval()

    with torch.no_grad():
        # Get discriminator output for the probability score
        discriminator_output = discriminator(signal_tensor)
        probability_score = torch.sigmoid(discriminator_output).item()

        # Use the generator to predict the second half of the signal
        predicted_signal = generator(signal_tensor)

        # Extract the second half of the predicted and actual signals
        actual_signal_second_half = signal_tensor[0, 0, len(signal_slice)//2:].unsqueeze(0)
        predicted_signal_second_half = predicted_signal[0, 0, len(signal_slice)//2:].unsqueeze(0)

        # Calculate the squared Euclidean distance (predictive error)
        predictive_error = calculate_squared_euclidean(predicted_signal_second_half, actual_signal_second_half)

    return probability_score, predictive_error


# Load the saved discriminator and generator models
discriminator_path = r'C:\nets\dcgan_netD.pkl'
loaded_discriminator = torch.load(discriminator_path)
generator_path = r'C:\nets\dcgan_netG.pkl'
loaded_generator = torch.load(generator_path)

# List of file paths
file_paths = [r'C:\filtered_signal10.xlsx',
              r'C:\filtered_signal12.xlsx',
              r'C:\filtered_signal14.xlsx']


# Iterate over each file path
for i, file_path in enumerate(file_paths):
    # Read the signal data from the Excel file
    df = pd.read_excel(file_path, header=None)
    df = pd.to_numeric(df[0], errors='coerce')

    # Define the slice parameters
    slice_length = 180
    stride = 30

    # Lists to store results
    slice_start_indices = []
    probability_scores = []
    predictive_errors = []

    # Iterate over slices and calculate probability scores and predictive errors
    for start_idx in range(0, len(df) - slice_length + 1, stride):
        slice_start_indices.append(start_idx)
        signal_slice = df[start_idx: start_idx + slice_length]
        
        # Get probability score and predictive error
        probability_score, predictive_error = calculate_probability_and_predict(
            loaded_generator, loaded_discriminator, signal_slice)
        
        probability_scores.append(probability_score)
        predictive_errors.append(predictive_error)

    # Print or save the results
    print(f"File: {file_path}")
    print(f"Probability Scores: {probability_scores}")
    print(f"Predictive Errors: {predictive_errors}")
