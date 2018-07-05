from django import forms



class Formulario(forms.Form):
	nombre = forms.CharField(label='Ingrese Nombre',widget=forms.TextInput(
		attrs={
			'class':'form-control',


		}))

	apellido = forms.CharField(label='Ingrese Apellido',widget=forms.TextInput(
		attrs={
			'class':'form-control',


		}))
	rut = forms.CharField(label='Ingrese RUT',widget=forms.TextInput(
		attrs={
			'class':'form-control',


		}))
	direccion = forms.CharField(label='Ingrese Direccion',widget=forms.TextInput(
		attrs={
			'class':'form-control',


		}))
	puntaje_psu = forms.IntegerField(label='Ingrese Puntaje_PSU',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'number'



		}))
	username = forms.CharField(label='Ingrese username',widget=forms.TextInput(
		attrs={
			'class':'form-control',


		}))
	password = forms.CharField(label='Ingrese Password',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'password'


		}))
	password_valida = forms.CharField(label='Comprobar Password',widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'type':'password'


			}))
	email = forms.CharField(label='Ingrese Email',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'mail',


		}))
