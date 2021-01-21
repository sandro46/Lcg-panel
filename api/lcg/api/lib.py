
import pandas as pd
from django.conf import settings
from api.models import *
from next_prev import next_in_order, prev_in_order

TMP_DIR = getattr(settings, "TMP_DIR", None)


def recalc_all_agrts():
       agrts = Agreement.objects.all()

       for a in agrts:
              print(a.id)
              recalc_debt_strucure(a.id)

def decrease_debt(remains, sum):
       """Вычитает сумму из остатка и возвращает, оба параметра после вычислений"""
       if remains >= sum:
              remains = remains - sum
              sum = 0
       else:
              sum = sum-remains
              remains = 0
       return remains, sum

def recalc_debt_strucure(agreement_id):
       """Пересчёт структуры долга после платежа с записью в базу данных"""
       a = Agreement.objects.filter(id=agreement_id).first()
       payments = Payment.objects.filter(agreement=a).order_by('created', 'id')
       if len(payments) == 0:
              a.current_court_costs = a.court_costs
              a.current_main_debt = a.main_debt
              a.current_percent = a.percent
              a.current_commission = a.commission
              a.current_penalty = a.penalty
              a.current_penalty_agreement = a.penalty_agreement
              a.current_debt = a.court_costs+a.main_debt+a.percent+a.commission+a.penalty
              a.save()
              return
       i=0
       for pay in payments:
              i+=1
              remains = pay.amount
              if i == 1:
                     court_costs = a.court_costs
                     percent = a.percent
                     commission = a.commission
                     penalty = a.penalty
                     main_debt = a.main_debt
                     penalty_agreement = a.penalty_agreement

                     start_court_costs = a.court_costs
                     start_main_debt = a.main_debt
                     start_percent = a.percent 
                     start_commission = a.commission
                     start_penalty = a.penalty
                     start_penalty_agreement = a.penalty_agreement
              else:
                     last_p = prev_in_order(pay, qs=payments)

                     court_costs = last_p.end_court_costs
                     percent = last_p.end_percent
                     commission = last_p.end_commission
                     penalty = last_p.end_penalty
                     penalty_agreement = last_p.end_penalty_agreement
                     main_debt = last_p.end_main_debt

                     start_court_costs = last_p.end_court_costs
                     start_main_debt = last_p.end_main_debt
                     start_percent = last_p.end_percent
                     start_commission = last_p.end_commission
                     start_penalty = last_p.end_penalty
                     start_penalty_agreement = last_p.end_penalty_agreement
              if court_costs > 0:
                     remains, court_costs = decrease_debt(remains, court_costs)
              print('[i] remains after costs = ', remains)
              if remains > 0 and penalty > 0:
                     remains, penalty = decrease_debt(remains, penalty)
              print('[i] remains after penalty = ', remains)
              if remains > 0 and penalty_agreement > 0:
                     remains, penalty_agreement = decrease_debt(remains, penalty_agreement)
              print('[i] remains after penalty_agreement = ', remains)
              if remains > 0 and commission >0:
                     remains, commission = decrease_debt(remains, commission)
              print('[i] remains after commission = ', remains)
              if remains > 0 and percent > 0:
                     remains, percent = decrease_debt(remains, percent)
              print('[i] remains after percent = ', remains)
              if remains > 0:
                     main_debt = main_debt-remains

              pay.start_court_costs=start_court_costs 
              pay.start_main_debt = start_main_debt
              pay.start_percent = start_percent
              pay.start_commission = start_commission
              pay.start_penalty = start_penalty
              pay.start_penalty_agreement = start_penalty_agreement
              pay.end_court_costs = court_costs
              pay.end_main_debt = main_debt
              pay.end_percent = percent
              pay.end_commission = commission
              pay.end_penalty = penalty
              pay.end_penalty_agreement = penalty_agreement
              pay.save()
              
              a.current_court_costs = court_costs
              a.current_main_debt = main_debt
              a.current_percent = percent
              a.current_commission = commission
              a.current_penalty = penalty
              a.current_debt = court_costs+main_debt+percent+commission+penalty+penalty_agreement
              a.save()
       

