stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfive"] = set(["ca", "az"])

needed = set(["wa", "mt", "id", "nv", "ut", "or", "ca", "az"])
final_stations = set()
while(needed):
    best_station = None
    states_covered = set()
    for station, station_states in stations.items():
        covered = needed & station_states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    needed -= states_covered

print(final_stations)
