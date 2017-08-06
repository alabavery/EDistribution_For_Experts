import config
import email_logging
#import gmail


def ten_new_addresses(email_address, unused_addresses, seen_email_data):
	addresses_to_send = unused_addresses[:10]
	del unused_addresses[:10]
	
	gmail.send_addresses_email(config.APPLICATION_EMAIL, 
								email_address,
								config.NEW_ADDRESSES_SUBJECT, 
								addresses_to_send,
								config.NEW_ADDRESSES_TEXT,
								gmail_client)

	for entry in seen_email_data:
		if entry['email_address'] == email_address:
			entry['sent_voter_addresses'].extend(addresses_to_send)
			return unused_addresses, seen_email_data
	
	new_entry = {'email_address':email_address,'sent_voter_addresses':addresses_to_send,'active':'y'}
	seen_email_data.append(new_entry)
	return unused_addresses, seen_email_data

 
def is_capitulation_text(text_content):
	for permutation in ['code red', 'codered', 'code-red']:
		if permutation in text_content.lower():
			return True
	return False


def handle_capitulation(email_address, unused_addresses, seen_email_data):
	#gmail.send_capitulation_response(email_address)
	for entry in seen_email_data:
		if entry['email_address'] == email_address:
			
			if len(entry['sent_voter_addresses']) < 10:
				print("Invalid capitulation of " + email_address + "logged")
				email_logging.invalid_capitulation(config.LOG_FILE_PATH, entry)
				return

			undone_addresses = entry['sent_voter_addresses'][-10:]
			del entry['sent_voter_addresses'][-10:]
			entry['active'] = 'n'
			break

	unused_addresses = undone_addresses + unused_addresses
	return unused_addresses, seen_email_data


def handle_email(email_data, unused_addresses, seen_email_data):
	"""
	: param email_data -> {'email_address':str, 'has_attachment':bool, 'text_content':str}
	: param unused_addresses -> [str]
	: param seen_email_data -> [{'email_address':str, 'sent_voter_addresses':[str]}]
	"""
	email_address = email_data['email_address']
	seen_email_entry = [entry for entry in seen_email_data if entry['email_address'] == email_address]
	
	if len(seen_email_entry) == 0:

		if email_data['has_attachment']: # something's gone wrong if there's an attachment on a previously unseen email address
			print("Attachment on unseen, logged")
			email_logging.attachment_on_unseen_email(config.LOG_FILE_PATH, email_data)
		elif is_capitulation_text(email_data['text_content']):
			print("capitulation from unseen, logged")
			email_logging.capitulation_from_unseen_email(config.LOG_FILE_PATH, email_data)
		else:
			print("Sending 10 addresses to unseen email " + email_address)
			unused_addresses, seen_email_data = ten_new_addresses(email_address, unused_addresses, seen_email_data)

	else:
		entry = seen_email_entry[0]

		if entry['active'] == 'n':
			if email_data['has_attachment'] or is_capitulation_text(email_data['text_content']):
				print("Recieved invalid from inactive email, logging.")
				email_logging.invalid_from_inactive_email(config.LOG_FILE_PATH, email_data)
			else:
				print("Sending 10 addresses to previously capitulated email " + email_address)
				unused_addresses, seen_email_data = ten_new_addresses(email_address, unused_addresses, seen_email_data)
				entry['active'] = 'y'

		else:
			if is_capitulation_text(email_data['text_content']):
				print("Handling capitulation of " + email_address)
				unused_addresses, seen_email_data = handle_capitulation(email_address, unused_addresses, seen_email_data)
			elif email_data['has_attachment']:
				print("Sending 10 addresses to seen email " + email_address)
				unused_addresses, seen_email_data = ten_new_addresses(email_address, unused_addresses, seen_email_data)
			else:
				print("Seen email w/no attach or capitulation logged")
				gmail.send_attachment_prompt(config.APPLICATION_EMAIL, 
								email_address,
								config.ATTACHMENT_PROMPT_SUBJECT, 
								config.ATTACHMENT_PROMPT_TEXT,
								gmail_client)
				email_logging.seen_email_no_attachment_no_capitulation(config.LOG_FILE_PATH, email_data)


	return unused_addresses, seen_email_data