def create_customer_ifne(*, inn ,f, i, o=None, dr=None, address_reg=None, adr=None, doc_no):
       c = Customer.objects.filter(inn=inn).first()
       
       if not c:
              c = Customer(inn=inn, f=f, i=i, o=o, dr=dr, address_reg=address_reg, doc_no=doc_no)
       else:
              c.inn = inn
              c.f = f
              c.i = i
              c.o = o
              c.dr = dr
              c.address_reg = address_reg
              c.adr = adr,
              c.doc_no=doc_no
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


       

def add_payments(l_id):
       sheetName = 'Sheet1'
       data_xls = pd.read_excel(TMP_DIR+'temp_register.xlsx',
                                   sheetName, index_col=None, header=0, nrows=None)
       l = Loader.objects.get(pk=l_id)
       i = 0
       loaded = 0
       rejected = 0
       for index, row in data_xls.iterrows():
              print('[i] Current row is ', row)
              if pd.isnull(row['Сумма платежа']) or pd.isnull(row['Договор']):
                     rejected += 1
                     continue
              row['Сумма платежа'] = str(row['Сумма платежа'])
              row['Сумма платежа'] = float(row['Сумма платежа'].replace(',', '.'))
              remains = row['Сумма платежа']
              a = Agreement.objects.filter(
                  agreement_no=row['Договор']).first()
              if not a:
                     rejected += 1
                     continue
              last_p = Payment.objects.filter(agreement=a).order_by('-created', '-id').first()
              start_court_costs = 0
              start_main_debt = 0
              start_percent = 0
              start_commission = 0
              start_penalty = 0
              court_costs = 0
              main_debt = 0
              percent = 0
              commission = 0
              penalty = 0
              if not last_p:
                  court_costs = a.court_costs
                  percent = a.percent
                  commission = a.commission
                  penalty = a.penalty
                  main_debt = a.main_debt

                  start_court_costs = a.court_costs
                  start_main_debt = a.main_debt
                  start_percent = a.percent
                  start_commission = a.commission
                  start_penalty = a.penalty
              else:
                  court_costs = last_p.end_court_costs
                  percent = last_p.end_percent
                  commission = last_p.end_commission
                  penalty = last_p.end_penalty
                  main_debt = last_p.end_main_debt

                  start_court_costs = last_p.end_court_costs
                  start_main_debt = last_p.end_main_debt
                  start_percent = last_p.end_percent
                  start_commission = last_p.end_commission
                  start_penalty = last_p.end_penalty
                  
              if court_costs > 0:
                     if remains >= court_costs:
                            remains = remains - court_costs
                            court_costs=0
                     else:
                            court_costs = court_costs-remains
                            remains = 0
              print('[i] remains after costs = ', remains)
              if remains > 0 and penalty>0:
                     if remains >= penalty:
                            remains = remains - penalty
                            penalty=0
                     else:
                            penalty = penalty-remains
                            remains = 0
              print('[i] remains after penalty = ', remains)
              if remains > 0 and commission>0:
                     if remains >= commission:
                            remains = remains - commission
                            commission=0
                     else:
                            commission = commission-remains
                            remains = 0
              print('[i] remains after commission = ', remains)
              if remains > 0 and percent > 0:
                     if remains >= percent:
                         remains = remains - percent
                         percent = 0
                     else:
                            percent = percent-remains
                            remains = 0
              print('[i] remains after percent = ', remains)
              if remains > 0:
                     main_debt = main_debt-remains
              
              p = Payment(
                     agreement = a,
                     amount = row['Сумма платежа'],
                     created = row['Дата платежа'],
                     start_court_costs=start_court_costs,                    
                     start_main_debt = start_main_debt,
                     start_percent = start_percent,
                     start_commission = start_commission,
                     start_penalty = start_penalty,
                     end_court_costs = court_costs,
                     end_main_debt = main_debt,
                     end_percent = percent,
                     end_commission = commission,
                     end_penalty = penalty
              )
              p.save()
              recalc_debt_strucure(a.id)

       l.status = Ref_load_status.objects.get(pk=2)
       l.items_loaded = loaded
       l.items_rejected = rejected
       l.save()
       return {
           "status": True,
           "rows_checked": i
       }

