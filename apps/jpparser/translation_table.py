from enum import Enum


class Pos(Enum):
    MAJOR = 0
    SUB = 1
    SUB2 = 2
    SUB3 = 3
    CONJ_TYPE = 4
    CONJ_FORM = 5


class Major(Enum):
    NOUN = '名詞'
    VERB = '動詞'
    ADJECTIVE = '形容詞'
    ADJECTIVAL_NOUN = '形状詞'
    ADVERB = '副詞'
    PRONOUN = '代名詞'
    PARTICLE = '助詞'
    AUX_VERB = '助動詞'
    CONJUGATION = '接続詞'
    INTERJECTION = '感動詞'
    PRENOM_ADJECTIVE = '連体詞'
    PREFIX = '接頭辞'
    SUFFIX = '接尾辞'
    SYMBOL = '補助記号'
    WHITE_SPACE = '空白'


MAJOR_EN = {
    Major.NOUN.value: 'Noun',
    Major.VERB.value: 'Verb',
    Major.ADJECTIVE.value: 'Adjective',
    Major.ADJECTIVAL_NOUN.value: 'Na-Adjective',
    Major.ADVERB.value: 'Adverb',
    Major.PRONOUN.value: 'Pronoun',
    Major.PARTICLE.value: 'Particle',
    Major.AUX_VERB.value: 'Auxiliary verb',
    Major.CONJUGATION.value: 'Conjugation',
    Major.INTERJECTION.value: 'Interjection',
    Major.PRENOM_ADJECTIVE.value: 'Prenominal Adjective',
    Major.PREFIX.value: 'Prefix',
    Major.SUFFIX.value: 'Suffix',
    Major.SYMBOL.value: 'Symbol',
    Major.WHITE_SPACE.value: 'White Space'
}

MAJOR_RU = {
    Major.NOUN.value: 'Существительное',
    Major.VERB.value: 'Глагол',
    Major.ADJECTIVE.value: 'Прилагательное',
    Major.ADJECTIVAL_NOUN.value: 'Na-Прилагательное',
    Major.ADVERB.value: 'Наречие',
    Major.PRONOUN.value: 'Местоимение',
    Major.PARTICLE.value: 'Частица',
    Major.AUX_VERB.value: 'Вспомогательный глагол',
    Major.CONJUGATION.value: 'Спряжение',
    Major.INTERJECTION.value: 'Междометие',
    Major.PRENOM_ADJECTIVE.value: 'Преноминиальное прилагательное',
    Major.PREFIX.value: 'Префикс',
    Major.SUFFIX.value: 'Суффикс',
    Major.SYMBOL.value: 'Символ',
    Major.WHITE_SPACE.value: 'Пробел'
}


class Sub(Enum):
    PERIOD = '句点'
    COMMA = '読点'
    SENTENCE_ENDING = '終助詞'
    NUMERAL = '数詞'
    PROPER_NOUN = '固有名詞'
    GENERAL = '一般'
    DEPENDAND = '非自立可能'
    AUXILARY_STEM = '助動詞語幹'
    NOMINALIZER = '準体助詞'
    BINDING_PARTICLE = '係助詞'
    CONJUNCTIVE_PARTICLE = '接続助詞'
    CASE_PARTICLE = '格助詞'
    ADVERBIAL_PARTICLE = '副助詞'
    NOMINAL = '名詞的'
    COMMON_NOUN = '普通名詞'
    ADJECTIVAL_I = '形容詞的'
    ADJECTIVAL_NA = '形状詞的'
    TARI = 'タリ'
    OPENING_BRACKET = '括弧開'
    CLOSING_BRACKET = '括弧閉'
    VERBAL = '動詞的'
    NONE = '*'


