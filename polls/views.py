#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from polls.models import Choice, Poll


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


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

        # REVERSE - Essa funcao ajuda a evitar a necessidade de codificar a URL na funcao de ponto de vista.
        # Eh dado o nome da visao que queremos passar o controle e a parcela variavel do padrao de URL
        # que aponta para esse ponto de vista.
        # reverse('poll:results', args=(p.id,)) => '/polls/3/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        # EXEMPLO 1
        # return HttpResponse("You're voting on poll %s." % poll_id)