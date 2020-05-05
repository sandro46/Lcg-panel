
from django.conf import settings
from lib import *


agrts = Agreement.objects.all()

for a in agrts:
    print(a.id)
    recalc_debt_strucure(a.id)
