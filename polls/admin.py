from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    """
    * admin.StackedInline mostra em blocos.
    * admin.TabularInline mostra em tabelas.
    """
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    """
    * fields e fieldsets nao podem estar declarados juntos no modelo.
    * 'classes': ['collapse'] exibe e esconde o fieldset.
    * list_display sao as colunas que vao aparecer na listagem do objeto.
    * list_filter criar uma coluna de filtro a direita.
    """

    # fields = ['pub_date', 'question']

    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Poll, PollAdmin)