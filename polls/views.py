from django.http import HttpResponse, Http404
from polls.models import Poll
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404


def index(request):
    lastet_poll_list = Poll.objects.order_by('-pub_date')[:5]
    # EXEMPLO: 1
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {'lastest_poll_list': lastet_poll_list})
    # return HttpResponse(template.render(context))

    # EXEMPLO: 2
    context = {'lastest_poll_list': lastet_poll_list}
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    # EXEMPLO: 1
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404

    # EXEMPLO: 2
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)