import datetime

from django import forms


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RenewBookForm(forms.Form):
    #날짜를 입력하는 폼에서 날짜를 받아옴
    renewal_date =  forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']


        #오늘보다 이전 날짜를 선택했는지 체크
        if data < datetime.date.today() :
            raise ValidationError(_('Invaild date - renewal in past'))
        

        if data > datetime.date.today() + datetime.timedelta(weeks=4) :
            raise ValidationError(_('Invaild date - renewal more than 4 weeks ahead'))
        

        return data