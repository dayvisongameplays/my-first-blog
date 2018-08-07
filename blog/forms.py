#Primeiro precisamos importar o módulo de formulários do Django
#(from django import forms) e, obviamente, nosso modelo Post (from .models import Post).

from django import forms
from .models import Post


#PostForm, como você já deve suspeitar, é o nome do nosso formulário. Precisamos dizer ao Django que este formulário é um ModelForm
# (assim o Django pode fazer a mágica pra gente) - o forms.ModelForm é o responsável por isso.
class PostForm(forms.ModelForm):

#Segundo, nós temos a classe Meta onde dizemos
# ao Django qual modelo deveria ser usado para criar este formulário (model = Post).
    class Meta:
        model = Post
        fields = ('title', 'text')