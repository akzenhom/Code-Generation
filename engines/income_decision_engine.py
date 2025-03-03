def decision_engine(income):
    min_income = 2500
    if income >= min_income:
        return "Eligible"
    else:
        return "Not Eligible"