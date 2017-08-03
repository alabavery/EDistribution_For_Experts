import config
#import gmail

def ten_new_addresses(email_address, unused_addresses, seen_email_data):
	assert len(unused_addresses) > 9
	addresses_to_send = unused_addresses[:10]
	del unused_addresses[:10]
	#gmail.send_addresses_email()
	for entry in seen_email_data:
		if entry['email_address'] == email_address:
			entry['sent_voter_addresses'].extend(addresses_to_send)
			return unused_addresses, seen_email_data
	
	new_entry = {'email_address':email_address,'sent_voter_addresses':addresses_to_send}
	seen_email_data.append(new_entry)
	return unused_addresses, seen_email_data

 
def is_capitulation_text(text_content):
	return text_content == config.CAPITULATION_TEXT


def handle_capitulation(email_address, unused_addresses, seen_email_data):
	# gmail.send_capitulation_response(email_address)
	for entry in seen_email_data:
		if entry['email_address'] == email_address:
			assert len(entry['sent_voter_addresses']) > 9
			undone_addresses = entry['sent_voter_addresses'][-10:]
			del entry['sent_voter_addresses'][-10:]
			break
	unused_addresses = undone_addresses + unused_addresses
	return unused_addresses, seen_email_data


def send_to_manual_review(email_data):
	print('\n',"Got email from previous volunteer that did not have attachment and was not capitulation email:",'\n',email_data)


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
		unused_addresses, seen_email_data = ten_new_addresses(email_address, unused_addresses, seen_email_data)
	else:
		if email_data['has_attachment']:
			unused_addresses, seen_email_data = ten_new_addresses(email_address, unused_addresses, seen_email_data)
		else:
			if is_capitulation_text(email_data['text_content']):
				unused_addresses, seen_email_data = handle_capitulation(email_address, unused_addresses, seen_email_data)
			else:
				send_to_manual_review(email_data)

	return unused_addresses, seen_email_data