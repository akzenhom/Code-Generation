def decision_engine(customer_age, is_moh=False):
    min_age = 21
    max_age = 60
    min_age_moh = 18

    if is_moh:
        if min_age_moh <= customer_age <= max_age:
            return "Eligible"
        else:
            return "Not Eligible"
    else:
        if min_age <= customer_age <= max_age:
            return "Eligible"
        else:
            return "Not Eligible"