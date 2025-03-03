def decision_engine(amount):
    min_limit = 1000
    if amount >= min_limit:
        return "Approved"
    else:
        return "Rejected"