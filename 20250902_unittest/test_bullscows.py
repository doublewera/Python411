import unittest  # Импортируем библиотеку модульного тестирования
import bullscows

# Класс называется TestChototam.....
# он наследует TestCase
class TestBullsCows(unittest.TestCase):

    # Методы, являющиеся тестами конкретных случаев,
    # называются test....., но лучше test_.....
    def test_me(self):
        return #self.assertEqual('foo'.upper(), 'FOO')
    
    # Загадать число из 4 разных цифр
    def test_prepare_4(self):
        chislo = bullscows.prepare()
        #assert len(chislo) == 4
        self.assertEqual(len(chislo), 4)

    # Загадать число из 4 разных цифр
    def test_prepare_unequal(self):
        chislo = bullscows.prepare()
        s = set(chislo)
        self.assertEqual(len(s), 4)

unittest.main()