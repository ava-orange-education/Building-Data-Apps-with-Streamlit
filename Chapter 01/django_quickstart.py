from django import forms
from django.conf import settings
from django.http import HttpResponse
from django.urls import path

# Define settings
settings.configure(DEBUG=True, ROOT_URLCONF=__name__, SECRET_KEY="42")


class NameForm(forms.Form):
    name = forms.CharField(label="Enter your name")


def greet(request):
    greeting = ""
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            greeting = f"Hello, {name}!"
    else:
        form = NameForm()
    return HttpResponse(f"""
        <form method="POST">
            {form.as_p()}
            <input type="submit" value="Submit">
        </form>
        <p>{greeting}</p>
    """)


# Define URL patterns
urlpatterns = [
    path("", greet, name="greet"),
]

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(["django_quickstart.py", "runserver"])