def up_finance(l_id):
       sheetName = 'Sheet1'
       data_xls = pd.read_excel(TMP_DIR+'temp_register.xlsx',
                                sheetName, index_col=None, header=0, nrows=None)
       data_xls['Договор'] = data_xls['Договор'].astype(str)
       l = Loader.objects.get(pk=l_id)
       i = 0
       loaded = 0
       rejected = 0
       for index, row in data_xls.iterrows():
              print('[i] Current row is ', row)
              if pd.isnull(row['Договор']):
                     rejected += 1
                     continue
              a = Agreement.objects.filter(agreement_no=row['Договор']).first()
              if not a:
                  rejected += 1
                  continue
              print('[i] Agreement ', a )
              a.current_debt = row['текущий долг'] if not pd.isnull(row['текущий долг']) else a.current_debt
              a.main_debt = row['основной долг'] if not pd.isnull(row['основной долг']) else a.main_debt
              a.percent = row['проценты'] if not pd.isnull(row['проценты']) else a.percent
              a.commission = row['комиссия'] if not pd.isnull(row['комиссия']) else a.commission
              a.penalty = row['пеня'] if not pd.isnull(row['пеня']) else a.penalty
              a.court_costs = row['судебные издержки (гос./пошлина)'] if not pd.isnull(row['судебные издержки (гос./пошлина)']) else a.court_costs
              a.save()

              recalc_debt_strucure(a.id)
       l.status = Ref_load_status.objects.get(pk=2)
       l.items_loaded = loaded
       l.items_rejected = rejected
       l.save()
       return {
           "status": True,
           "rows_checked": i
       }

def change_stage(l_id):
       sheetName = 'реестр'
       data_xls = pd.read_excel(TMP_DIR+'temp_register.xlsx',
                             sheetName, index_col=None, header=0, nrows=None)
       l = Loader.objects.get(pk=l_id)
       i = 0
       loaded = 0
       rejected = 0
       for index, row in data_xls.iterrows():
              print('[i] Current row is ', row)
              if pd.isnull(row['ИНН']) or pd.isnull(row['id стадии']) or pd.isnull(row['Договор']):
                     rejected+=1
                     continue
              c = Customer.objects.filter(inn=row['ИНН']).first()
              if not c:                     
                     rejected+=1
                     continue
              a = Agreement.objects.filter(agreement_no=row['Договор'], customer=c).first()
              if not a:
                  rejected += 1
                  continue
              a.process_type = Ref_process_type.objects.get(id=row['id стадии'])
              a.save()

       l.status = Ref_load_status.objects.get(pk=2)
       l.items_loaded = loaded
       l.items_rejected = rejected
       l.save()
       return {
           "status": True,
           "rows_checked": i
       }


def change_csi_by_agreement(l_id):
       sheetName = 'Лист1'
       data_xls = pd.read_excel(TMP_DIR+'temp_register.xlsx',
                               sheetName, index_col=None, header=0, nrows=None, dtype=str)
       data_xls['Дата закрепления'] = pd.to_datetime(data_xls['Дата закрепления'])
       data_xls['Дата отзыва'] = pd.to_datetime(data_xls['Дата отзыва'])
       data_xls['Дата приостановления действий'] = pd.to_datetime(data_xls['Дата приостановления действий'])
       data_xls['Дата возврата исполнительного листа'] = pd.to_datetime(data_xls['Дата возврата исполнительного листа'])
       
       l = Loader.objects.get(pk=l_id)
       i = 0
       loaded = 0
       rejected = 0
       for index, row in data_xls.iterrows():
              
              if pd.isnull(row['id ЧСИ']) or pd.isnull(row['Договор']):
                     rejected += 1
                     continue
              a = Agreement.objects.filter(agreement_no=row['Договор']).first()
              if not a:
                     rejected += 1
                     continue
              с = Ref_csi.objects.filter(id=row['id ЧСИ']).first()
              if not с:
                  rejected += 1
                  continue
              a.csi = с

              a.give_csi_dt=row['Дата закрепления'] if pd.notnull(row['Дата закрепления']) else None
              a.recall_csi_dt=row['Дата отзыва'] if pd.notnull(row['Дата отзыва']) else None
              a.stop_actions_csi_dt=row['Дата приостановления действий'] if pd.notnull(row['Дата приостановления действий']) else None
              a.return_ispol_doc_dt = row['Дата возврата исполнительного листа'] if pd.notnull(row['Дата возврата исполнительного листа']) else None

              a.save()

       l.status = Ref_load_status.objects.get(pk=2)
       l.items_loaded = loaded
       l.items_rejected = rejected
       l.save()
       return {
           "status": True,
           "rows_checked": i
       }

