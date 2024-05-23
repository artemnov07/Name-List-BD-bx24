from fast_bitrix24.server_response import ErrorInServerResponseException


def add_field(bx):
    try:
        params = {
            "FIELD_NAME": "GENDER",
            "EDIT_FORM_LABEL": "Пол",
            "LIST_COLUMN_LABEL": "Пол",
            "USER_TYPE_ID": "string",
            "XML_ID": "GENDER",
        }
        gender = bx.call('crm.contact.userfield.add', params)
        return gender
    except ErrorInServerResponseException:
        pass


def get_data_contacts(bx):
    params = {'SELECT': ['ID', 'NAME']}
    contacts = bx.get_all('crm.contact.list', params)
    return contacts