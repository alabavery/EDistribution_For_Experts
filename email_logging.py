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


def seen_email_no_attachment_no_capitulation(log_file_path, email_data):
	message = "Got email from previous volunteer that did not have attachment and was not capitulation email.\nData: " + str(email_data)
	log(log_file_path, message)


def capitulation_from_unseen_email(log_file_path. email_data):
	message = "Got email from unseen volunteer with capitulation text.\nData: " + str(email_data)
	log(log_file_path, message)


def invalid_from_inactive_email(log_file_path, email_data):
	message = "Got email from inactive volunteer with capitulation text and/or attachment.\nData: " + str(email_data)
	log(log_file_path, message)
