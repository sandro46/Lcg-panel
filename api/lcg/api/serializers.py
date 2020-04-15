from rest_framework import serializers

from api.models import *

class LoaderStatusSeraialiser(serializers.ModelSerializer):

    class Meta:
        model = Ref_load_status
        fields = ['name']

class LoaderTypeSeraialiser(serializers.ModelSerializer):

    class Meta:
        model = Ref_load_type
        fields = ['name']

class LoaderSerialize(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d.%m.%Y")
    # created_at = serializers.DateTimeField(format='%Y')
    # type_name = serializers.PrimaryKeyRelatedField(read_only=True)
    type = LoaderTypeSeraialiser(many=False, read_only=True)
    status = LoaderStatusSeraialiser(many=False, read_only=True)
    # author_name = serializers.CharField(source='author.name', read_only=True)
    # id = serializers.ReadOnlyField()

    class Meta:
        model = Loader
        fields = '__all__'
        

class LoaderResponse(serializers.Serializer):
    # created = serializers.DateTimeField(format="%Y-%m-%d")
    pk = serializers.EmailField()

class CustomerSerialize(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'f', 'i', 'o', 'dr', 'inn', 'doc_no']

class CustomerPhoneSerilize(serializers.ModelSerializer):
    
    class Meta:
        model = Customer_phone
        fields = '__all__'

class RefPhoneTypeSerialize(serializers.ModelSerializer):
    
    class Meta:
        model = Ref_phone_type
        fields = '__all__' 

class RefLoadTypeSerialize(serializers.ModelSerializer):

    class Meta:
        model = Ref_load_type
        fields = '__all__' 

class RefRegionSerialize(serializers.ModelSerializer):
    
    class Meta:
        model = Ref_region
        fields = '__all__' 
        
class RefCsiSerialize(serializers.ModelSerializer):
    region = RefRegionSerialize(many=False, read_only=True)

    class Meta:
        model = Ref_csi
        fields = '__all__'
        
class RefProcessTypeSerialize(serializers.ModelSerializer):

    class Meta:
        model = Ref_process_type
        fields = '__all__'

class PaymentSerialize(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'


class AgreementSerialize(serializers.ModelSerializer):
    customer = CustomerSerialize(many=False, read_only=True)
    process_type = RefProcessTypeSerialize(many=False, read_only=True)
    csi = RefCsiSerialize(many=False, read_only=True)
    # agreement_from = serializers.DateTimeField(format="%d.%m.%Y")

    class Meta:
        model = Agreement
        fields = '__all__'

class RefContactTypeSerilize(serializers.ModelSerializer):
    class Meta:
        model = Ref_contact_type
        fields = '__all__'

class RefContactResultSerilize(serializers.ModelSerializer):
    class Meta:
        model = Ref_contact_type
        fields = '__all__'

class ContactSerilize(serializers.ModelSerializer):
    result = RefContactTypeSerilize(many=False, read_only=True)
    type = RefContactResultSerilize(many=False, read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'


