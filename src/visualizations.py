import matplotlib.pyplot as plt
import os

def plot_satellites_per_year(satellites, save_path=None):
    counts = satellites.groupby('year').size()
    plt.figure(figsize=(10,5))
    counts.plot(kind='bar')
    plt.title('Satellites Launched Per Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    if save_path:
        plt.savefig(save_path)
    plt.close()

def plot_mission_success(status_counts, save_path=None):
    plt.figure(figsize=(6,4))
    status_counts.plot(kind='bar')
    plt.title('Mission Success Counts')
    plt.xlabel('Status')
    plt.ylabel('Count')
    if save_path:
        plt.savefig(save_path)
    plt.close()
