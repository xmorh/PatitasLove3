from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    precio = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm',
        'min': 0,    # Valor mínimo permitido
        'inputmode': 'numeric',  # Indicar que se espera un valor numérico
    }))

    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'precio', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm'}),
            'marca': forms.TextInput(attrs={'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-pink-500 focus:border-pink-500 focus:z-10 sm:text-sm'}),
        }
