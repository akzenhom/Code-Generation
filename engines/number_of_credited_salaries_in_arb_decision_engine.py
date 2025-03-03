def is_bank_statement_required(data):
    return data.get('Number of Credited Salaries in ARB', {}).get('IsBankStatmentRequired', False)