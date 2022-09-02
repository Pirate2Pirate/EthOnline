### Simple fow showing Belvo's python SDK usage

from pydoc import cli
from belvo.client import Client

# Don't forget to get real values
client = Client("Secret Key ID", "Secret Key PASSWORD", "sandbox")

### FISCAL DATA (verify personhood)

# FAKE SAT
FISCAL_INSTITUTION = 'tatooine_mx_fiscal'
#username and password should be user input instead of hard coded
fiscal_link = client.Links.create(institution=FISCAL_INSTITUTION,username="alguien123",password="passwrod123")

### BANK DATA FOR BALANCES

#FAKE BANK
BANK_INSTITUTION = 'gotham_mx_business'
# username and password should be both user input
bank_link = client.Links.create(institution=BANK_INSTITUTION,username="alguien123",password="contrasena123")
# TODO generate correct date functions
balances = client.Balances.create(bank_link['id'],date_from="2022-09-01",date_to="2022-09-02",save_data=False)

for b in balances:
    print(b['account']['collected_at'],b['account']['balance'])