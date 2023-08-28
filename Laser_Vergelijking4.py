import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Function to plot data from CSV
def plot_csv_data(file_path, save_path=None):
    df = pd.read_csv(file_path)

    print("Available columns:", df.columns)  # Print column names

    lasers = [col for col in df.columns if 'laser' in col]

    # Create subplots
    fig1, axs1 = plt.subplots(2, 1, figsize=(10, 18))

    # Plot laser data
    axs1[0].axhline(y=125, color='black', linestyle='--', label='Reference Error')
    for laser in lasers:
        axs1[0].plot(df[laser], label=laser)
    axs1[0].set_xlabel('Row')
    axs1[0].set_ylabel('Value')
    axs1[0].set_title(f'Plot of laser data ({file_path})')
    axs1[0].legend()
    axs1[0].grid(True)
    plt.show() # Adjust layout and show the subplots

    # Plot error between lasers and reference value
    axs1[1].axhline(y=0, color='black', linestyle='--', label='Reference Error')
    for laser in lasers:
        error = df[laser] - 125  # Calculate error
        axs1[1].plot(error, label=f'{laser} - 125mm')
    axs1[1].set_xlabel('Row')
    axs1[1].set_ylabel('Error')
    axs1[1].set_title(f'Error between lasers and reference value (125mm) ({file_path})')
    axs1[1].legend()
    axs1[1].grid(True)
    plt.show() # Adjust layout and show the subplots

    # Create subplots
    fig3, axs3 = plt.subplots(2, 1, figsize=myfigsize)  # Two subplots arranged vertically
    # Laser pairs to compare
    laser_pairs = [(lasers[0], lasers[1]), (lasers[2], lasers[3])]

    for (laser1, laser2), ax in zip(laser_pairs, axs3):
        # Calculate and plot errors between current laser pair from both files
        error_laser = df[laser2] - df[laser1]  # Assuming the lasers have the same index
        ax.plot(error_laser)
        ax.axhline(y=0, color='black', linestyle='--', label='Reference Error')
        ax.set_xlabel('Row')
        ax.set_ylabel(f'{laser1} - {laser2}')
        ax.set_title(f'Error between {laser1} and {laser2}')
        ax.legend()
        ax.grid(True)

    # Set a common title for the figure
    fig3.suptitle(f'Error Comparison between Laser Pairs for File ({file_path})')

    # Adjust layout and show the subplots
    plt.tight_layout()
    plt.show()

    # Save the figure if save_path is provided
    if save_path:
        fig1.savefig(save_path)
    else:
        # Show the plot if save_path is not provided
        plt.show()


# Function to plot data from CSV
def plot_csv_data2(file_path1, file_path2, save_path=None):
    df1 = pd.read_csv(file_path1)
    df2 = pd.read_csv(file_path2)

    lasers = [col for col in df1.columns if 'laser' in col]

    # Create subplots
    fig2, axs2 = plt.subplots(1, 1, figsize=myfigsize)  # Use the same size as your original code

    # Calculate and plot errors between all four lasers
    for laser in lasers:
        error_laser = df1[laser] - df2[laser]  # Assuming the lasers have the same index
        axs2.plot(error_laser, label=f'File 1 - File 2 ({laser})')

    axs2.axhline(y=0, color='black', linestyle='--', label='Reference Error')
    axs2.set_xlabel('Row')
    axs2.set_ylabel('Error')
    axs2.set_title(f'Error between File 1 and File 2 for all lasers')
    axs2.legend()
    axs2.grid(True)

    # Adjust layout and show the subplots
    plt.tight_layout()
    plt.show()

    if save_path:   fig2.savefig(save_path)
    else:           plt.show()       # Show the plot if save_path is not provided


screen_width = 23.5  # Replace with your screen width
screen_height = 13.2  # Replace with your screen height
myfigsize=(screen_width, screen_height)

# Define file paths for saving figures
save_path1, save_path2, save_path3 = 'plot1.png', 'plot2.png', 'plot3.png'

# File paths to plot
file_path1 = 'Excel_Data/lasers_grouped_request_2023_08_24__16-15-04.csv'
file_path2 = 'Excel_Data/lasers_normal_2023_08_24__16-13-37.csv'

# Plot data from both files
plot_csv_data(file_path1, save_path1)
plot_csv_data(file_path2, save_path2)

# Plot data from both files
plot_csv_data2(file_path1, file_path2, save_path3)
