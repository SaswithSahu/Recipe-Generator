```markdown
# 🍳 Recipe Generator with Fine-Tuned GPT-2

A simple **recipe generation app** powered by a fine-tuned version of **DistilGPT-2**.  
Users can enter ingredients in a chat-like interface, and the app will generate recipe suggestions.

---

## 📂 Project Structure

```

Task-2/
├── data/
│    └── recipes.jsonl        # Training dataset
├── models/
│    └── distilgpt2-recipe/   # Fine-tuned model (download separately)
├── scripts/
│    └── api\_cpu.py           # FastAPI backend
├── index.html                # Frontend chat UI
├── style.css                 # Frontend styles
├── script.js                 # Frontend logic
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies

````

---

## 🚀 Features
- Fine-tuned **DistilGPT-2** model for recipe generation.  
- **FastAPI backend** for serving the model.  
- **Classic chat UI** using HTML, CSS, and JavaScript.  
- Lightweight CPU-friendly deployment.

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/recipe-generator.git
cd Task-2
````

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Model Setup

The fine-tuned model is not stored in this repo (too large).
Download it from Google Drive:

👉 [Download distilgpt2-recipe.zip](https://drive.google.com/file/d/1TaWxtSCHPI17FX-4l-iTddlbnqOmwEwu/view?usp=sharing)

After downloading:

1. Unzip the file
2. Place the folder inside:

```
Task-2/models/distilgpt2-recipe/
```

Your folder should look like:

```
Task-2/
 ├── models/
 │    └── distilgpt2-recipe/
 │         ├── config.json
 │         ├── pytorch_model.bin
 │         ├── tokenizer.json
 │         └── ...
```

---

## ▶️ Running the Backend

Start the FastAPI server:

```bash
uvicorn scripts.api_cpu:app --reload --port 8000
```

* The backend will run on: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 💬 Running the Frontend

Simply open `index.html` in your browser.

* Enter ingredients in the chatbox.
* The model will generate a recipe response from the backend.

---

## 🛠 Tech Stack

* **Python** (FastAPI, Transformers, Datasets)
* **JavaScript, HTML, CSS** (frontend)
* **Hugging Face Transformers** (model fine-tuning)

---

## 📊 Dataset

The training dataset is located in:

```
data/recipes.jsonl
```

Each entry contains:

```json
{
  "ingredients": "Chicken, Spinach, Tomato Sauce",
  "recipe": "Bake chicken breasts with spinach and tomato sauce until cooked through."
}
```
