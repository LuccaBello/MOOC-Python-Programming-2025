import math

def get_station_data(filename: str):
    stations = {}
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(';')
                
                try:
                    longitude = float(parts[0])
                    latitude = float(parts[1])
                    name = parts[3]
                    stations[name] = (longitude, latitude)
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
        
    return stations

def distance(stations: dict, station1: str, station2: str):
    if station1 not in stations or station2 not in stations:
        raise ValueError(f"One or both stations not found in the data: {station1}, {station2}")

    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km

def greatest_distance(stations: dict):
    if len(stations) < 2:
        return (None, None, 0.0)

    station_names = list(stations.keys())
    max_dist = 0.0
    best_s1 = ""
    best_s2 = ""

    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            s1 = station_names[i]
            s2 = station_names[j]
            
            dist = distance(stations, s1, s2)
            
            if dist > max_dist:
                max_dist = dist
                best_s1 = s1
                best_s2 = s2
                
    return (best_s1, best_s2, max_dist)

if __name__ == "__main__":
    
    sample_data = """24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
    24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
    24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003
    24.93874;60.16436;5;Designmuseo;20;Yes;005
    24.92846;60.16281;6;Hietalahdentori;20;Yes;006
    24.939801;60.161989;4;Viiskulma;24;Yes;004
    """
    with open("stations1.csv", "w") as f:
        f.write(sample_data)
        
    print("--- Testing get_station_data ---")
    stations = get_station_data('stations1.csv')
    print(f"Loaded {len(stations)} stations.")
    
    print("\n--- Testing distance ---")
    d1 = distance(stations, "Designmuseo", "Hietalahdentori")
    print(f"Distance (Designmuseo, Hietalahdentori): {d1}")
    
    d2 = distance(stations, "Viiskulma", "Kaivopuisto")
    print(f"Distance (Viiskulma, Kaivopuisto): {d2}")

    print("\n--- Testing greatest_distance ---")
    station1, station2, greatest = greatest_distance(stations)
    print(f"Greatest distance: {station1}, {station2}, {greatest}")