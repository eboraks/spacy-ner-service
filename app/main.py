from typing import List
from fastapi import FastAPI
from .models import TextQuery, Entities
from .ner_extractor import NerExtractor, EntityLinkerExtractor
import logging, sys, uvicorn, spacy

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)


entityLinker = EntityLinkerExtractor()
ner = NerExtractor()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ner_extractor/")
async def spacy_ner(query: TextQuery) -> List[Entities]:
    if query.text == None:
        logging.warning("Query text is empty")
        raise ValueError("Query text is empty")

    entities1 = ner.identify(query.text)
    entities2 = entityLinker.identify(query.text)
    entities = consolidate(entities1, entities2)
    return entities


def consolidate(ners, entlinker):
    if len(entlinker) == 0:
        return ners

    ner_text = [ent.text for ent in ners]
    el_text = [ent.text for ent in entlinker]

    results = []
    for idx, text in enumerate(ner_text):
        if text in el_text:
            logging.info(f"Consolidate Entities: {text} is in {' '.join(el_text)}")
            results.append(entlinker[el_text.index(text)])
        else:
            logging.info(f"Consolidate Entities: {text} is not in {' '.join(el_text)}")
            results.append(ners[idx])

    return results


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8999)
