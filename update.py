from db_config import CRM


def display_all_crm():
    for crm in CRM.select():
        print(crm.id, crm.name)


def update_crm(id):
    crm = CRM.get_by_id(id)
    crm.name = "Tom Ford"
    crm.save()


if __name__ == "__main__":
    display_all_crm()

    id = 3
    crm = CRM.get_by_id(id)
    crm.user = "Tom Ford"
    crm.save()
    update_crm(id)

    display_all_crm()