def load_csi_actions(l_id):
       data_xls = pd.read_excel(TMP_DIR+'temp_register.xlsx', index_col=None, header=0, nrows=None)
       data_xls['Дата'] = pd.to_datetime(data_xls['Дата'])
       data_xls['Status'] = 'OK'

       l = Loader.objects.get(pk=l_id)
       i = 0
       loaded = 0
       rejected = 0
       for index, row in data_xls.iterrows():
              i += 1
              print('[i][load_csi_actions] Current row is ', row)
              if pd.isnull(row['Договор']):
                     data_xls['Status'][index] = 'Error: Нет договора'
                     rejected+=1
                     continue
              a = Agreement.objects.filter(agreement_no=row['Договор']).first()
              if not a:
                     data_xls['Status'][index] = 'Error: Не найден договор'
                     rejected += 1
                     continue
              if not a.csi:
                     data_xls['Status'][index] = 'Error: За делом не закреплён ЧСИ'
                     rejected += 1
                     continue

              obj = Csi_actions(
                     agreement=a,
                     csi=a.csi,

                     arrest_of_salary=('Y' if row['Арест ЗП/Пенсии']=='Y' else 'N'),
                     arrest_of_property=('Y' if row['Арест имущества']=='Y' else 'N'),
                     arrest_of_accounts=('Y' if row['Арест счета']=='Y' else 'N'),
                     arrest_of_deparure=('Y' if row['Ограничение выезда']=='Y' else 'N'),

                     created=row['Дата'],

                     comment=row['КОМЕНТАРИИ'] if row['КОМЕНТАРИИ'] else None,
              )
              obj.save()

       l.status = Ref_load_status.objects.get(pk=2)
       l.items_loaded = loaded
       l.items_rejected = rejected
       l.save()

       report_file_name = 'result_csi_actions.xlsx'
       report_file_path = TMP_DIR + report_file_name

       with pd.ExcelWriter(report_file_path, mode='w') as writer:
              data_xls.to_excel(writer, index=False)

       return {
           "status": True,
           "rows_checked": i,
           "send_report": {
              'content_type': 'application/vnd.ms-excel',
              'filename': report_file_name
           }
       }


def up_court_costs(l_id):
       sheetName = 'Лист1'
       data_xls = pd.read_excel(TMP_DIR+'temp_register.xlsx', sheetName, index_col=None, header=0,nrows=None )
       l = Loader.objects.get(pk=l_id)

       i = 0
       loaded = 0
       rejected = 0
       data_xls['Договор'] = data_xls['Договор'].astype(str)
       for index, row in data_xls.iterrows():
              # break
              i += 1
              print('[i] row["Договор"]=', row['Договор'])

              a = Agreement.objects.filter(agreement_no=row['Договор']).first()
              if not a:
                  rejected += 1
                  continue
              a.court_costs = row['судебные издержки']
              a.save()
              recalc_debt_strucure(a.id)

       l.status = Ref_load_status.objects.get(pk=2)
       l.items_loaded = loaded
       l.items_rejected = rejected
       l.save()
       return {
              "status": True,
              "rows_checked": i
       }


