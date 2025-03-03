def generate_decision_engine(config):
    max_limit = config['Maximum Limit']['MaxLimit']
    is_considering_higher_limit = config['Maximum Limit']['IsConsideringHigherLimit']
    
    def decision_engine(request_amount):
        if request_amount <= max_limit:
            return "Approved"
        elif is_considering_higher_limit:
            return "Pending Further Review"
        else:
            return "Rejected"
    
    return decision_engine

config = {'Maximum Limit': {'MaxLimit': 300000, 'IsConsideringHigherLimit': False}}
decision_engine = generate_decision_engine(config)