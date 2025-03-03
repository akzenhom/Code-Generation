def generate_decision(pdb_data):
    pdbr_value = pdb_data.get('PDBR', {}).get('PDBR', 0.0)
    if pdbr_value > 0.5:
        return "High PDBR"
    elif pdbr_value < 0.3:
        return "Low PDBR"
    else:
        return "Moderate PDBR"

pdb_data = {'PDBR': {'PDBR': 0.45}}
decision = generate_decision(pdb_data)
print(decision)