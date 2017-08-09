import file_io
import config
import core_logic
import testing
import gmail


def check_continue_conditions(unused_addresses):
	# check wifi
	if len(unused_addresses) < 10:
		print("FEWER THAN TEN ADDRESSES LEFT TO SEND (CONGRATS!!!!!!)")
		return False
	return True


unused_addresses = file_io.get_json_data(config.ADDRESSES_JSON_FILE_NAME) # list(str)
seen_email_data = file_io.get_json_data(config.SEEN_EMAIL_FILE_NAME) # list({'email':str, 'voter_addresses:' list(str)})
new_email_data = gmail.get_unread_email_data(config.CLIENT_SECRET_FILE_NAME, config.SCOPES, config.APPLICATION_NAME) # list({'email_address':str, 'has_attachment':bool, 'text_content':str})

core_logic.email_logging.clear_log(config.LOG_FILE_PATH)

gmail_client = gmail.get_gmail_client(config.CLIENT_SECRET_FILE_NAME, config.SCOPES, config.APPLICATION_NAME)

for email_data in new_email_data:
	unused_addresses, seen_email_data = core_logic.handle_email(email_data, unused_addresses, seen_email_data, gmail_client)
	if not check_continue_conditions(unused_addresses): # check that unused_addresses is > 9, wifi connected, etc.
		break

file_io.write_json_data(config.ADDRESSES_JSON_FILE_NAME, unused_addresses)
file_io.write_json_data(config.SEEN_EMAIL_FILE_NAME, seen_email_data)