from pydantic import BaseModel


class TextQuery(BaseModel):
    text: str


# span.text, span.kb_id_, span.label_, span._.description, span._.score
# ('amazon is a company', 'Q3884', 'ORG', ['American multinational technology company'], 2.439415036234588)
class Entities(BaseModel):
    text: str
    label: str
    wikidata_id: str | None = None
    description: str | None = None
    score: float | None = None
