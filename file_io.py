import json
import csv


def get_one_column_csv(csv_file_path):
	"""Use when data is all in one column and you want all rows."""
	file = open(csv_file_path, 'r')
	reader_ = csv.reader(file)
	data_list = [row[0] for row in reader_]
	file.close()
	return data_list


def get_json_data(json_file_path):
	file = open(json_file_path, 'r')
	data = json.loads(file.read())
	file.close()
	return data


def write_json_data(json_file_path, data):
	data_json = json.dumps(data)
	json_file = open(json_file_path, 'w')
	json_file.write(data_json)
	json_file.close()


def reset_json_files(csv_file_path, unused_addresses_file_path, seen_email_data_file_path):
	unused_addresses = get_one_column_csv(csv_file_path)
	write_json_data(unused_addresses_file_path, unused_addresses)
	write_json_data(seen_email_data_file_path, [])
