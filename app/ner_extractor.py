import spacy
import logging
import sys
from typing import Any, List
from app.models import Entities

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)


class EntityLinkerExtractor:
    def __init__(self) -> None:
        self.nlp = spacy.blank("en")
        self.nlp.add_pipe("opentapioca")

    def identify(self, text: str) -> List[Entities]:
        if text == None or len(text) < 3:
            logging.warning("ExtractNER query text is empty")
            raise ValueError("Query text is null")

        results = []
        doc = self.nlp(text)
        for span in doc.ents:
            ent = Entities(
                text=span.text,
                label=span.label_,
                wikidata_id=span.kb_id_,
                description=span._.description[0],
                score=span._.score,
            )
            results.append(ent)
            # print((span.text, span.kb_id_, span.label_, span._.description, span._.score))

        logging.info(f"ExtractNER, Identify {len(results)} entities")
        return results


class NerExtractor:
    def __init__(self) -> None:
        self.nlp = spacy.load("en_core_web_lg")

    def identify(self, text: str) -> List[Entities]:
        if text == None or len(text) < 3:
            logging.warning("ExtractNER query text is empty")
            raise ValueError("Query text is null")

        results = []
        doc = self.nlp(text)
        for span in doc.ents:
            ent = Entities(
                text=span.text,
                label=span.label_,
            )
            results.append(ent)
            # print((span.text, span.kb_id_, span.label_, span._.description, span._.score))

        logging.info(f"ExtractNER, Identify {len(results)} entities")
        return results
