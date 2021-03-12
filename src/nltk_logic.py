import nltk
from src.parser import Parser
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


class NoPunctText():

    def clean_txt(self):
        """Removing punctuation
        """
        tokenizer = RegexpTokenizer(r'\w+')
        list_str = tokenizer.tokenize(Parser().final_text())
        return list_str


class Final_str():
    """Getting string from list without punctuation
            """
    def convert_list_to_string(org_list, seperator=' '):
        """ Convert list to string, by joining all item in list with given separator.
            Returns the concatenated string """
        return seperator.join(org_list)

    full_str = convert_list_to_string(NoPunctText().clean_txt())


class Logic():

    def print_txt(self):
        """Prints .txt file
        """
        print(Parser().final_text())

    def tok_lem_stm(self):
        """ Using tokenize, lemmatize and stemming
        """
        print(sent_tokenize(Parser().final_text()))
        print(f'* Sum of sentences in given .txt file: {len(sent_tokenize(Parser().final_text()))}')
        print(word_tokenize(Final_str().full_str))
        print(f'* Sum of words in given .txt file: {len(word_tokenize(Final_str().full_str))}')

        lemmatizer = WordNetLemmatizer()
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_tokenize(Final_str().full_str)])
        print(f'* Lemmatization result: {lemmatized_output}')

        ps = PorterStemmer()
        words = word_tokenize(Final_str().full_str)
        stem_list = []
        for w in words:
            stem_list.append(ps.stem(w))
        print(f'* Stemming result: {stem_list}')

    def stop_words(self):
        """Removing stopwords
        """
        stop_words = set(stopwords.words('english'))
        filtered_text = [w for w in word_tokenize(Final_str().full_str) if w not in stop_words]
        print(f'* Result of removing stopwords: {filtered_text}')

    def com_words(self):
        """Core logic for common words un .txt file
            """
        allWords = nltk.tokenize.word_tokenize(Final_str().full_str)
        allWordDist = nltk.FreqDist(w.lower() for w in allWords)
        stop_words = set(stopwords.words('english'))
        allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stop_words)
        return allWordExceptStopDist

    def all_cw(self):
        """Getting number of each word appearance in .txt file
                """
        mostCommon = self.com_words().most_common()
        print(f'* Number of each word appearance: {mostCommon}')

    def usr_cw(self):
        """Getting wanted number of most common words in .txt file
                    """
        usr_numb = int(input("Enter wanted number of most common words: "))
        mostCommon_usr = self.com_words().most_common(usr_numb)
        print(f'* Top {usr_numb} common words: {mostCommon_usr}')
