# library
from library.mortgage.test import accounts

# shortening names that are longer than 32 characters for e2e
E2E_ACCRUED_INT_RECEIVABLE = "ACCRUED_INT_RECEIVABLE"
E2E_INTEREST_RECEIVED = "ACCRUED_INT_RECEIVED"
E2E_CAPITALISED_INT_RECEIVABLE = "CAPITALISED_RECEIVABLE"
E2E_CAPITALISED_INT_RECEIVED = "CAPITALISED_INT_RECEIVED"
E2E_EARLY_REPAYMENT_FEE_INCOME = "EARLY_REPAYMENT_FEE_INCOME"
E2E_PENALTY_INT_RECEIVED = "PENALTY_INTEREST_REC"
E2E_LATE_REPAYMENT_FEE_INCOME = "LATE_REPAYMENT_FEE_INCOME"
E2E_OP_ALLOWANCE_FEE_INCOME = "OP_ALLOWANCE_FEE_INCOME"
internal_accounts_tside = {
    "TSIDE_ASSET": [
        E2E_ACCRUED_INT_RECEIVABLE,
        E2E_CAPITALISED_INT_RECEIVABLE,
    ],
    "TSIDE_LIABILITY": [
        accounts.DEPOSIT_ACCOUNT,
        accounts.INTERNAL_ACCOUNT,
        E2E_INTEREST_RECEIVED,
        E2E_EARLY_REPAYMENT_FEE_INCOME,
        E2E_CAPITALISED_INT_RECEIVED,
        E2E_LATE_REPAYMENT_FEE_INCOME,
        E2E_OP_ALLOWANCE_FEE_INCOME,
        E2E_PENALTY_INT_RECEIVED,
    ],
}
