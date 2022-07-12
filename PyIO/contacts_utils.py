import csv
import pickle
import json
from contact import Contact


def csv_to_contacts(path, encoding='latin_1'):
    contacts = []

    with open(path, encoding=encoding) as archive:
        reader = csv.reader(archive)

        for line in reader:
            id, name, email = line
            contact = Contact(id, name, email)
            contacts.append(contact)
    return contacts


def contacts_to_pickle(contacts, path):
    with open(path, "wb") as archive:
        pickle.dump(contacts, archive)


def pickle_to_contacts(path):
    with open(path, "rb") as archive:
        contacts = pickle.load(archive)
    return contacts


def contacts_to_json(contacts, path):
    with open(path, "w") as archive:
        json.dump(contacts, archive, default=_contact_to_json)


def _contact_to_json(contact):
    return contact.__dict__


def json_to_contatos(path):
    contacts = []
    with open(path) as archive:
        contacts_json = json.load(archive)
        for contact in contacts_json:
            c = Contact(**contact)
            contacts.append(c)
    return contacts
