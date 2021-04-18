# XLSR
Cross-lingual sentence representations project on GitHub: [German-NLP-Group/xlsr](https://github.com/German-NLP-Group/xlsr)

We have created a new project with two gloals:
- provide clean code to train models for cross-Lingual sentence representations
- provide models that further increase the performance of [T-Systems-onsite/cross-en-de-roberta-sentence-transformer](https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer).

The model training consists of two parts steps:
1. automated hyperparameter oprimization with optuna and a 10-fold crossvalidation
2. training and saving the models with the found hyperparameterset

More details can be found on the [README.md](https://github.com/German-NLP-Group/xlsr/blob/main/README.md) page of the project.
