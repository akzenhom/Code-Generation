def generate_decision_engine(criteria):
    def decision_engine(employee_data):
        if employee_data.get('Length of Service', 0) >= criteria['Length of Service']['MinLengthOfService']:
            return True
        return False
    return decision_engine

criteria = {'Length of Service': {'MinLengthOfService': 1}}
engine = generate_decision_engine(criteria)

# Example usage:
employee_data = {'Length of Service': 2}
print(engine(employee_data))  # Output: True