SUB_EN = {
    Sub.SENTENCE_ENDING.value: 'Sentence-ending',
    Sub.PERIOD.value: 'Period',
    Sub.COMMA.value: 'Comma',
    Sub.NUMERAL.value: 'Numeral',
    Sub.GENERAL.value: 'General (default subtype)',
    Sub.PROPER_NOUN.value: '固有名詞',
    Sub.DEPENDAND.value: 'Dependant',
    Sub.NOMINALIZER.value: 'Nominalizing particle',
    Sub.BINDING_PARTICLE.value: 'Binding / Topic particle',
    Sub.CONJUNCTIVE_PARTICLE.value: 'Conjunctive particle',
    Sub.AUXILARY_STEM.value: 'Auxiliary stem',
    Sub.CASE_PARTICLE.value: 'Case particle',
    Sub.NOMINAL.value: 'Nominal',
    Sub.ADVERBIAL_PARTICLE.value: 'Adverbial particle',
    Sub.COMMON_NOUN.value: 'General noun',
    Sub.ADJECTIVAL_I.value: 'Adjectival-I',
    Sub.ADJECTIVAL_NA.value: 'Adjectival-Na',
    Sub.TARI.value: 'Tari',
    Sub.OPENING_BRACKET.value: 'Opening bracket',
    Sub.CLOSING_BRACKET.value: 'Closing bracket',
    Sub.VERBAL.value: 'Verbal',
    Sub.NONE.value: ''
}


class Sub2(Enum):
    PLACE = '地名'
    PERSON_NAME = '人名'
    COUNTER_CAPABLE = '助数詞可能'
    ADVERB_CAPABLE = '副詞可能'
    SURU_VERB_CAPABLE = 'サ変可能'
    NA_ADJECTIVE_CAPABLE = '形状詞可能'
    SURU_NA_CAPABLE = 'サ変形状詞可能'
    COUNTER = '助数詞'
    GENERAL = '一般'
    NONE = '*'


SUB2_EN = {
    Sub2.PLACE.value: 'Place name',
    Sub2.PERSON_NAME.value: 'Person name',
    Sub2.COUNTER_CAPABLE.value: 'Counter capable',
    Sub2.ADVERB_CAPABLE.value: 'Adverb capable',
    Sub2.SURU_VERB_CAPABLE.value: 'Suru-verb capable',
    Sub2.NA_ADJECTIVE_CAPABLE.value: 'Na-adjective capable',
    Sub2.SURU_NA_CAPABLE.value: 'Suru-verb & Na-adjective capable',
    Sub2.COUNTER.value: 'Counter',
    Sub2.GENERAL.value: 'General',
    Sub2.NONE.value: ''
}


class Sub3(Enum):
    COUNTRY = '国'
    FIRST_NAME = '名'
    LAST_NAME = '姓'
    GENERAL = '一般'
    NONE = '*'


SUB3_EN = {
    Sub3.COUNTRY.value: 'Country',
    Sub3.FIRST_NAME.value: 'First name',
    Sub3.LAST_NAME.value: 'Last name',
    Sub3.GENERAL.value: 'General',
    Sub3.NONE.value: ''
}


class ConjugationType(Enum):
    CLASSICAL_SHIKU = '文語形容詞-シク'
    CLASSICAL_RASHI = '文語助動詞-ラシ'

    AUXILIARY_NAI = '助動詞-ナイ'
    AUXILIARY_NU = '助動詞-ヌ'
    AUXILIARY_DA = '助動詞-ダ'
    AUXILIARY_RASHII = '助動詞-ラシイ'
    AUXILIARY_TA = '助動詞-タ'
    AUXILIARY_RERU = '助動詞-レル'
    AUXILIARY_TAI = '助動詞-タイ'
    AUXILIARY_DESU = '助動詞-デス'

    GODAN_SA = '五段-サ行'
    GODAN_BA = '五段-バ行'
    GODAN_KA = '五段-カ行'
    GODAN_WA = '五段-ワア行'
    GODAN_NA = '五段-ナ行'
    GODAN_TA = '五段-タ行'
    GODAN_RA = '五段-ラ行'
    GODAN_MA = '五段-マ行'

    LOWER_ICHIDAN_RA = '下一段-ラ行'
    LOWER_ICHIDAN_DA = '下一段-ダ行'
    LOWER_ICHIDAN_KA = '下一段-カ行'
    LOWER_ICHIDAN_A = '下一段-ア行'
    LOWER_ICHIDAN_NA = '下一段-ナ行'
    LOWER_ICHIDAN_GA = '下一段-ガ行'
    LOWER_ICHIDAN_SA = '下一段-サ行'
    LOWER_ICHIDAN_TA = '下一段-タ行'
    LOWER_ICHIDAN_BA = '下一段-バ行'
    LOWER_ICHIDAN_MA = '下一段-マ行'

    UPPER_ICHIDAN_RA = '上一段-ラ行'
    UPPER_ICHIDAN_GA = '上一段-ガ行'
    UPPER_ICHIDAN_A = '上一段-ア行'
    UPPER_ICHIDAN_MA = '上一段-マ行'
    UPPER_ICHIDAN_ZA = '上一段-ザ行'
    UPPER_ICHIDAN_KA = '上一段-カ行'
    UPPER_ICHIDAN_TA = '上一段-タ行'

    SA_IRREGULAR = 'サ行変格'
    KA_IRREGULAR = 'カ行変格'

    I_ADJECTIVE = '形容詞'

    NONE = '*'


