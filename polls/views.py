from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Question,Environment
from django.template import loader
from django.http import Http404



def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))








def biaoge(request,product_name):
    template = loader.get_template('polls/biaoge.html')
    return HttpResponse(template.render())



def demo(request,product_name):
    template = loader.get_template('polls/demo.htm')
    return HttpResponse(template.render())





def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)






def test(request, product_name):
    try:
        #environment_data = Environment.objects.get(product_name=product_name)
        environment_data_list = Environment.objects.filter(product_name=product_name)        

        template = loader.get_template('polls/biaoge_xiugai.html')
        context = {
            'environment_data_list': environment_data_list,
            'product_name':product_name
        }

        return HttpResponse(template.render(context, request))

        # temperature=environment_data.temperature
        # return HttpResponse("The temperature of product %s is %s." % (product_name,str(temperature)))




    except Question.DoesNotExist:
        raise Http404("Question does not exist")



