import config

def clear_log(log_file_path):
	file = open(log_file_path, 'w')
	file.write('')
	file.close()


def log(log_file_path, message):
	file = open(log_file_path, 'a')
	file.write('\n\n\n' + message)
	file.close()


def attachment_on_unseen_email(log_file_path, email_data):
	message = "Attachment on a previously unseen email address.  Data: " + str(email_data)
	log(log_file_path, message)


def invalid_capitulation(log_file_path, seen_email_entry):
	message = "Recieved capitulation from someone with fewer than 10 presumed sent addresses.\nTheir seen data:" + str(seen_email_entry)
	log(log_file_path, message)