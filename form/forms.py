from django import forms


class UserForm(forms.Form):

    CHOICES = (('1','1'),('2', '2'),('3', '3'),('4', '4'))
    question_text = forms.CharField(label='Question',
                                    widget=forms.TextInput(attrs={'class':'input-class'}))
    option1 = forms.CharField(label='Option 1')
    option2 = forms.CharField(label='Option 2')
    option3 = forms.CharField(label='Option 3')
    option4 = forms.CharField(label='Option 4')
    correct_opt = forms.CharField(widget=forms.Select(choices=CHOICES))
    extra_field_count = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(0,int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['option{index}'.format(index=index+5)] = \
                forms.CharField(required=False)