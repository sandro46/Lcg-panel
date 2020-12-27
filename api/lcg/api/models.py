from django.db import models
from django.utils import timezone

# Create your models here.

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class Ref_load_status(models.Model):
    name = models.CharField(max_length=50)
    
class Ref_load_type(models.Model):
    name = models.CharField(max_length=50)

class Loader(models.Model):    
    
    file_name = models.CharField(max_length=100)
    type =  models.ForeignKey(Ref_load_type, on_delete=models.CASCADE)
    status =  models.ForeignKey(Ref_load_status, on_delete=models.CASCADE)
    items_loaded = models.IntegerField(default=0)
    items_rejected = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):    
    
    inn = models.CharField(max_length=20)
    f = models.CharField(max_length=50)
    i = models.CharField(max_length=50)
    o = models.CharField(max_length=50, null=True)
    dr = models.DateField(null=True)
    doc_no = models.CharField(max_length=50, null=True)
    address_live = models.IntegerField(null=True)
    address_reg = models.IntegerField(null=True)
    main_phone = models.IntegerField(null=True)
    created = models.DateField(auto_now_add=True)
  
class Ref_region(models.Model):
    name = models.CharField(max_length=511)

class Ref_address_type(models.Model):
    name = models.CharField(max_length=50)

class Customer_address(models.Model):
    
    addr = models.CharField(max_length=511)
    customer = models.ForeignKey(Customer, related_name="fk_address_customer_id", on_delete=models.CASCADE)
    type = models.ForeignKey(Ref_address_type, related_name="fk_ref_address_type_id", on_delete=models.CASCADE)
    index = models.IntegerField(null=True)
    deactivated = models.CharField(max_length=1, default='N')
    created = models.DateField(auto_now_add=True)


class Ref_phone_type(models.Model):
    name = models.CharField(max_length=100)

class Customer_phone(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    type = models.ForeignKey(Ref_phone_type, on_delete=models.CASCADE)
    deactivated = models.CharField(max_length=1, default='N')
    created = models.DateField(auto_now_add=True)

class Ref_csi(models.Model):
    fio = models.CharField(max_length=100)
    region = models.ForeignKey(Ref_region, on_delete=models.CASCADE)
    no = models.CharField(max_length=12, null=True)
    phone = models.CharField(max_length=12, null=True)
    phone2 = models.CharField(max_length=12, null=True)
    addr = models.CharField(max_length=255, null=True)
    index = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=50, null=True)

class Contragent(models.Model):
    name = models.CharField(max_length=100)
    type_info = models.CharField(max_length=100, null=True)
    
class Ref_process_type(models.Model):
    name = models.CharField(max_length=100)


class Agreement(models.Model):
    
    # template = models.ForeignKey(Template, verbose_name="template_link", related_name="fk_template_task", on_delete=models.CASCADE)
    agreement_no = models.CharField(max_length=50)
    agreement_from = models.DateField(auto_now_add=False)
    current_debt = models.FloatField(default=0)
    current_main_debt = models.FloatField(default=0)
    current_court_costs = models.FloatField(default=0)
    current_percent = models.FloatField(default=0)
    current_commission = models.FloatField(default=0)
    current_penalty = models.FloatField(default=0)
    current_penalty_agreement = models.FloatField(default=0)
    main_debt = models.FloatField(default=0)
    court_costs = models.FloatField(default=0)
    initial_debt = models.FloatField(default=0)
    percent = models.FloatField(default=0)
    commission = models.FloatField(default=0)
    penalty = models.FloatField(default=0)
    penalty_agreement = models.FloatField(default=0)
    product_type = models.CharField(max_length=255, null=True)
    customer = models.ForeignKey(Customer, related_name="fk_agreement_customer_id", on_delete=models.CASCADE)
    loader = models.ForeignKey(Loader, on_delete=models.CASCADE)
    contragent = models.ForeignKey(Contragent, related_name="fk_agreement_contragent_id", on_delete=models.CASCADE, null=True)
    process_type = models.ForeignKey(Ref_process_type, on_delete=models.CASCADE)
    csi = models.ForeignKey(Ref_csi, on_delete=models.CASCADE, null=True)
    ispol_date = models.DateField(null=True)
    ispol_doc_no = models.CharField(max_length=20, null=True)
    arrest_of_salary = models.CharField(max_length=1, default='N')
    arrest_of_property = models.CharField(max_length=1, default='N')
    arrest_of_accounts = models.CharField(max_length=1, default='N')
    arrest_of_deparure = models.CharField(max_length=1, default='N')
    created = models.DateField(auto_now_add=True)
    notary_id = models.IntegerField(null=True)
    nadpis_doc_no = models.CharField(max_length=100, null=True)
    nadpis_initial_date = models.DateField(null=True)
    nadpis_start_date = models.DateField(null=True)
    give_csi_dt = models.DateField(null=True)
    recall_csi_dt = models.DateField(null=True)
    stop_actions_csi_dt = models.DateField(null=True)
    return_ispol_doc_dt = models.DateField(null=True)

    formfield_overrides = {
        models.DateField: {'input_formats': ('%d.%m.%Y',)},
    }


class Csi_actions(models.Model):
    """Исторя действий ЧСИ"""

    csi = models.ForeignKey(Ref_csi, on_delete=models.CASCADE)
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE)

    arrest_of_salary = models.CharField(max_length=1, default='N')    
    arrest_of_property = models.CharField(max_length=1, default='N')
    arrest_of_accounts = models.CharField(max_length=1, default='N')
    arrest_of_deparure = models.CharField(max_length=1, default='N')

    give_csi_dt = models.DateField(null=True)
    recall_csi_dt = models.DateField(null=True)
    stop_actions_csi_dt = models.DateField(null=True)
    return_ispol_doc_dt = models.DateField(null=True)
    
    comment = models.TextField(null=True)

    created = models.DateField(auto_now_add=True)
    
    formfield_overrides = {
        models.DateField: {'input_formats': ('%d.%m.%Y',)},
    }

    
class Payment(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE)
    amount = models.FloatField()
    start_court_costs = models.FloatField(null=True)
    start_main_debt = models.FloatField(null=True)
    start_percent = models.FloatField(null=True)
    start_commission = models.FloatField(null=True)
    start_penalty = models.FloatField(null=True)
    start_penalty_agreement = models.FloatField(null=True)
    end_court_costs = models.FloatField(null=True)
    end_main_debt = models.FloatField(null=True)
    end_percent = models.FloatField(null=True)
    end_commission = models.FloatField(null=True)
    end_penalty = models.FloatField(null=True)
    end_penalty_agreement = models.FloatField(null=True)
    created = models.DateField(auto_now_add=False)
    load_dt = models.DateField(auto_now_add=True, null=True)

class Ref_contact_type(models.Model):
    name = models.CharField(max_length=100)

class Ref_contact_result(models.Model):
    name = models.CharField(max_length=100)

class Contact(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE)
    phone = models.ForeignKey(Customer_phone, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Ref_contact_type, on_delete=models.CASCADE, null=True)
    result = models.ForeignKey(Ref_contact_result, on_delete=models.CASCADE, null=True)
    installment_amt = models.FloatField(null=True)
    installment_dt_to = models.DateField(null=True)
    comment = models.TextField(null=True)
    created = models.DateField(auto_now_add=True)
