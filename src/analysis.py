def calculate_mission_success(missions):
    def mission_success(application):
        if isinstance(application, str) and 'partially successful' in application.lower():
            return 'Partial/Failure'
        else:
            return 'Success'
    missions['mission_status'] = missions['Application'].apply(mission_success)
    return missions['mission_status'].value_counts()

def satellite_mass_distribution(satellites):
    return satellites['mass'].dropna()
