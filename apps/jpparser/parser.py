from translation_table import Pos, Major, Sub


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.core_words = {}

    def parse_core_words(self):
        for i, t in enumerate(self.tokens):
            # filter
            pos = t.part_of_speech()[Pos.MAJOR.value]
            if pos not in core_pos:
                continue

            # handle core word in dict
            dict_form = self.get_dict_form(t)
            if dict_form not in self.core_words:
                self.core_words[dict_form] = CoreWord(dict_form)

            core_word = self.core_words[dict_form]
            core_word.count += 1

            # create compound word
            compound = Compound(i, t)
            ai = i + 1
            while self.is_aux(ai):
                compound.append(ai, self.tokens[ai])
                ai += 1

            core_word.compounds.append(compound)

    def get_dict_form(self, t):
        if t.part_of_speech()[1] == Sub.NUMERAL.value:
            return t.surface()

        return t.normalized_form()

    def is_aux(self, token_idx):
        if len(self.tokens) < token_idx:
            return False

        pos = self.tokens[token_idx].part_of_speech()

        # filter particles
        if pos[Pos.SUB.value] == Sub.CONJUNCTIVE_PARTICLE.value:
            return True

        # append auxiliary verbs
        if pos[Pos.MAJOR.value] == Major.AUX_VERB.value:
            return True

        if pos[Pos.MAJOR.value] == Major.SUFFIX.value:
            return True

        return False


class CoreWord:
    def __init__(self, word):
        self.word = word
        self.count = 0
        self.compounds = []


class Compound:
    def __init__(self, idx, stem_token):
        self.idx = idx
        self.aux_indices = []
        self.word = stem_token.surface()
        self.reading = stem_token.reading_form()
        self.begin = stem_token.begin()
        self.end = self.begin

    def append(self, idx, aux_token):
        self.aux_indices.append(idx)
        self.word += aux_token.surface()
        self.reading += aux_token.reading_form()
        self.end = aux_token.end()

    def get_token_range(self):
        end = self.aux_indices[-1] if len(self.aux_indices) > 0 else self.idx
        end += 1
        return slice(self.idx, end)


core_pos = [Major.NOUN.value, Major.VERB.value, Major.ADJECTIVE.value,
            Major.ADJECTIVAL_NOUN.value, Major.ADVERB.value]
