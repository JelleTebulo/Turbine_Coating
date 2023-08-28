import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Function to plot data from CSV
def plot_csv_data(file_path):
    df = pd.read_csv(file_path)

    print("Available columns:", df.columns)  # Print column names

    lasers = [col for col in df.columns if 'laser' in col]

    plt.figure(figsize=(10, 6))
    plt.axhline(y=125, color='black', linestyle='--', label='Reference Error')
    for laser in lasers:
        plt.plot(df[laser], label=laser)


    plt.xlabel('Row')
    plt.ylabel('Value')
    plt.title(f'Plot of laser data and robot tool height ({file_path})')
    plt.legend()
    plt.grid(True)


    plt.show()

    # Calculate and plot error between lasers and reference value (125mm)
    plt.figure(figsize=(10, 6))

    for laser in lasers:
        error = df[laser] - 125  # Calculate error
        plt.plot(error, label=f'{laser} - 125mm')

    plt.axhline(y=0, color='black', linestyle='--', label='Reference Error')
    plt.xlabel('Row')
    plt.ylabel('Error')
    plt.title(f'Error between lasers and reference value (125mm) ({file_path})')
    plt.legend()
    plt.grid(True)

    plt.show()

# File paths to plot
file_path1 = 'Excel_Data/lasers_grouped_request_2023_08_24__16-15-04.csv'
file_path2 = 'Excel_Data/lasers_normal_2023_08_24__16-13-37.csv'

# Plot data from both files
plot_csv_data(file_path1)
plot_csv_data(file_path2)