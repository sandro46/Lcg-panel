import json, requests, time, re
from datetime import datetime, timedelta
from django.conf import settings
# from snippets.serializers import SnippetSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db.models import Q
from api.models import *
from api.serializers import *
from api.lib import *
from django.core import serializers

TMP_DIR = getattr(settings, "TMP_DIR", None)


def decode_utf8(input_iterator):
    for l in input_iterator:
        yield l.decode('utf-8')


class Agreements(APIView):
    # permission_classes = (AllowAny

    def get(self, request, id=None):
        if id:
            a = Agreement.objects.get(id=id)
            obj = Agreement.objects.filter(customer=a.customer).all().order_by('-id')
            serializer = AgreementSerialize(obj, many=True)
            c = Contact.objects.filter(agreement=obj[0]).all().order_by('-id')
            print('[i] Contact object is ', c)
            # return Response({"payload": 'ok'})
            contacts = ContactSerilize(c, many=True) if len(c)>0 else []
            contacts = contacts.data if len(c)>0 else []
            return Response({"payload": serializer.data, "contacts": contacts})
        else:
            print('[i] Get params is ', request.GET )

            if len(request.GET) == 0:
                obj = Agreement.objects.all().order_by('-id')[:10]
            else:
                if request.GET['search_by_string']:
                    customer = Customer.objects.filter(
                        Q(inn=request.GET['search_by_string']) |
                        Q(f=request.GET['search_by_string'])
                    )
                    print('[i] Customer searched result is :', len(customer))
                    if (customer):
                        obj = Agreement.objects.filter(customer__in=customer).all().order_by('-id')
                    else:
                        obj = Agreement.objects.filter(
                            Q(agreement_no=request.GET['search_by_string']) | 
                            Q(id=request.GET['search_by_string'])
                        ).order_by('-id')
                    if len(obj) == 0:
                        obj = []
        serializer = AgreementSerialize(obj, many=True)
        return Response({"payload": serializer.data})

    def put(self, request, id):
        print('[i] Agreements request is ', request.data)
        print('[i] Agreement process_type is ',
              request.data['agreement']['process_type']
              )

        agreement = Agreement.objects.get(pk=id)
        agreement.csi = Ref_csi.objects.get(pk=request.data['agreement']['csi']['id']) if request.data['agreement']['csi'] else None
        agreement.arrest_of_salary = request.data['agreement']['arrest_of_salary']
        agreement.arrest_of_property = request.data['agreement']['arrest_of_property']
        agreement.arrest_of_accounts = request.data['agreement']['arrest_of_accounts']
        agreement.arrest_of_deparure = request.data['agreement']['arrest_of_deparure']
        agreement.give_csi_dt = datetime.strptime(request.data['agreement']['give_csi_dt'], '%d.%m.%Y').strftime('%Y-%m-%d') if request.data['agreement']['give_csi_dt'] else None
        agreement.recall_csi_dt = datetime.strptime(request.data['agreement']['recall_csi_dt'], '%d.%m.%Y').strftime('%Y-%m-%d') if request.data['agreement']['recall_csi_dt'] else None
        agreement.stop_actions_csi_dt = datetime.strptime(request.data['agreement']['stop_actions_csi_dt'], '%d.%m.%Y').strftime('%Y-%m-%d') if request.data['agreement']['stop_actions_csi_dt'] else None
        agreement.return_ispol_doc_dt = datetime.strptime(request.data['agreement']['return_ispol_doc_dt'], '%d.%m.%Y').strftime('%Y-%m-%d') if request.data['agreement']['return_ispol_doc_dt'] else None
        
        process_type = None
        if isinstance(request.data['agreement']['process_type'], int):
            process_type = process_type = request.data['agreement'].get('process_type', None)  
        if isinstance(request.data['agreement']['process_type'], dict): 
            process_type = request.data['agreement']['process_type'].get('id', None)        
        agreement.process_type = Ref_process_type.objects.get(pk=process_type) if process_type else None

        agreement.save()
        return Response({"payload": "OK"})
    

class Phones(APIView):
    def get(self, request):
        print('[i] Request phones. Params is', request.GET)
        if request.GET['agreement_id']:
            a = Agreement.objects.get(pk=request.GET['agreement_id'])
            obj = Customer_phone.objects.filter(customer=a.customer)
            
        serializer = CustomerPhoneSerilize(obj, many=True)
        return Response({"payload": serializer.data})

class Payments(APIView):
    def get(self, request):
        print('[i] Request phones. Params is', request.GET)
        if request.GET['agreement_id']:
            obj = Payment.objects.filter(agreement=Agreement.objects.get(pk=request.GET['agreement_id']))
            
        serializer = PaymentSerialize(obj, many=True)
        return Response({"payload": serializer.data})


