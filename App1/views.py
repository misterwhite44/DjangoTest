from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': "Bienvenue sur Django",
        'list_pokemon': [
            {'name': 'Pikachu', 'type': 'Électrique'},
            {'name': 'Salamèche', 'type': 'Feu'},
            {'name': 'Bulbizarre', 'type': 'Plante'}
        ],       
        'Age': 21
    }
    return render(request, 'index.html', context)


def contact(request):
    content = """
    <h2>Contactez-nous</h2>
    <form method="post" action="/submit-contact/">
        <label for="email">Email :</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        <label for="message">Message :</label>
        <textarea id="message" name="message" rows="4" cols="50" required></textarea>
        <br><br>
        <button type="submit">Envoyer</button>
    </form>
    """
    return HttpResponse(content)

def result(request, number):
    return HttpResponse(f"Le numéro est : {number}")
