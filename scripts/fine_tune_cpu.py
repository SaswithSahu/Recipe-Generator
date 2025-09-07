from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling
)

# Model & tokenizer
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Fix padding token
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Load dataset
dataset_path = r"C:\Users\saswith sahu\Desktop\Task-2\data\recipes.jsonl"
dataset = load_dataset("json", data_files=dataset_path)["train"]

# Tokenize dataset
def format_example(ex):
    text = f"Ingredients: {ex['ingredients']}\nRecipe: {ex['recipe']}"
    return tokenizer(text, truncation=True, max_length=128)

dataset = dataset.map(format_example, remove_columns=dataset.column_names)
dataset.set_format(type="torch", columns=["input_ids", "attention_mask"])

# Data collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Training arguments
training_args = TrainingArguments(
    output_dir=r"C:\Users\saswith sahu\Desktop\Task-2\models\distilgpt2-recipe",
    num_train_epochs=5,                     # Increase for better learning
    per_device_train_batch_size=2,          # CPU-friendly small batch
    gradient_accumulation_steps=4,          # Simulate larger batch
    save_steps=100,
    save_total_limit=2,                     # Keep only 2 checkpoints
    logging_steps=20,
    learning_rate=5e-5,
    weight_decay=0.01,
    fp16=False,                             # CPU training
    remove_unused_columns=False,
    logging_dir=r"C:\Users\saswith sahu\Desktop\Task-2\logs",
    report_to=None                          # Disable WandB/other logs if not used
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=data_collator
)

# Train and save
trainer.train()
trainer.save_model(r"C:\Users\saswith sahu\Desktop\Task-2\models\distilgpt2-recipe")
