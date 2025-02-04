class TravelItineraryPlanner:
    def __init__(self, destinations, activities, travel_time, budget):
        self.destinations = destinations  # List of destination names
        self.activities = activities  # Dictionary of activities for each destination
        self.travel_time = travel_time  # Time taken to travel between destinations
        self.budget = budget  # Total available budget for the trip
        self.best_itinerary = None
        self.best_utility = -1  # Lowest utility score possible
        
    def set_preferences(self, preferred_activities, max_travel_time, max_budget):
        """Sets the user's preferences for activities, travel time, and budget."""
        self.preferred_activities = preferred_activities
        self.max_travel_time = max_travel_time
        self.max_budget = max_budget
    
    def calculate_utility(self, itinerary):
        """Calculates the utility score for a given itinerary."""
        total_time = 0
        total_cost = 0
        total_activity_match = 0
        
        for i in range(len(itinerary) - 1):
            # Add travel time between destinations
            total_time += self.travel_time[itinerary[i]][itinerary[i + 1]]
            
            # Add activity scores for each destination based on preferences
            for activity in self.activities[itinerary[i]]:
                if activity in self.preferred_activities:
                    total_activity_match += 1
            
            # Add costs for each destination (simplified for this example)
            total_cost += 100  # Assuming each destination costs $100 (simplified)
        
        # Check if travel time and cost are within the limits
        if total_time > self.max_travel_time or total_cost > self.max_budget:
            return -1  # Invalid itinerary
        
        # Calculate the utility score: higher score is better
        utility_score = total_activity_match - (total_time / 10) - (total_cost / 50)
        return utility_score
    
    def plan_trip(self):
        """Generate all possible itineraries and select the best one."""
        from itertools import permutations
        
        # Generate all possible itineraries
        itineraries = list(permutations(self.destinations))
        
        for itinerary in itineraries:
            # Calculate utility score for each itinerary
            utility = self.calculate_utility(itinerary)
            if utility > self.best_utility:
                self.best_utility = utility
                self.best_itinerary = itinerary
        
        return self.best_itinerary, self.best_utility
    
    def suggest_itinerary(self):
        """Return the best itinerary based on utility score."""
        if self.best_itinerary:
            return f"Best Itinerary: {self.best_itinerary} with Utility Score: {self.best_utility}"
        else:
            return "No valid itinerary found within the given constraints."

# Example usage:

# Define destinations, activities, and travel times
destinations = ["Paris", "Rome", "Berlin"]
activities = {
    "Paris": ["Sightseeing", "Shopping", "Museum"],
    "Rome": ["Sightseeing", "Food", "Museum"],
    "Berlin": ["Nightlife", "Museum", "Shopping"]
}
travel_time = {
    "Paris": {"Rome": 2, "Berlin": 3},
    "Rome": {"Paris": 2, "Berlin": 2},
    "Berlin": {"Paris": 3, "Rome": 2}
}

# Set user's budget and preferences
budget = 500  # Total budget
preferred_activities = ["Museum", "Sightseeing"]  # Preferred activities
max_travel_time = 5  # Maximum travel time (in hours)

# Create a travel itinerary planner agent
planner = TravelItineraryPlanner(destinations, activities, travel_time, budget)

# Set the user's preferences
planner.set_preferences(preferred_activities, max_travel_time, budget)

# Plan the trip and suggest the best itinerary
planner.plan_trip()
itinerary = planner.suggest_itinerary()

print(itinerary)
