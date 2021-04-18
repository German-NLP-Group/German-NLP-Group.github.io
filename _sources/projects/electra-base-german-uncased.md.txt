# German Electra Model
The German Electra model: [german-nlp-group/electra-base-german-uncased](https://huggingface.co/german-nlp-group/electra-base-german-uncased)

We released an improved German Electra model. It was trained on a total of 1,500,000 steps.

# Uncase and Umlauts ('Ö', 'Ä', 'Ü')
This model is uncased. This helps especially for domains where colloquial terms with uncorrect capitalization is often used.

The special characters 'ö', 'ü', 'ä' are included through the `strip_accent=False` option, as this leads to an improved precision.

# Creators
This model was trained and open sourced in conjunction with the [**German NLP Group**](https://german-nlp-group.github.io/) in equal parts by:
- [**Philip May**](https://May.la) - [T-Systems on site services GmbH](https://www.t-systems-onsite.de/)
- [**Philipp Reißel**](https://www.reissel.eu) - [ambeRoad](https://amberoad.de/)
