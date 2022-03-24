from django import forms

from . import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order    #直接取用models中的類別
        fields = ['full_name', 'address', 'postal_code', 'phone']
    def __str__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = '收件者姓名'
        self.fields['address'].label = '收件地址'
        self.fields['postal_code'].label = '郵遞區號'
        self.fields['phone'].label = '聯絡電話'
