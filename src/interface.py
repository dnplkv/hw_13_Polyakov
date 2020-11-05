from src.nltk_logic import Logic


class Interface():
    """Implementing import of correct method after user choice
    """
    def First(self):
        Logic().print_txt()

    def Second(self):
        Logic().tok_lem_stm()

    def Third(self):
        Logic().stop_words()

    def Fourth(self):
        Logic().all_cw()

    def Fifth(self):
        Logic().usr_cw()