def load_main(l_id):
       sheetName = 'реестр'
       data_xls = pd.read_excel(TMP_DIR+'temp_register.xlsx', sheetName, index_col=None, header=0,nrows=None )
       # data_xls = data_xls.fillna(0)
       l = Loader.objects.get(pk=l_id)
       
       i = 0
       loaded = 0
       rejected = 0
       for index, row in data_xls.iterrows():
              # print(row['Отчество'])
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
              print('[i] row["ID Контрагента"]=', int(str(row['ID Контрагента']).replace(',', '.')) )
              process_type = Ref_process_type.objects.get(id=1)

              # return {
              #        "status": True,
              #        "rows_checked": 20
              # }
              
              a = Agreement.objects.filter(
                     agreement_no=row['Номер договора']
                     , agreement_from=row['Дата договора']                      
              ).first()
              contr = Contragent.objects.filter(id=int(str(row['ID Контрагента']).replace(',', '.'))).first()
              print(row['ID Контрагента'], contr.id, l, process_type)

              row['Общая сумма взыскиваемой задолженности'] = row['Общая сумма взыскиваемой задолженности'] if pd.notnull(row['Общая сумма взыскиваемой задолженности']) else 0
              row['основной долг'] = row['основной долг'] if pd.notnull(row['основной долг'] ) else 0
              row['пеня'] = row['пеня'] if pd.notnull(row['пеня'] ) else 0
              row['проценты'] = row['проценты'] if pd.notnull(row['проценты'] ) else 0
              row['комиссия'] = row['комиссия'] if pd.notnull(row['комиссия'] ) else 0
              row['Платеж за несоблюдение условий договора'] = row['Платеж за несоблюдение условий договора'] if pd.notnull(row['Платеж за несоблюдение условий договора'] ) else 0
              row['Сумма выдачи'] = row['Сумма выдачи'] if pd.notnull(row['Сумма выдачи'] ) else 0
              if not a:
                     a = Agreement(
                            agreement_no=row['Номер договора'], 
                            agreement_from=row['Дата договора'], 
                            current_debt=str(row['Общая сумма взыскиваемой задолженности']).replace(',', '.'), 
                            current_main_debt=str(row['основной долг'] if pd.notnull(row['основной долг'] ) else 0).replace(',', '.'),
                            current_percent=str(row['проценты']).replace(',', '.'),
                            current_commission=str(row['комиссия']).replace(',', '.'),
                            current_penalty=str(row['пеня']).replace(',', '.'),
                            current_penalty_agreement=str(row['Платеж за несоблюдение условий договора']).replace(',', '.'),
                            main_debt=str(row['основной долг']).replace(',', '.'),
                            initial_debt=str(row['Сумма выдачи']).replace(',', '.'),
                            percent=str(row['проценты']).replace(',', '.'),
                            commission=str(row['комиссия']).replace(',', '.'),
                            penalty=str(row['пеня']).replace(',', '.'),
                            contragent=contr,
                            penalty_agreement=str(row['Платеж за несоблюдение условий договора']).replace(',', '.'),
                            customer_id=c.id, loader=l,
                            product_type=row['Тип продукта'],
                            process_type = process_type
                     )
              else:
                     a.agreement_no=row['Номер договора']
                     a.agreement_from=row['Дата договора']
                     a.current_debt=str(row['Общая сумма взыскиваемой задолженности']).replace(',', '.')
                     a.current_main_debt=str(row['основной долг']).replace(',', '.')
                     a.current_percent=str(row['проценты']).replace(',', '.')
                     a.current_commission=str(row['комиссия']).replace(',', '.')
                     a.current_penalty=str(row['пеня']).replace(',', '.')
                     a.current_penalty_agreement=str(row['Платеж за несоблюдение условий договора']).replace(',', '.')
                     a.main_debt=str(row['основной долг']).replace(',', '.')
                     a.initial_debt=str(row['Сумма выдачи']).replace(',', '.')
                     a.percent=str(row['проценты']).replace(',', '.')
                     a.commission=str(row['комиссия']).replace(',', '.')
                     a.penalty = str(row['пеня']).replace(',', '.')
                     a.customer = c
                     a.contragent = contr
                     a.penalty_agreement=str(row['Платеж за несоблюдение условий договора']).replace(',', '.')
                     a.loader=l
                     a.product_type=row['Тип продукта']
                     a.process_type = process_type
       
              a.save()
              recalc_debt_strucure(a.id)
              loaded += 1
       l.status = Ref_load_status.objects.get(pk=2)
       l.items_loaded = loaded
       l.items_rejected = rejected
       l.save()
       return {
              "status": True,
              "rows_checked": i
       }
              
