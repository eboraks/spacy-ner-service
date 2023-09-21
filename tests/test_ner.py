from app.ner_extractor import NerExtractor, EntityLinkerExtractor

entityLinker = EntityLinkerExtractor()
ner = NerExtractor()


def test_entities_identification():
    entities = ner.identify(
        "This is a sentence about Obama and Amazon. apple is a company and a fruit. amazon is a company and a river"
    )

    assert len(entities) > 0
    for entity in entities:
        if entity.text == "Amazon":
            assert entity.label == "ORG"


def test_linker_identification():
    entities = entityLinker.identify(
        "This is a sentence about Obama and Amazon. apple is a company and a fruit. amazon is a company and a river"
    )

    assert len(entities) > 0
    for entity in entities:
        assert len(entity.description) > 0
        assert type(entity.description) == str
        assert type(entity.score) == float
        if entity.text == "Amazon":
            assert entity.label == "ORG"
