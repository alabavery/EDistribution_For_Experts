import config
import gmail

def ten_new_addresses(email_address, unused_addresses, seen_email_data):
	addresses_to_send = unused_addresses[:10]


def is_capitulation_text(text_content):
	return text_content = config.CAPITULATION_TEXT


def handle_capitulation(email_address):
	# gmail.send_capitulation_response(email_address)
	# 
	pass


def send_to_manual_review(email_data):
	pass


def handle_email(email_data, unused_addresses, seen_email_data):
	"""
	: param email_data -> {'email_address':str, 'has_attachment':bool, 'text_content':str}
	: param unused_addresses -> [str]
	: param seen_email_data -> [{'email_address':str, 'sent_voter_addresses':[str]}]
	"""
	email_address = email_data['email_address']
	seen_email_entry = [entry for entry in seen_email_data if entry['email_address'] == email_address]
	if len(seen_email_entry) == 0:
		assert email_data['has_attachment'] == False # something's gone wrong if there's an attachment on a previously unseen email address
		ten_new_addresses(email_address, unused_addresses, seen_email_data)
	else:
		if email_data['has_attachment']:
			ten_new_addresses(email_address, unused_addresses, seen_email_data)
		else:
			if is_capitulation_text(email_data['text_content']):
				handle_capitulation(email_address)
			else:
				send_to_manual_review(email_data)


	"""
	check if email_data['email_address'] is in seen_email_data
		-- IF NOT (aka it's new address):
		a. get 10 addresses from unused_addresses
		b. add entry in seen_email_data
		c. send email for sending 10 addresses
		-- IF YES (aka it's seen before)
		a. check if attachment
			-- IF NOT:
			1. check if text is "I can't complete" etc.
				--IF NOT:
				1. send to manual review
				IF YES:
				1. reply "thanks for letting us know" etc.
				2. get [-10:] of entry's 'sent_voter_addresses'
				3. add to beginning of of unused_addresses
				4. del [-10:] of entry's 'sent_voter_addresses'
			--IF YES:
			1. same as new email
	"""