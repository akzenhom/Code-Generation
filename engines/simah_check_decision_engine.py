class DecisionEngine:
    def __init__(self, config):
        self.config = config

    def check_non_write_off_products_status(self, product_status):
        return product_status in self.config['SIMAH Check']['NonWriteOff_ProductsStatus']

    def check_write_off_non_financial_default_status(self, default_status):
        return default_status in self.config['SIMAH Check']['WriteOff_NonFinancial_DefaultStatus']

    def check_write_off_other_financial_default_status(self, default_status):
        return default_status in self.config['SIMAH Check']['WriteOff_OtherFinancial_DefaultStatus']

    def check_non_write_off_other_financial_products(self, product):
        return product in self.config['SIMAH Check']['NonWriteOff_OtherFinancial_Products']

    def check_write_off_non_financial_products(self, product):
        return product in self.config['SIMAH Check']['WriteOff_NonFinancial_Products']

    def check_non_write_off_checking(self):
        return self.config['SIMAH Check']['NonWriteOff_Checking']

    def check_non_write_off_non_financial_checking(self):
        return self.config['SIMAH Check']['NonWriteOff_NonFinancial_Checking']

    def check_non_write_off_other_financial_checking(self):
        return self.config['SIMAH Check']['NonWriteOff_OtherFinancial_Checking']

    def check_non_write_off_other_financial_max_consecutive_payments(self, consecutive_payments):
        return consecutive_payments <= self.config['SIMAH Check']['NonWriteOff_OtherFinancial_MaxConsecutivePayments']

    def check_non_write_off_other_financial_consecutive_payments_forgiveness(self):
        return self.config['SIMAH Check']['NonWriteOff_OtherFinancial_ConsecutivePaymentsForgivness']

    def check_write_off_checking(self):
        return self.config['SIMAH Check']['WriteOff_Checking']

    def check_write_off_non_financial_checking(self):
        return self.config['SIMAH Check']['WriteOff_NonFinancial_Checking']

    def check_write_off_non_financial_tolerance_amount(self, amount):
        return amount <= self.config['SIMAH Check']['WriteOff_NonFinancial_ToleranceAmount']

    def check_write_off_other_financial_checking(self):
        return self.config['SIMAH Check']['WriteOff_OtherFinancial_Checking']

    def check_write_off_other_financial_tolerance_amount(self, amount):
        return amount <= self.config['SIMAH Check']['WriteOff_OtherFinancial_ToleranceAmount']

    def check_write_off_bounced_cheques_checking(self):
        return self.config['SIMAH Check']['WriteOff_BouncedCheques_Checking']

    def check_write_off_bounced_cheques_is_rejected(self):
        return self.config['SIMAH Check']['WriteOff_BouncedCheques_IsRejected']

    def check_write_off_bounced_cheques_clearing_period(self, days):
        return days <= self.config['SIMAH Check']['WriteOff_BouncedCheques_ClearingPeriod']

    def check_write_off_unexecuted_case_checking(self):
        return self.config['SIMAH Check']['WriteOff_UnExecutedCase_Checking']

    def check_write_off_reject_if_unexecuted_case(self):
        return self.config['SIMAH Check']['WriteOff_RejectIfUnExecutedCase']

    def check_simah_report_validity(self, days_since_report):
        return days_since_report <= self.config['SIMAH Check']['SIMAHReport_Validity']