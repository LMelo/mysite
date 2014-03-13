from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Poll, Choice
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse


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
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # REDISPLAY THE POLL VOTING FORM.
        data = {
            'poll': p,
            'error_message': "You didn't select a choice"
        }
        return render(request, 'polls/detail.html', data)
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Essa funcao ajuda a evitar a necessidade de codificar a URL na funcao de ponto de vista.
        # Eh dado o nome da visao que queremos passar o controle e a parcela variavel do padrao de URL
        # que aponta para esse ponto de vista.
        # reverse('poll:results', args=(p.id,)) => '/polls/3/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    # EXEMPLO 1
    # return HttpResponse("You're voting on poll %s." % poll_id)