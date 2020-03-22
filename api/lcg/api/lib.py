
import pandas as pd
from django.conf import settings
from api.models import *

TMP_DIR = getattr(settings, "TMP_DIR", None)

def create_customer_ifne(*, inn ,f, i, o=None, dr=None, address_reg=None, adr=None, doc_no):
       c = Customer.objects.filter(inn=inn).first()
       
       if not c:
              c = Customer(inn=inn, f=f, i=i, o=o, dr=dr, address_reg=address_reg, doc_no=doc_no)
              c.save()
       return c

def create_address_ifne(*, addr, type, customer):
       adr_type = Ref_address_type.objects.filter(id=type).first()
       adr = Customer_address.objects.filter(addr=addr, type=adr_type, customer=customer).first()
       
       if not adr:
              adr = Customer_address(addr=addr, type=adr_type, customer=customer)
              adr.save()
       return adr

def create_phone_ifne(*, phone, type, customer: Customer):
       ph_type = Ref_phone_type.objects.filter(id=type).first()
       ph = Customer_phone.objects.filter(phone=phone, type=ph_type, customer=customer).first()
       
       if not ph:
              ph = Customer_phone(phone=phone, type=ph_type, customer=customer)
              ph.save()
       return ph



def load_main(l_id):
       sheetName = 'реестр'
       data_xls = pd.read_excel(TMP_DIR+'temp_register.xlsx', sheetName, index_col=None, header=0,nrows=None )
       l = Loader.objects.get(pk=l_id)
       
       i = 0
       loaded = 0
       rejected = 0
       for index, row in data_xls.iterrows():
              # break
              i += 1
              print('[i] row["ИНН"]=', str(row['ИНН']))
              print('[i] row["Дата рождения"]=', str(row['Дата рождения']))

              
              c = create_customer_ifne(
                     inn=row['ИНН'], f=row['Фамилия'], i=row['Имя'], 
                     o=row['Отчество'] if pd.notnull(row['Отчество']) else None,
                     dr=row['Дата рождения'] if pd.notnull(row['Дата рождения']) else None,
                     doc_no=row['Номер удостоверения личности'] if pd.notnull(row['Номер удостоверения личности']) else None
              )

              if pd.notnull(row['Адрес регистрации']):
                     adr = create_address_ifne(addr=row['Адрес регистрации'], type=1, customer=c)                
                     c.address_reg=adr.id
                     c.save()

              print('[i] row["Номер договора"]=', str(row['Номер договора']))
              print('[i] row["Дата договора"]=', str(row['Дата договора']))
              print('[i] row["Тип продукта"]=', str(row['Тип продукта']))
              a = Agreement.objects.filter(
                            agreement_no=row['Номер договора']
                            , agreement_from=row['Дата договора']                      
                     ).first()
              if not a:
                     a = Agreement(
                            agreement_no=row['Номер договора'], agreement_from=row['Дата договора'], 
                            current_debt=row['Общая сумма взыскиваемой задолженности'], 
                            main_debt=row['основной долг'], initial_debt=row['Сумма выдачи'], 
                            percent=row['проценты'], commission=row['комиссия'], 
                            penalty=row['пеня'], customer_id=c.id, loader=l,
                            product_type=row['Тип продукта'],
                            process_type = Ref_process_type.objects.get(id=1)
                     )
                     a.save()
                     loaded += 1
              else:
                     rejected += 1
       l.status = Ref_load_status.objects.get(pk=2)
       l.items_loaded = loaded
       l.items_rejected = rejected
       l.save()
       return {
              "status": True,
              "rows_checked": i
       }
              
