import frappe
from frappe.utils import nowdate


jv = frappe.new_doc('Journal Entry')
jv.voucher_type = 'Journal Entry'
jv.naming_series = 'ACC-JV-.YYYY.-'
jv.posting_date = nowdate()
jv.company = 'Upeosoft Limited '
jv.remark = 'This is a rest remark for the GitHub example'

#Entry to the Credit Side
jv.append('accounts', {
    'account': "First Account",
    'party_type' : 'Customer',
    'party' : "Customer Name",
    'credit' : float(amount_paid),
    'debit' : float(0),
    'debit_in_account_currency' : float(0),
    'credit_in_account_currency' : float(amount_paid),
})


#Entry to the Debit Side
jv.append('accounts', {
    'account': "Second Account",
    'debit' : float(self.amount_paid),
    'credit' : float(0),
    'credit_in_account_currency': float(0),
    'debit_in_account_currency': float(self.amount_paid)
})


jv.save()
# jv.submit()