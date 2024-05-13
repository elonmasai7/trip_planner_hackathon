class TripPlanner:
    def __init__(self, user_data):
        self.user_data = user_data

    def suggest_places(self):
        if 'last_visited' in self.user_data:
            last_visited = self.user_data['last_visited']
            suggestions = self._find_similar_places(last_visited)
            return suggestions
        else:
            return "No suggestion available. Please provide more data."

    def _find_similar_places(self, last_visited):
        # Simple placeholder method for suggesting similar places
        similar_places = {
            'Nairobi': ['Mombasa', 'Kisumu', 'Maasai Mara'],
            'Mombasa': ['Nairobi', 'Diani Beach', 'Watamu'],
            'Kisumu': ['Nairobi', 'Naivasha', 'Kakamega Forest'],
            # Add more suggestions as needed
        }
        return similar_places.get(last_visited, "No similar places found for the last visited location.")


def main():
    # Example user data
    user_data = {
        'last_visited': 'Nairobi'
        # Add more user data as needed
    }

    # Create a TripPlanner instance
    trip_planner = TripPlanner(user_data)

    # Get suggestions
    suggestions = trip_planner.suggest_places()

    # Display suggestions
    print("Suggestions for your next trip:")
    print(suggestions)


if __name__ == "__main__":
    main()
