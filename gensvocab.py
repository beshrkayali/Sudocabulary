"""Generate .svocab from folkets_sv_en_public.xml."""

from lxml import objectify
import random


def gen_svocab():
    tree = objectify.fromstring(open("folkets_sv_en_public.xml", "rb").read())
    word_count = len(tree.word)

    words_to_use = []
    for _ in range(100):
        word = tree.word[random.randint(0, word_count - 1)]
        if hasattr(word, "translation"):
            words_to_use.append(
                {
                    "word": {
                        "value": word.get("value"),
                        "comment": word.get("comment"),
                    },
                    "translation": {
                        "value": word.translation.get("value"),
                        "comment": word.translation.get("comment"),
                    },
                }
            )

    with open(".svocab_base", "r") as origin:
        origin = origin.read()

        words_str = " ".join(
            [
                '"%s%s"'
                % (
                    w["word"]["value"],
                    (" (%s)" % w["word"]["comment"]) if w["word"]["comment"] else "",
                )
                for w in words_to_use
            ]
        )

        wordarray = "( {} )".format(words_str)

        meaning_str = " ".join(
            [
                '"%s%s"'
                % (
                    w["translation"]["value"],
                    (" [%s]" % w["translation"]["comment"])
                    if w["translation"]["comment"]
                    else "",
                )
                for w in words_to_use
            ]
        )

        meaningarray = "( {} )".format(meaning_str)

        origin = origin.replace("%wordarray%", wordarray)
        origin = origin.replace("%meaningarray%", meaningarray)

        with open(".svocab", "w") as svocab:
            svocab.write(origin)

    print("Generated %s words .svocab file" % len(words_to_use))


if __name__ == "__main__":
    gen_svocab()
