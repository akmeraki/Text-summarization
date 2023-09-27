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
│  
├── images      - contains images used in this repository.
│                 
├── research
│    └── Text_Summarizer_Pegasus.ipynb - research notebooks to Train,evaluate and test Text Summarizer Pegasus model. 
|     └── data_ingestion.ipynb - research notebook for data ingestion 
|     └── data_validation.ipynb - reserach notebook for data validation 
|── 
|
|