CONJ_TYPE_EN = {
    ConjugationType.CLASSICAL_SHIKU.value: 'Classical Shiku-adjective',
    ConjugationType.CLASSICAL_RASHI.value: 'Classical Rashi',

    ConjugationType.AUXILIARY_NAI.value: 'Auxiliary Nai',
    ConjugationType.AUXILIARY_NU.value: 'Auxiliary Nu',
    ConjugationType.AUXILIARY_DA.value: 'Auxiliary Da',
    ConjugationType.AUXILIARY_RASHII.value: 'Auxiliary Rashii',
    ConjugationType.AUXILIARY_TA.value: 'Auxiliary Ta',
    ConjugationType.AUXILIARY_RERU.value: 'Auxiliary Reru',
    ConjugationType.AUXILIARY_TAI.value: 'Auxiliary Tai',
    ConjugationType.AUXILIARY_DESU.value: 'Auxiliary Desu',

    ConjugationType.GODAN_SA.value: 'Godan-SA',
    ConjugationType.GODAN_BA.value: 'Godan-BA',
    ConjugationType.GODAN_KA.value: 'Godan-KA',
    ConjugationType.GODAN_WA.value: 'Godan-WA',
    ConjugationType.GODAN_NA.value: 'Godan-NA',
    ConjugationType.GODAN_TA.value: 'Godan-TA',
    ConjugationType.GODAN_RA.value: 'Godan-RA',
    ConjugationType.GODAN_MA.value: 'Godan-MA',

    ConjugationType.LOWER_ICHIDAN_RA.value: 'Lower Ichidan-RA',
    ConjugationType.LOWER_ICHIDAN_DA.value: 'Lower Ichidan-DA',
    ConjugationType.LOWER_ICHIDAN_KA.value: 'Lower Ichidan-KA',
    ConjugationType.LOWER_ICHIDAN_A.value:  'Lower Ichidan-A',
    ConjugationType.LOWER_ICHIDAN_NA.value: 'Lower Ichidan-NA',
    ConjugationType.LOWER_ICHIDAN_GA.value: 'Lower Ichidan-GA',
    ConjugationType.LOWER_ICHIDAN_SA.value: 'Lower Ichidan-SA',
    ConjugationType.LOWER_ICHIDAN_TA.value: 'Lower Ichidan-TA',
    ConjugationType.LOWER_ICHIDAN_BA.value: 'Lower Ichidan-BA',
    ConjugationType.LOWER_ICHIDAN_MA.value: 'Lower Ichidan-MA',

    ConjugationType.UPPER_ICHIDAN_RA.value: 'Upper Ichidan-RA',
    ConjugationType.UPPER_ICHIDAN_GA.value: 'Upper Ichidan-GA',
    ConjugationType.UPPER_ICHIDAN_A.value:  'Upper Ichidan-A',
    ConjugationType.UPPER_ICHIDAN_MA.value: 'Upper Ichidan-MA',
    ConjugationType.UPPER_ICHIDAN_ZA.value: 'Upper Ichidan-ZA',
    ConjugationType.UPPER_ICHIDAN_KA.value: 'Upper Ichidan-KA',
    ConjugationType.UPPER_ICHIDAN_TA.value: 'Upper Ichidan-TA',

    ConjugationType.SA_IRREGULAR.value: 'SA-Irregular',
    ConjugationType.KA_IRREGULAR.value: 'KA-Irregular',

    ConjugationType.I_ADJECTIVE.value: 'I-Adjective',

    ConjugationType.NONE.value: ''
}


