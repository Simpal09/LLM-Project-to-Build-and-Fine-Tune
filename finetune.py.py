# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-_7lE0uj_6NxWzWoISwJ5d8B8SMPkrwe
"""

pip install rouge-score

import os
import torch
from transformers import (AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer,
                          DataCollatorForLanguageModeling)
from datasets import Dataset
from rouge_score import rouge_scorer
from peft import get_peft_model, PromptTuningConfig
import pandas as pd

# Step 1: Load Pre-trained Large Language Model and Tokenizer
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set padding token if not already present
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Step 2: Load and Preprocess Dataset
data = {
    "text": [
        "E-commerce platforms offer a wide range of products.",
        "Return policies vary by category and seller.",
        "Free shipping is available for orders above a certain amount.",
        "Discounts are offered during festive seasons.",
        "Customer reviews help in making purchase decisions."
    ]
}

df = pd.DataFrame(data)
dataset = Dataset.from_pandas(df)

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Step 3: Fine-Tuning the Model
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="steps",
    eval_steps=500,
    save_steps=500,
    learning_rate=5e-5,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    load_best_model_at_end=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
    eval_dataset=tokenized_datasets,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()

# Step 4: Evaluate the Fine-Tuned Model with ROUGE Metric
scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
def compute_metrics(eval_preds):
    predictions, labels = eval_preds
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    scores = {
        metric: scorer.score(decoded_preds[i], decoded_labels[i])
        for i, metric in enumerate(["rouge1", "rouge2", "rougeL"])
    }
    return {"rouge": scores}

# Step 5: Implement Prompt Engineering and PEFT (Parameter-Efficient Fine-Tuning)
peft_config = PromptTuningConfig(task_type="CAUSAL_LM", num_virtual_tokens=20)
peft_model = get_peft_model(model, peft_config)

# Step 6: Implement RLHF (Reinforcement Learning with Human Feedback) placeholder
# Requires human-labeled data and policy optimization techniques (not fully implemented here)

# Step 7: Knowledge Grounding with Retrieval Augmented Generation (RAG)
def retrieve_documents(query):
    # Placeholder for document retrieval mechanism
    return "Relevant documents for query: " + query

def augment_input_with_knowledge(input_text):
    knowledge = retrieve_documents(input_text)
    return f"{knowledge}\n{input_text}"

# Step 8: Build Chatbot Application for E-commerce Use Case
def chatbot_response(user_query):
    augmented_query = augment_input_with_knowledge(user_query)
    inputs = tokenizer(augmented_query, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example Usage
if __name__ == "__main__":
    print("Fine-tuned LLM Example")
    user_input = "What are the return policies for electronics?"
    response = chatbot_response(user_input)
    print("Chatbot Response:", response)

eff49119dbc9bbd7cad7016ee86b4410c9a5a030

import os
import torch
from transformers import (AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer,
                          DataCollatorForLanguageModeling)
from datasets import Dataset
from rouge_score import rouge_scorer
from peft import get_peft_model, PromptTuningConfig
import pandas as pd

# Step 1: Load Pre-trained Large Language Model and Tokenizer
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set padding token if not already present
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Step 2: Load and Preprocess Dataset
data = {
    "text": [
        "E-commerce platforms offer a wide range of products.",
        "Return policies vary by category and seller.",
        "Free shipping is available for orders above a certain amount.",
        "Discounts are offered during festive seasons.",
        "Customer reviews help in making purchase decisions."
    ]
}

df = pd.DataFrame(data)
dataset = Dataset.from_pandas(df)

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Step 3: Fine-Tuning the Model
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="steps",
    eval_steps=500,
    save_steps=500,
    learning_rate=5e-5,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    load_best_model_at_end=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
    eval_dataset=tokenized_datasets,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()

# Step 4: Evaluate the Fine-Tuned Model with ROUGE Metric
scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
def compute_metrics(eval_preds):
    predictions, labels = eval_preds
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    scores = {
        metric: scorer.score(decoded_preds[i], decoded_labels[i])
        for i, metric in enumerate(["rouge1", "rouge2", "rougeL"])
    }
    return {"rouge": scores}

# Step 5: Implement Prompt Engineering and PEFT (Parameter-Efficient Fine-Tuning)
peft_config = PromptTuningConfig(task_type="CAUSAL_LM", num_virtual_tokens=20)
peft_model = get_peft_model(model, peft_config)

# Step 6: Implement RLHF (Reinforcement Learning with Human Feedback) placeholder
# Requires human-labeled data and policy optimization techniques (not fully implemented here)

# Step 7: Knowledge Grounding with Retrieval Augmented Generation (RAG)
def retrieve_documents(query):
    # Placeholder for document retrieval mechanism
    return "Relevant documents for query: " + query

def augment_input_with_knowledge(input_text):
    knowledge = retrieve_documents(input_text)
    return f"{knowledge}\n{input_text}"

# Step 8: Build Chatbot Application for E-commerce Use Case
def chatbot_response(user_query):
    augmented_query = augment_input_with_knowledge(user_query)
    inputs = tokenizer(augmented_query, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)



