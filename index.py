import file_io
import config
import core_logic
import testing
#import gmail

def reset_unused_address_json(csv_file_path, json_file_path):
	# read csv
	# write to json
	pass


def check_continue_conditions(unused_addresses):
	# check wifi
	if len(unused_addresses) < 10:
		print("FEWER THAN TEN ADDRESSES LEFT TO SEND (CONGRATS!!!!!!)")
		return False
	return True


unused_addresses = file_io.get_json_data(config.ADDRESSES_JSON_FILE_NAME) # list of strings
seen_email_data = file_io.get_json_data(config.SEEN_EMAIL_FILE_NAME) # list of {'email':str, 'voter_addresses:' [str]}
#new_email_data = gmail.get_gmail_data() # list of {'email_address':str, 'has_attachment':bool, 'text_content':str}

core_logic.logging.clear_log(config.LOG_FILE_PATH)

new_email_data = []
for simulated_email in range(20):
	new_email_data.append(testing.generate_email_data())


for email_data in new_email_data:
	unused_addresses, seen_email_data = core_logic.handle_email(email_data, unused_addresses, seen_email_data)
	if not check_continue_conditions(unused_addresses): # check that unused_addresses is > 9, wifi connected, etc.
		break

file_io.write_json_data(config.ADDRESSES_JSON_FILE_NAME, unused_addresses)
file_io.write_json_data(config.SEEN_EMAIL_FILE_NAME, seen_email_data)