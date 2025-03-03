def age_check(rule_values, client_data):
    """
    Check the age rule against client data for each case:
    1- Retired
    2- Medical officer of health (MOH) Not Retired
    3- Military Not Retired:
        - MilitaryStudent
        - MilitaryOfficer
        - MilitaryNon-Officer
    4- Not Retired General Case
 
    Returns:
        Tuple containing:
        - error message if rule fails, None if it passes
        - list of acceptance reasons
        - list of rejection reasons
    """
   
    military_age_keys = {
        "MilitaryStudent": "MaxAge-MilitaryStudent",
        "MilitaryOfficer": "MaxAge-MilitaryOfficer",
        "MilitaryNonOfficer": "MaxAge-MilitaryNonOfficer"
    }
 
    job_age_keys = {
        "MOH": "MaxAge-MOH",
        "Doctor": "MaxAge-MOH",
        "Consultant Doctor": "MaxAge-MOH"
    }
 
    min_age = rule_values.get("MinAge", 0)
    max_age = rule_values.get("MaxAge-Employed", rule_values.get("MaxAge", float("inf")))
    client_age = client_data['age']
   
    # Initialize lists for acceptance and rejection reasons
    acceptances = []
    rejections = []
    error = None
 
    age_values = {
        "minAge": min_age,
        "maxAge": max_age,
        "expected":f"{min_age}-{max_age}",
        "actual":client_age
    }
 
   
 
    # 1- Retired
    if "MaxAge-Retirees" in rule_values and client_data["retired"]:
        max_age = rule_values.get("MaxAge-Retirees", max_age)
        age_values["maxAge"] = max_age
        age_values["minAge"] = min_age
        age_values["expected"] = f"{min_age}-{max_age}"
        age_values["actual"] = client_age
        if not (min_age <= client_age <= max_age):
            error = f"Age For Retirees must be between {min_age} and {max_age}, But Customer Age is {client_age}"
            rejections.append(error)
        else:
            acceptances.append(f"Age For Retirees must be between {min_age} and {max_age}, And the Customer Age is {client_age} so he passed age checking")
       
    # 2- MOH
    job = client_data.get("job")
    if job in job_age_keys and job_age_keys[job] in rule_values and not client_data["retired"]:
        min_age = rule_values.get("MinAge-MOH", min_age)
        max_age = rule_values.get(job_age_keys[job], max_age)
        age_values["maxAge"] = max_age
        age_values["minAge"] = min_age
        age_values["expected"] = f"{min_age}-{max_age}"
        age_values["actual"] = client_age
        if not (min_age <= client_age <= max_age):
            error = f"Age For {job} must be between {min_age} and {max_age}, But Customer Age is {client_age}"
            rejections.append(error)
        else:
            acceptances.append(f"Age For {job} must be between {min_age} and {max_age}, And the Customer Age is {client_age} so he passed age checking")
   
    # 3- Military
    milit_rank = client_data.get("militaryRank")
    if milit_rank in military_age_keys and military_age_keys[milit_rank] in rule_values and milit_rank is not None and not client_data["retired"]:
        max_age = rule_values.get(military_age_keys[milit_rank], max_age)
        age_values["maxAge"] = max_age
        age_values["minAge"] = min_age
        age_values["expected"] = f"{min_age}-{max_age}"
        age_values["actual"] = client_age
        if not (min_age <= client_age <= max_age):
            error = f"Age For {milit_rank} must be between {min_age} and {max_age}, But Customer Age is {client_age}"
            rejections.append(error)
        else:
            acceptances.append(f"Age For {milit_rank} must be between {min_age} and {max_age}, And the Customer Age is {client_age} so he passed age checking")
   
    # 4- Not Retired General Case
    if not client_data["retired"] and not (job in job_age_keys) and not (milit_rank in military_age_keys):
        age_values["maxAge"] = max_age
        age_values["minAge"] = min_age
        age_values["expected"] = f"{min_age}-{max_age}"
        age_values["actual"] = client_age
        if not (min_age <= client_age <= max_age):
            error = f"Age must be between {min_age} and {max_age}, But Customer Age is {client_age}"
            rejections.append(error)
        else:
            acceptances.append(f"Age must be between {min_age} and {max_age}, And the Customer Age is {client_age} so he passed age checking")
           
    return error, acceptances, rejections , age_values