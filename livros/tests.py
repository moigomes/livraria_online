from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase

from clientes.models import Cliente
from emprestimos.models import Emprestimo
from .models import Livro


class TestMetodosJurosMulta(TestCase):

    def setUp(self):
        self.metodos = Livro()
        self.valor_emprestimo = round(Decimal(100.0), 2)

    def test_valor_da_multa_deve_ser_zero(self):
        """Sem atraso - 0% de multa"""
        quantidade_dias_emprestimo = 3
        valor_multa_obtido = self.metodos.calcular_multa(self.valor_emprestimo, quantidade_dias_emprestimo)
        valor_multa_esperado = round(Decimal(0.0), 2)
        self.assertEqual(valor_multa_esperado, valor_multa_obtido)

    def test_valor_da_multa_deve_ser_tres(self):
        """Até 3 dias - 3% de multa"""
        quantidade_dias_emprestimo = 6
        valor_multa_obtido = self.metodos.calcular_multa(self.valor_emprestimo, quantidade_dias_emprestimo)
        valor_multa_esperado = round(Decimal(3.0), 2)
        self.assertEqual(valor_multa_esperado, valor_multa_obtido)

    def test_valor_da_multa_deve_ser_cinco(self):
        """Acima de 3 dias - 5% de multa"""
        quantidade_dias_emprestimo = 8
        valor_multa_obtido = self.metodos.calcular_multa(self.valor_emprestimo, quantidade_dias_emprestimo)
        valor_multa_esperado = Decimal(5.0)
        self.assertEqual(valor_multa_esperado, valor_multa_obtido)

    def test_valor_da_multa_deve_ser_sete(self):
        """Acima de 5 dias - 7% de multa"""
        quantidade_dias_emprestimo = 9
        valor_multa_obtido = self.metodos.calcular_multa(self.valor_emprestimo, quantidade_dias_emprestimo)
        valor_multa_esperado = round(Decimal(7.0), 2)
        self.assertEqual(valor_multa_esperado, valor_multa_obtido)

    def test_valor_do_juros_deve_ser_zero(self):
        """Sem atraso - 0%"""
        quantidade_dias_emprestimo = 3
        valor_juros_obtido = self.metodos.calcular_juros(self.valor_emprestimo, quantidade_dias_emprestimo)
        valor_juros_esperado = round(Decimal(0.0), 2)
        self.assertEqual(valor_juros_esperado, valor_juros_obtido)

    def test_valor_do_juros_deve_ser_zero_ponto_sessenta(self):
        """Até 3 dias - 0.2% ao dia"""
        quantidade_dias_emprestimo = 6
        valor_juros_obtido = self.metodos.calcular_juros(self.valor_emprestimo, quantidade_dias_emprestimo)
        valor_juros_esperado = round(Decimal(0.60), 2)
        self.assertEqual(valor_juros_esperado, valor_juros_obtido)

    def test_valor_do_juros_deve_ser_dois(self):
        """Acima de 3 dias - 0.4% ao dia"""
        quantidade_dias_emprestimo = 8
        valor_juros_obtido = self.metodos.calcular_juros(self.valor_emprestimo, quantidade_dias_emprestimo)
        valor_juros_esperado = round(Decimal(2), 2)
        self.assertEqual(valor_juros_esperado, valor_juros_obtido)

    def test_valor_do_juros_deve_ser_tres_ponto_cinquenta_e_nove(self):
        """Acima de 5 dias - 0.6% ao dia"""
        quantidade_dias_emprestimo = 9
        valor_juros_obtido = self.metodos.calcular_juros(self.valor_emprestimo, quantidade_dias_emprestimo)
        valor_juros_esperado = round(Decimal(3.6), 2)
        self.assertEqual(valor_juros_esperado, valor_juros_obtido)


