from django.shortcuts import render, get_object_or_404, render_to_response
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
# Create your views here.

app_name = "form"


def index(request):
    if request.method == 'POST':
        myForm = UserForm(request.POST)

        if myForm.is_bound and myForm.is_valid:
            return HttpResponseRedirect("show")

    else:
        myForm = UserForm()
        print(myForm)
        return render(request, 'form/index.html', {'form':myForm})


def showIndex(request, id):
    stu_name = get_object_or_404(myInfo, pk=id)

    try:
        school = stu_name.myschool_set.all()
    except(KeyError, mySchool.DoesNotExits):
        return HttpResponse("Could not find results!!")
    else:
        return render(request, 'form/show.html', {'school': school, 'name': stu_name.my_first_name })


def show_response(request):
    if request.method == 'POST':
        m = UserForm(request.POST, extra=request.POST.get('extra_field_count'))
        print("="*100)
        print(m)
        print("=" * 100)

        if m.is_valid():
            q_text=m.cleaned_data["question_text"]
            c_opt = m.cleaned_data["correct_opt"]
            QuestionObj = Questions(question_text=q_text, correct_ans=c_opt)
            QuestionObj.save();

            query = Questions.objects.filter(question_text=q_text).last()
            for i,x in enumerate(m.fields):
                #query.options_set.create(option=m.cleaned_data["option"+i])
                index = "option"+ str(i)

                try:
                    option = query.options_set.create(option=m.cleaned_data[index])
                    print(index)
                except KeyError:
                    print("Does Not Exists!")

            return HttpResponseRedirect('show')
        else:
            print(m.errors)
            return HttpResponse("Could Not Save Data Because it was not valid!")

    else:
        questions = Questions.objects.all()

        return render(request, 'form/show.html', {'questions':questions})