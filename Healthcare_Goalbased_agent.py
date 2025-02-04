class HealthcareDiagnosticAgent:
    def __init__(self, symptoms, medical_history):
        self.symptoms = symptoms
        self.medical_history = medical_history
        self.goal = None
        self.diagnosis = None
        
    def set_goal(self, goal):
        """Sets the goal for the agent (e.g., diagnose a disease)."""
        self.goal = goal

    def process_input(self):
        """Process symptoms and medical history to suggest a diagnosis."""
        # Example goal: diagnosing a condition based on symptoms
        if self.goal == "diagnose":
            self.diagnosis = self.diagnose_condition()

    def diagnose_condition(self):
        """Diagnoses a medical condition based on symptoms."""
        # Basic rule-based diagnosis for demonstration
        if 'fever' in self.symptoms and 'cough' in self.symptoms:
            return "Flu"
        elif 'headache' in self.symptoms and 'nausea' in self.symptoms:
            return "Migraine"
        elif 'shortness of breath' in self.symptoms and 'chest pain' in self.symptoms:
            return "Heart Attack"
        else:
            return "Condition Uncertain"
        
    def take_action(self):
        """Take action based on the diagnosis (e.g., suggest medical action)."""
        if self.diagnosis == "Flu":
            return "Recommend taking rest, hydration, and over-the-counter medications."
        elif self.diagnosis == "Migraine":
            return "Recommend resting in a dark room and taking pain relievers."
        elif self.diagnosis == "Heart Attack":
            return "Recommend immediate medical attention and call for an ambulance."
        else:
            return "Consult with a doctor for further evaluation."
    
    def get_diagnosis(self):
        """Returns the diagnosis."""
        return self.diagnosis


# Example usage:
# A patient has symptoms such as fever and cough
patient_symptoms = ['fever', 'cough']
patient_medical_history = []  # You could also add medical history, if relevant

# Create a healthcare diagnostic agent for the patient
diagnostic_agent = HealthcareDiagnosticAgent(patient_symptoms, patient_medical_history)

# Set the agent's goal to "diagnose"
diagnostic_agent.set_goal("diagnose")

# Process the input (symptoms and medical history) to get a diagnosis
diagnostic_agent.process_input()

# Get the diagnosis and recommended actions
diagnosis = diagnostic_agent.get_diagnosis()
action = diagnostic_agent.take_action()

print(f"Diagnosis: {diagnosis}")
print(f"Recommended Action: {action}")
