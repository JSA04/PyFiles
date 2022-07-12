from contacts_utils import json_to_contatos


# contacts = csv_para_contacts("datas/contacts.csv")
# contacts_to_pickle(contacts, "datas/contacts.pickle")

# contacts = pickle_to_contatos("datas/contacts.pickle")
# contacts_to_json(contacts, "datas/contacts.json")

contacts = json_to_contatos("datas/contacts.json")

for contact in contacts:
    print(f"{contact.id:^2} - {contact.name:9} - {contact.email:30}")
