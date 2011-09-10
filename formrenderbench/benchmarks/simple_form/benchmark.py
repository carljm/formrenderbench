from django import forms, template
from django.conf import settings

from djangobench.utils import run_benchmark


class SimpleForm(forms.Form):
    one = forms.CharField()
    two = forms.CharField(widget=forms.Textarea)


if settings.NEW_FORM_RENDERING:
    tpl = "{% form myform %}"
else:
    tpl = "{{ form.as_p }}"


def benchmark():
    context = template.Context(
        {
            "myform": SimpleForm()
            }
        )
    t = template.Template(tpl)
    t.render(context)


run_benchmark(
    benchmark,
    syncdb = False,
    meta = {
        "description": "Render a simple two-field form."
        }
    )
