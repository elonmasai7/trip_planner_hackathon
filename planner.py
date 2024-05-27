from math import radians, sin, cos, sqrt, atan2

class TripPlanner:
    def __init__(self, user_data):
        self.user_data = user_data

    def calculate_distance(self, origin, destination):
        
        lat1, lon1 = origin
        lat2, lon2 = destination
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = 6371 * c  # Radius of earth in kilometers
        return distance

    def suggest_places(self):
        if 'last_visited' in self.user_data:
            last_visited = self.user_data['last_visited']
            suggestions = self._find_similar_places(last_visited)
            return suggestions
        else:
            return "No suggestion available. Please provide more data."

    def _find_similar_places(self, last_visited):
        
        towns_and_similar_places = {
            'Nairobi': ['Mombasa', 'Kisumu', 'Maasai Mara', 'Nakuru', 'Eldoret', 'Thika', 'Malindi', 'Kitale', 'Garissa', 'Kakamega', 'Nyeri', 'Machakos', 'Ruiru', 'Meru', 'Lamu'],
            'Mombasa': ['Nairobi', 'Diani Beach', 'Watamu', 'Kisumu', 'Nakuru', 'Malindi', 'Kitale', 'Garissa', 'Kakamega', 'Nyeri', 'Machakos', 'Ruiru', 'Meru', 'Lamu'],
            'Kisumu': ['Nairobi', 'Naivasha', 'Kakamega Forest', 'Mombasa', 'Nakuru', 'Eldoret', 'Thika', 'Malindi', 'Kitale', 'Garissa', 'Nyeri', 'Machakos', 'Ruiru', 'Meru', 'Lamu'],
            # Add more towns and their similar places as needed
        }
        return towns_and_similar_places.get(last_visited, "No similar places found for the last visited town.")

    def budget_estimation(self, destination):
        # Placeholder method for budget estimation based on destination
        # You can implement more sophisticated logic here based on user preferences, duration, etc.
        estimated_budget = {
            'Nairobi': 10000,
            'Mombasa': 12000,
            'Kisumu': 8000,
            'Maasai Mara': 15000,
            'Diani Beach': 13000,
            'Watamu': 11000,
            'Naivasha': 9000,
            'Kakamega Forest': 8500,
            # Add more destinations with their estimated budgets
        }
        return estimated_budget.get(destination, "Budget estimation not available for this destination.")


def main():
    # Example user data
    user_data = {
        'last_visited': 'Nairobi'
        # Add more user data as needed
    }

    # Create a TripPlanner instance
    trip_planner = TripPlanner(user_data)

    # Search bar for user input
    destination = input("Enter a destination town in Kenya: ")

    # Get suggestions based on user input
    suggestions = trip_planner._find_similar_places(destination)

    # Display suggestions
    print("Suggestions for your next trip:")
    print(suggestions)

    # Calculate distance between Nairobi and the destination
    nairobi = (-1.286389, 36.817223)
    destination_coords = {
        'Nairobi': nairobi,
        'Mombasa': (-4.0435, 39.6682),
        'Kisumu': (-0.0917, 34.7679),
        # Add coordinates for other destinations
    }
    if destination in destination_coords:
        distance_nairobi_destination = trip_planner.calculate_distance(nairobi, destination_coords[destination])
        print(f"The distance between Nairobi and {destination} is approximately {distance_nairobi_destination:.2f} kilometers.")

    # Estimate budget for the destination
    budget_destination = trip_planner.budget_estimation(destination)
    print(f"Estimated budget for a trip to {destination}: KES {budget_destination:.2f}")


if __name__ == "__main__":
    main()
