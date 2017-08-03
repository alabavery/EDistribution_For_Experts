from core_logic import *
from file_io import *
from config import *


def make_an_email(address, attach, txt):
	 return {'email_address':address,'has_attachment':attach,'text_content':txt}
an_email = make_an_email("abc@gmail",False,"Hey")
unused_addresses = get_json_data("Batch1 - Two Votes.json")
seen_email_data = []