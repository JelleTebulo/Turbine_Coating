import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Function to plot data from CSV
def plot_csv_data(file_path):
    df = pd.read_csv(file_path)

    print("Available columns:", df.columns)  # Print column names

    lasers = [col for col in df.columns if 'laser' in col]
    robot_z = ' robot_z'

    plt.figure(figsize=(10, 6))

    for laser in lasers:
        plt.plot(df[laser], label=laser)

    # plt.plot(df[robot_z], label=robot_z, linestyle='dashed')

    plt.xlabel('Row')
    plt.ylabel('Value')
    plt.title(f'Plot of laser data and robot tool height ({file_path})')
    plt.legend()
    plt.grid(True)

    plt.show()


# File paths to plot
file_path1 = 'Excel_Data/lasers_grouped_request_2023_08_24__16-15-04.csv'
file_path2 = 'Excel_Data/lasers_normal_2023_08_24__16-13-37.csv'

# Plot data from both files
plot_csv_data(file_path1)
plot_csv_data(file_path2)

