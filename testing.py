from core_logic import *
from file_io import *
from config import *
import random


# unused_addresses = get_json_data("Batch1 - Two Votes.json")
# seen_email_data = []


def make_an_email(address, attach, txt):
	 return {'email_address':address,'has_attachment':attach,'text_content':txt}


def generate_email_data():
	address_chooser = random.randint(0,10)
	if address_chooser < 8:
		email_address = str(random.randint(0,3)) + "@gmail.com"
	else:
		email_address = str(random.randint(4,7)) + "@gmail.com"
	
	attachment = random.choice([True, False])
	txt_chooser = random.randint(0,10)
	if txt_chooser < 7:
		txt = "hello"
	else:
		txt = "code red"
	return make_an_email(email_address, attachment, txt)
