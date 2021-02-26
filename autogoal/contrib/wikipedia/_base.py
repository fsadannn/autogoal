import wikipedia

from autogoal.kb import Word, Entity, Summary, Flags
from autogoal.utils import nice_repr
from autogoal.experimental.pipeline import AlgorithmBase


@nice_repr
class WikipediaSummary(AlgorithmBase):
    """This class find a word in Wikipedia and return a summary in english.
    """

    def __init__(self):
        pass

    def run(self, input: Word(domain='general', language='english'))-> Summary():
        """This method use Word2Vect of gensim for tranform a word in embedding vector.
        """
        try:
            return wikipedia.summary(input)
        except:
            return ""


@nice_repr
class WikipediaContainsWord(AlgorithmBase):
    """This class find a word in Wikipedia and return a summary in english.
    """

    def __init__(self):
        pass

    def run(self, input: Word(domain='general', language='english'))-> Flags():
        """This method use Word2Vect of gensim for tranform a word in embedding vector.
        """
        return dict(in_wikipedia=bool(wikipedia.search(input)))


@nice_repr
class WikipediaSummarySpanish(AlgorithmBase):
    """This class find a word in Wikipedia and return a summary in Spanish.
    """

    def __init__(self):
        wikipedia.set_lang("es")

    def run(self, input: Word(domain='general', language='spanish'))-> Summary():
        """This method use Word2Vect of gensim for tranform a word in embedding vector.
        """
        try:
            return wikipedia.summary(input)
        except:
            return ""


@nice_repr
class WikipediaContainsWordSpanish(AlgorithmBase):
    """This class find a word in Wikipedia and return a summary in Spanish.
    """

    def __init__(self):
        wikipedia.set_lang("es")

    def run(self, input: Word(domain='general', language='spanish'))-> Flags():
        """This method use Word2Vect of gensim for tranform a word in embedding vector.
        """
        return dict(in_wikipedia=bool(wikipedia.search(input)))
