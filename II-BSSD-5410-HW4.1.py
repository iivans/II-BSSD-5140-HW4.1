from collections import deque

# Graph based on the provided flight data
graph = {
    "OMA": ["DAL", "HOU", "MDW"], 
    "SDF": ["BWI", "DAL", "HOU", "MDW"], 
    "BWI": ["SDF", "PWM", "SLC", "BZE", "DAL", "HOU", "MDW"], 
    "PWM": ["BWI", "MDW"], 
    "SLC": ["MDW", "BWI", "DAL", "HOU"], 
    "BZE": ["HOU", "BWI"], 
    "DAL": ["MDW", "HOU", "SLC", "BWI", "SDF", "OMA"], 
    "HOU": ["OMA", "BWI", "SDF", "SLC", "BZE", "DAL", "MDW"], 
    "MDW": ["OMA", "BWI", "SDF", "PWM", "SLC", "DAL", "HOU"]
}

# BFS function to find the shortest path
def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        current_city, path = queue.popleft()
        
        if current_city == goal:
            return path
        
        visited.add(current_city)
        
        for neighbor in graph.get(current_city, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None  # If no path found

# Solve Task 1: Omaha to Louisville
result_1 = bfs_shortest_path(graph, "OMA", "SDF")
print("Shortest path from Omaha to Louisville:", result_1)

# Solve Task 2: Baltimore to Salt Lake City, then to Portland
result_2_to_salt_lake = bfs_shortest_path(graph, "BWI", "SLC")
result_2_to_portland = bfs_shortest_path(graph, "SLC", "PWM")
print("Shortest path from Baltimore to Salt Lake City:", result_2_to_salt_lake)
print("Shortest path from Salt Lake City to Portland:", result_2_to_portland)

# Solve Task 3: Belize City to Portland
result_3 = bfs_shortest_path(graph, "BZE", "PWM")
print("Shortest path from Belize City to Portland:", result_3)
