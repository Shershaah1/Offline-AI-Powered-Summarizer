from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "sshleifer/distilbart-cnn-12-6"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Save offline
tokenizer.save_pretrained("./model")
model.save_pretrained("./model")

print("✅ DistilBART model downloaded and saved offline to ./model folder.")
