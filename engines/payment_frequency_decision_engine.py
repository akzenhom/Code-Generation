def generate_decision_engine(payment_data):
    payment_frequency = payment_data.get('Payment Frequency', {}).get('PaymentFrequency')
    
    if payment_frequency == 1:
        return "Monthly Payment"
    else:
        return "Other Payment Frequency"

# Example usage
payment_data = {'Payment Frequency': {'PaymentFrequency': 1}}
decision = generate_decision_engine(payment_data)
print(decision)