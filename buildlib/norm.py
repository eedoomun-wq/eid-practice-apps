"""Answer normalisation. engine/app.js has the same rules in norm(); keep them in step."""
import re

_APOS = re.compile(r"[‘’ʼ`´]")


def norm(s):
    s = (s or "").lower()
    s = _APOS.sub("'", s)
    s = re.sub(r"[“”]", '"', s)
    s = re.sub(r"[–—\-]", " ", s)
    s = re.sub(r"\bcan't\b", "can not", s)
    s = re.sub(r"\bcannot\b", "can not", s)
    s = re.sub(r"\bwon't\b", "will not", s)
    s = re.sub(r"\bshan't\b", "shall not", s)
    s = re.sub(r"n't\b", " not", s)
    s = re.sub(r"'m\b", " am", s)
    s = re.sub(r"'re\b", " are", s)
    s = re.sub(r"'ve\b", " have", s)
    s = re.sub(r"'ll\b", " will", s)
    s = re.sub(r"'d like\b", " would like", s)
    s = re.sub(r"[.,!?;:\"()…]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return fold(s)


# British and American spellings are both accepted: fold them to one form before comparing.
FOLD_WORDS = {
    "color": "colour", "colors": "colours", "favorite": "favourite", "favorites": "favourites",
    "neighbor": "neighbour", "neighbors": "neighbours", "honor": "honour", "flavor": "flavour",
    "behavior": "behaviour", "humor": "humour", "center": "centre", "centers": "centres",
    "theater": "theatre", "theaters": "theatres", "meter": "metre", "meters": "metres",
    "kilometer": "kilometre", "kilometers": "kilometres", "liter": "litre", "liters": "litres",
    "centimeter": "centimetre", "centimeters": "centimetres",
    "traveled": "travelled", "traveling": "travelling", "traveler": "traveller", "travelers": "travellers",
    "canceled": "cancelled", "canceling": "cancelling", "dialed": "dialled", "dialing": "dialling",
    "jewelry": "jewellery", "gray": "grey", "mom": "mum", "program": "programme", "programs": "programmes",
    "pajamas": "pyjamas", "cozy": "cosy", "practicing": "practising", "practiced": "practised",
}
_ZE = re.compile(r"\b([a-z]{3,})iz(e|es|ed|ing|er|ers|ation|ations)\b")


def fold(s):
    s = _ZE.sub(r"\1is\2", s)
    return " ".join(FOLD_WORDS.get(w, w) for w in s.split(" "))


# Cases the browser smoke test also runs through window.__APP.norm, to prove both sides agree.
PARITY_CASES = [
    "She isn’t a teacher.",
    "I'm  from Damascus!",
    "They can't swim",
    "We cannot come.",
    "I won't go?",
    "Twenty-one",
    "You're late, Hadi.",
    "I'd like a coffee",
    "Yes, I am.",
    "It's 7:30 in the morning.",
    "I apologized to my favorite neighbor.",
    "We traveled to the theater center.",
    "Gray jewelry, size 10",
]
