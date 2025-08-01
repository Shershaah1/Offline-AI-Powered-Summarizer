from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Save model and tokenizer locally
tokenizer.save_pretrained("./model")
model.save_pretrained("./model")

print("✅ Model and tokenizer saved locally in ./model")
