from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load model and tokenizer
model_path = r"C:\Users\saswith sahu\Desktop\Task-2\models\distilgpt2-recipe"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

@app.post("/get_recipe")
async def get_recipe(data: dict):
    ingredients = data.get("ingredients", "")
    prompt = f"Ingredients: {ingredients}\nRecipe:"

    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    
    # Generate recipe with controlled parameters
    output = model.generate(
        input_ids,
        max_new_tokens=100,
        do_sample=True,
        top_k=50,
        top_p=0.9,
        temperature=0.8,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        repetition_penalty=1.2,  # prevent repetition
        num_return_sequences=1
    )

    recipe = tokenizer.decode(output[0], skip_special_tokens=True)
    # Remove the prompt from the generated text
    recipe = recipe.replace(prompt, "").strip()
    return {"recipe": recipe}
