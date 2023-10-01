from db_config import CRM

def select_action():
    return input("===== Welcome to CRM Application =====\n[S]how: Show all users info\n[A]dd: Add new user\n[Q]uit: Quit The Application\n======================================")


def add_action():
    user_name = input("New user name >")
    user_age = input("New user age >")

    crm = CRM(name=user_name, age=user_age) 
    crm.save()
    print(f"Add new user:{user_name}") 


def show_action():
    for crm in CRM.select():
        print(f"Name: {crm.name} Age: {crm.age}")


def finish_action():
    print("Bye!")


def find_action(name):
    crm = CRM.get_or_none(CRM.name == name)
    return crm


def main():
    while True:
        select = select_action()

        if select == "S":
            show_action()
            continue

        if select == "A":
            add_action()
            continue

        if select == "Q":
            finish_action()
            break


        print("command not found")


if __name__ == "__main__":
    main()