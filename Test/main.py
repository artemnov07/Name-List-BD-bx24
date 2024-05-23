import configparser
from pprint import pprint

from fast_bitrix24 import Bitrix

from database import update_contact_gender
from func import add_field, get_data_contacts


def main(bx, database, user, password):
	add_field(bx)
	contacts = get_data_contacts(bx)
	pprint(contacts)
	update_contact_gender(bx, contacts,  database, user, password)


if __name__ == '__main__':
	config = configparser.ConfigParser()
	config.read("setting.ini", encoding='utf-8')
	database = config.get('db', 'database')
	user = config.get('db', 'user')
	password = config.get('db', 'password')
	webhook = config.get('BITRIX24', 'webhook')
	bx = Bitrix(webhook)
	main(bx, database, user, password)