class TestLivroModel(TestCase):

    def setUp(self):
        Livro.objects.create(codigo='101010',
                             titulo='Livro Legal',
                             autor='Autor',
                             ano_lancamento=1983,
                             valor_emprestimo=Decimal(100.0))

        Cliente.objects.create(nome="Fulano", telefone='51998989898')

    def test_valor_da_multa_com_tres_dias_de_emprestimo(self):
        emprestimo = Emprestimo.objects.create(livro=Livro.objects.get(codigo='101010'),
                                               cliente=Cliente.objects.get(nome='Fulano'),
                                               data_retirada=(date.today() - timedelta(days=3)))

        emprestimos = Emprestimo.objects.filter(cliente=emprestimo.cliente)
        livro = Livro.get_livros_emprestados(emprestimos=emprestimos)[0]
        valor_multa_obtido = livro.get('multa')
        valor_multa_esperado = round(Decimal(0.0), 2)
        self.assertEqual(valor_multa_esperado, valor_multa_obtido)

    def test_valor_da_multa_com_seis_dias_de_emprestimo(self):
        emprestimo = Emprestimo.objects.create(livro=Livro.objects.get(codigo='101010'),
                                               cliente=Cliente.objects.get(nome='Fulano'),
                                               data_retirada=(date.today() - timedelta(days=6)))

        emprestimos = Emprestimo.objects.filter(cliente=emprestimo.cliente)
        livro = Livro.get_livros_emprestados(emprestimos=emprestimos)[0]
        valor_multa_obtido = livro.get('multa')
        valor_multa_esperado = round(Decimal(3.0), 2)
        self.assertEqual(valor_multa_esperado, valor_multa_obtido)

    def test_valor_da_multa_com_oito_dias_de_emprestimo(self):
        emprestimo = Emprestimo.objects.create(livro=Livro.objects.get(codigo='101010'),
                                               cliente=Cliente.objects.get(nome='Fulano'),
                                               data_retirada=(date.today() - timedelta(days=8)))

        emprestimos = Emprestimo.objects.filter(cliente=emprestimo.cliente)
        livro = Livro.get_livros_emprestados(emprestimos=emprestimos)[0]
        valor_multa_obtido = livro.get('multa')
        valor_multa_esperado = round(Decimal(5.0), 2)
        self.assertEqual(valor_multa_esperado, valor_multa_obtido)

    def test_valor_da_multa_com_nove_dias_de_emprestimo(self):
        emprestimo = Emprestimo.objects.create(livro=Livro.objects.get(codigo='101010'),
                                               cliente=Cliente.objects.get(nome='Fulano'),
                                               data_retirada=(date.today() - timedelta(days=9)))

        emprestimos = Emprestimo.objects.filter(cliente=emprestimo.cliente)
        livro = Livro.get_livros_emprestados(emprestimos=emprestimos)[0]
        valor_multa_obtido = livro.get('multa')
        valor_multa_esperado = round(Decimal(7.0), 2)
        self.assertEqual(valor_multa_esperado, valor_multa_obtido)

    def test_valor_do_juros_com_tres_dias_de_emprestimo(self):
        emprestimo = Emprestimo.objects.create(livro=Livro.objects.get(codigo='101010'),
                                               cliente=Cliente.objects.get(nome='Fulano'),
                                               data_retirada=(date.today() - timedelta(days=3)))

        emprestimos = Emprestimo.objects.filter(cliente=emprestimo.cliente)
        livro = Livro.get_livros_emprestados(emprestimos=emprestimos)[0]
        valor_juros_obtido = livro.get('juros')
        valor_juros_esperado = round(Decimal(0.0), 2)
        self.assertEqual(valor_juros_esperado, valor_juros_obtido)

    def test_valor_do_juros_com_seis_dias_de_emprestimo(self):
        emprestimo = Emprestimo.objects.create(livro=Livro.objects.get(codigo='101010'),
                                               cliente=Cliente.objects.get(nome='Fulano'),
                                               data_retirada=(date.today() - timedelta(days=6)))

        emprestimos = Emprestimo.objects.filter(cliente=emprestimo.cliente)
        livro = Livro.get_livros_emprestados(emprestimos=emprestimos)[0]
        valor_juros_obtido = livro.get('juros')
        valor_juros_esperado = round(Decimal(0.6), 2)
        self.assertEqual(valor_juros_esperado, valor_juros_obtido)

    def test_valor_do_juros_com_oito_dias_de_emprestimo(self):
        emprestimo = Emprestimo.objects.create(livro=Livro.objects.get(codigo='101010'),
                                               cliente=Cliente.objects.get(nome='Fulano'),
                                               data_retirada=(date.today() - timedelta(days=8)))

        emprestimos = Emprestimo.objects.filter(cliente=emprestimo.cliente)
        livro = Livro.get_livros_emprestados(emprestimos=emprestimos)[0]
        valor_juros_obtido = livro.get('juros')
        valor_juros_esperado = round(Decimal(2.0), 2)
        self.assertEqual(valor_juros_esperado, valor_juros_obtido)

    def test_valor_do_juros_com_nove_dias_de_emprestimo(self):
        emprestimo = Emprestimo.objects.create(livro=Livro.objects.get(codigo='101010'),
                                               cliente=Cliente.objects.get(nome='Fulano'),
                                               data_retirada=(date.today() - timedelta(days=9)))

        emprestimos = Emprestimo.objects.filter(cliente=emprestimo.cliente)
        livro = Livro.get_livros_emprestados(emprestimos=emprestimos)[0]
        valor_juros_obtido = livro.get('juros')
        valor_juros_esperado = round(Decimal(3.6), 2)
        self.assertEqual(valor_juros_esperado, valor_juros_obtido)

    def tearDown(self):
        Emprestimo.objects.all().delete()
