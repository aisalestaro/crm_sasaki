from db_config import CRM

# インスタンスを作成してから保存
crm = CRM(name="Bob", age="15")
crm.save()

CRM.create(name="Tom", age="57")
CRM.create(name="Ken", age="73")
