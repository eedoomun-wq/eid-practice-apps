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
    return s


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
]