class ConjugationForm(Enum):
    STEM_SA = '語幹-サ'
    STEM_GENERAL = '語幹-一般'

    CONTINUATIVE_FORM = '連用形-一般'
    CONTINUATIVE_FORM_GEMIN = '連用形-促音便'
    CONTINUATIVE_FORM_NASAL = '連用形-撥音便'
    CONTINUATIVE_FORM_CONTR = '連用形-融合'
    CONTINUATIVE_FORM_I = '連用形-イ音便'
    CONTINUATIVE_FORM_NI = '連用形-ニ'

    CONDITIONAL_FORM_CONTR = '仮定形-融合'
    CONDITIONAL_FORM = '仮定形-一般'

    IRREALIS_FORM = '未然形-一般'
    IRREALIS_FORM_SA = '未然形-サ'

    TERMINAL_FORM = '終止形-一般'
    VOLITIONAL_FORM = '意志推量形'
    ATTRIBUTIVE_FORM = '連体形-一般'
    IMPERATIVE_FORM = '命令形'

    NONE = '*'


CONJ_FORM_EN = {
    ConjugationForm.STEM_SA.value: 'Stem (SA)',
    ConjugationForm.STEM_GENERAL.value: 'Stem',

    ConjugationForm.CONTINUATIVE_FORM.value: 'Continuative form (General)',
    ConjugationForm.CONTINUATIVE_FORM_GEMIN.value: 'Continuative form (Geminated)',
    ConjugationForm.CONTINUATIVE_FORM_NASAL.value: 'Continuative form (Nasal)',
    ConjugationForm.CONTINUATIVE_FORM_CONTR.value: 'Continuative form (Contracted)',
    ConjugationForm.CONTINUATIVE_FORM_I.value: 'Continuative form (I-sound change)',
    ConjugationForm.CONTINUATIVE_FORM_NI.value: 'Continuative form (Ni-ending)',

    ConjugationForm.CONDITIONAL_FORM.value: 'Conditional form',
    ConjugationForm.CONDITIONAL_FORM_CONTR.value: 'Conditional form (contracted)',

    ConjugationForm.IRREALIS_FORM.value: 'Irrealis form',
    ConjugationForm.IRREALIS_FORM_SA.value: 'Irrealis form (SA)',

    ConjugationForm.TERMINAL_FORM.value: 'Terminal form',
    ConjugationForm.VOLITIONAL_FORM.value: 'Volitional form',
    ConjugationForm.ATTRIBUTIVE_FORM.value: 'Attributive form',
    ConjugationForm.IMPERATIVE_FORM.value: 'Imperative form',

    ConjugationForm.NONE.value: ''
}


def translate_pos(token):
    pos = token.part_of_speech()

    major = pos[Pos.MAJOR.value]
    major_loc = MAJOR_EN.get(major)
    if major_loc is None:
        print(f'Unknown major POS: {major}')

    sub = pos[Pos.SUB.value]
    sub_loc = SUB_EN.get(sub)
    if sub_loc is None:
        print(f'Unknown sub POS: "{sub}"')

    sub2 = pos[Pos.SUB2.value]
    sub2_loc = SUB2_EN.get(sub2)
    if sub2_loc is None:
        print(f'Unknown sub2 POS: "{sub2}')

    sub3 = pos[Pos.SUB3.value]
    sub3_loc = SUB3_EN.get(sub3)
    if sub3_loc is None:
        print(f'Unknown sub3 POS: "{sub3}')

    conj_type = pos[Pos.CONJ_TYPE.value]
    conj_type_loc = CONJ_TYPE_EN.get(conj_type)
    if conj_type_loc is None:
        print(f'Unknown conj_type POS: "{conj_type}')

    conj_form = pos[Pos.CONJ_FORM.value]
    conj_form_loc = CONJ_FORM_EN.get(conj_form)
    if conj_form_loc is None:
        print(f'Unknown conj_form POS: "{conj_form}')

    return (
        major_loc,
        sub_loc,
        sub2_loc,
        sub3_loc,
        conj_type_loc,
        conj_form_loc,
    )
