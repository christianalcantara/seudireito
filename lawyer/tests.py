from django.test import TestCase
from .models import Lawyer
from .validators import validate_telefone

class AdvogadoTestCase(TestCase):
    # def setUp(self):
    #     Advogado.objects.create(usuario_id=1, nome="Christian Douglas", cpf='88815935134', email='chr@gjk.com')

    def teste_telefone_valido(self):
        """Animals that can speak are correctly identified"""
        # lion = Advogado.objects.get(usuario_id=1)
        # self.assertEqual(lion, 'The lion says "roar"')
        validate_telefone('1245')
        validate_telefone('(11)9885-8965')