class Contacts(APIView):
    def get(self, request, id):
        obj = Contact.objects.filter(id=id).all().order_by('-id')
        serializer = ContactSerilize(obj, many=True)
        return Response({"payload": serializer.data})
    def post(self, request):
        print('[i] Post data is ', request.data)
        agreement = Agreement.objects.get(pk=request.data['agreement_id'])
        phone = None
        if request.data['new_phone'] and request.data['type'] == 1:
            phone = create_phone_ifne(
                phone=request.data['new_phone'], 
                type=request.data['new_phone_type'], 
                customer=agreement.customer
            )
        obj = Contact( 
            agreement = agreement,
            type=Ref_contact_type.objects.get(pk=request.data['type']) if request.data['type'] else None, 
            result=Ref_contact_result.objects.get(pk=request.data['result']) if request.data['result'] else None,
            comment=request.data['comment'] if request.data['comment'] else None,
            phone = phone,
            installment_amt = request.data['installment_amt'] if request.data['result']==1 and request.data['installment_amt'] else None,
            installment_dt_to = request.data['installment_dt_to'] if request.data['result']==1 and request.data['installment_dt_to'] else None
        )
        obj.save()
        serializer = ContactSerilize(obj)
        return Response({"payload": serializer.data})

class LoaderCtl(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        obj = Loader.objects.all().order_by('-created')
        serializer = LoaderSerialize(obj, many=True)
        return Response({"payload": serializer.data})

    def post(self, request):
        print('[i] Data type id is ',  request.data['type'])
        print('[i] Filename is ',  request.data['file'])
        f = request.data['file']

        with open(TMP_DIR+'temp_register.xlsx', 'wb+') as temp_file:
            for chunk in f.chunks():
                temp_file.write(chunk)
            if(request.data['type'] == '1'):
                l = Loader(
                    file_name=f.name, 
                    type=Ref_load_type.objects.get(pk=request.data['type']), 
                    status=Ref_load_status.objects.get(pk=1)
                )
                l.save()
                res = load_main(l.id)
                l.refresh_from_db()
                data = LoaderSerialize(l).data
                print('[i] Model data is ', data)
            if(request.data['type'] == '2'):
                l = Loader(
                    file_name=f.name, 
                    type=Ref_load_type.objects.get(pk=request.data['type']), 
                    status=Ref_load_status.objects.get(pk=1)
                )
                l.save()
                res = change_stage(l.id)
                l.refresh_from_db()
                data = LoaderSerialize(l).data
                print('[i] Model data is ', data)
            if(request.data['type'] == '3'):
                l = Loader(
                    file_name=f.name,
                    type=Ref_load_type.objects.get(pk=request.data['type']),
                    status=Ref_load_status.objects.get(pk=1)
                )
                l.save()
                res = add_payments(l.id)
                l.refresh_from_db()
                data = LoaderSerialize(l).data
                print('[i] Model data is ', data)
            if(request.data['type'] == '4'):
                l = Loader(
                    file_name=f.name,
                    type=Ref_load_type.objects.get(pk=request.data['type']),
                    status=Ref_load_status.objects.get(pk=1)
                )
                l.save()
                res = change_csi_by_agreement(l.id)
                l.refresh_from_db()
                data = LoaderSerialize(l).data
                print('[i] Model data is ', data)
                
        return Response({"payload": data})


class Ref(APIView):
    def get(self, request):
        print(request.GET)

        if(request.GET.get("type") == 'loaderTypes'):
            obj = Ref_load_type.objects.order_by('id').all()
            serializer = RefLoadTypeSerialize(obj, many=True)
            return Response({"payload": serializer.data})

        if(request.GET.get("type") == 'processTypes'):
            obj = Ref_process_type.objects.order_by('id').all()
            serializer = RefProcessTypeSerialize(obj, many=True)
            return Response({"payload": serializer.data})

        if(request.GET.get("type") == 'contactTypes'):
            obj = Ref_contact_type.objects.order_by('id').all()
            serializer = RefProcessTypeSerialize(obj, many=True)
            return Response({"payload": serializer.data})

        if(request.GET.get("type") == 'contactResults'):
            obj = Ref_contact_result.objects.order_by('id').all()
            serializer = RefProcessTypeSerialize(obj, many=True)
            return Response({"payload": serializer.data})

        if(request.GET.get("type") == 'phone_types'):
            obj = Ref_phone_type.objects.order_by('id').all()
            serializer = RefPhoneTypeSerialize(obj, many=True)
            return Response({"payload": serializer.data})

        if(request.GET.get("type") == 'csi'):
            obj = Ref_csi.objects.order_by('region').all()
            serializer = RefCsiSerialize(obj, many=True)
            return Response({"payload": serializer.data})

        return Response({"payload": {}})


