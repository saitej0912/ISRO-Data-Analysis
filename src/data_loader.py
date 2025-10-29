import pandas as pd

def load_missions_data(filepath):
    missions = pd.read_csv(filepath)
    # Clean columns for spaces
    missions.columns = missions.columns.str.replace('\xa0', ' ', regex=False).str.strip()
    missions['Date'] = pd.to_datetime(missions['Date'], errors='coerce')
    missions['year'] = missions['Date'].dt.year
    return missions

def load_satellites_data(filepath):
    satellites = pd.read_csv(filepath)
    satellites.columns = satellites.columns.str.strip()
    satellites['launch_date'] = pd.to_datetime(satellites['launch_date'], errors='coerce')
    satellites['year'] = satellites['launch_date'].dt.year
    return satellites
