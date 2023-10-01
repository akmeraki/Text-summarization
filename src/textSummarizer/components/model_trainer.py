import torch
import os
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from textSummarizer.logging import logger
from textSummarizer.entity import ModelTrainerConfig
from datasets import load_dataset, load_from_disk


class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):

        self.config = config

    def train(self):

        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        print(self.config)

        trainer_args = TrainingArguments(
            output_dir = self.config.root_dir,
            num_train_epochs =  int(self.config.num_train_epochs),
            warmup_steps= int(self.config.num_train_epochs),
            per_device_train_batch_size = int(self.config.per_device_train_batch_size), 
            weight_decay = float(self.config.weight_decay),
            logging_steps = int(self.config.logging_steps),
            evaluation_strategy = self.config.evaluation_strategy,
            eval_steps = int(self.config.eval_steps),
            save_steps =  float(self.config.save_steps),
            gradient_accumulation_steps  = int(self.config.gradient_accumulation_steps)
        )

        trainer = Trainer(model=model_pegasus, args=trainer_args,
                          tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                          train_dataset = dataset_samsum_pt["test"],
                          eval_dataset = dataset_samsum_pt["validation"])
        
        trainer.train()

        # save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))

        # Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
