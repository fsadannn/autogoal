from autogoal.ml import AutoClassifier
from autogoal.datasets import haha
from autogoal.search import Logger, PESearch, ConsoleLogger, ProgressLogger, MemoryLogger
from autogoal.kb import List, Sentence, Tuple, CategoricalVector

classifier = AutoClassifier(
    input=List(Sentence()),
    search_algorithm=PESearch,
    search_iterations=1000,
    search_kwargs=dict(pop_size=10, evaluation_timeout=60, memory_limit=1024 ** 3),
)

class ErrorLogger(Logger):
    def error(self, e:Exception, solution):
        if e and solution:
            with open("errors.log", "a") as fp:
                fp.write(f"solution={repr(solution)}\nerror={repr(e)}\n\n")


memory_logger = MemoryLogger()

X_train, X_test, y_train, y_test = haha.load()


# TESTING
# from autogoal.contrib.nltk._generated import SpaceTokenizer
# from autogoal.kb._data import build_composite_list, Word

# ListClass = build_composite_list(Sentence(), List(Word()))
# algorithm = ListClass(SpaceTokenizer())

# algorithm.run(X_train)
# ---

classifier.fit(X_train, y_train, logger=[ErrorLogger(), ConsoleLogger(), ProgressLogger(), memory_logger])
score = classifier.score(X_test, y_test)
print(score)

print(memory_logger.generation_best_fn)
print(memory_logger.generation_mean_fn)
