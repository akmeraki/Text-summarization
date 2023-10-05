# Text-summarization

Text summarization is the process of shortening a set of data computationally, to create a subset that represents the most important or relevant information within the original content.

<p align="center">
<img src="https://github.com/akmeraki/Text-summarization/blob/main/images/b9bf06f6.png">
</p>

### Dependencies 

This project requires **Python 3.8** and the following Python libraries installed: Please utilize the environment file to install related packages.

- [HuggingFace](https://huggingface.co/)
- [Transformers](https://huggingface.co/docs/transformers/installation)
- [Transformers][sentencepiece](https://github.com/google/sentencepiece)
- [sacrebleu](https://github.com/mjpost/sacrebleu)
- [datasets](https://huggingface.co/docs/datasets/v1.15.1/tutorial.html)
- [rouge_score](https://pypi.org/project/rouge-score/)

### Table of Contents 


### Folder Structure 
```
├──  artifacts    - folder where data artifacts are stored 
│    └── data_ingestion - contains the downloaded data files.   
|    └── data_validation - contains the validation status file.
|    └── data_transformation - contains the dataset after transformation.
│    └── model_training - contains the trained model and tokenizer.
|    └── model_evaluation - contains results of model evaluation as a CSV file.    
├── config    - contains config YAML file which specifies Paths of required artifacts
├── images    - contains images used in this repository.
│                 
├── research
│    └── Text_Summarizer_Pegasus.ipynb - research notebooks to Train, evaluate and test Text Summarizer Pegasus model. 
|    └── 01_data_ingestion.ipynb - pre-pipeline implementation notebook for data ingestion 
|    └── 02_data_validation.ipynb - pre-pipeline implementation notebook for data validation 
|    └── 03_data_transformation.ipynb - pre-pipeline implementation notebook for data transformation 
|    └── 04_model_trainer.ipynb - pre-pipeline implementation notebook for model training 
|    └── 05_model_trainer.ipynb - pre-pipeline implementation notebook for model evaluation
|
├── src/textSummarizer
|          └── 
|
| 