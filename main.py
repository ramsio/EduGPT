from src.models.model import EduGPT
from src.datasets.corpus_builder import CorpusBuilder

def main():
    model = EduGPT()
    builder = CorpusBuilder()

    builder.build_corpus()
    model.show_information()

if __name__ == "__main__":
    main()
