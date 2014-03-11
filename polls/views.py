from django.http import HttpResponse, Http404
from polls.models import Poll
from django.template import RequestContext, loader
from django.shortcuts import render


def index(request):
    lastet_poll_list = Poll.objects.order_by('-pub_date')[:5]
    # PRIMEIRO EXEMPLO
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {'lastest_poll_list': lastet_poll_list})
    # return HttpResponse(template.render(context))

    # SEGUNDO EXEMPLO
    context = {'lastest_poll_list': lastet_poll_list}
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)