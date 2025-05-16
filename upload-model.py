from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login, HfApi
import torch
from peft import LoraConfig, get_peft_model

# Se connecter à Hugging Face avec votre token
print("Connexion à Hugging Face...")
login()  # Entrez votre token quand demandé

# Définir le nom du repo dans l'organisation Epitech
repo_id = "Epitech/smart-home-assistant-model"

# Créer un modèle de base avec LoRA
print("Création d'un modèle optimisé pour Raspberry Pi 4GB...")

# Utiliser un modèle très léger
base_model_id = "microsoft/phi-1_5"  # Modèle très léger (1.3B)
print(f"Chargement du modèle de base {base_model_id}...")

# Configuration sans bitsandbytes et sans CUDA
tokenizer = AutoTokenizer.from_pretrained(base_model_id)
model = AutoModelForCausalLM.from_pretrained(
    base_model_id,
    torch_dtype=torch.float16,  # Utiliser float16 pour économiser de la mémoire
    device_map="cpu",  # Forcer l'utilisation du CPU
)

# Ajouter les adaptateurs LoRA
print("Ajout des adaptateurs LoRA...")
lora_config = LoraConfig(
    r=4,  # Rang réduit pour économiser la mémoire
    lora_alpha=4,
    # Pour Phi-1.5, les modules cibles sont différents
    target_modules=["Wqkv", "fc1", "fc2"],
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, lora_config)
print("Modèle avec LoRA créé avec succès.")

# Sauvegarder le modèle localement
print("Sauvegarde du modèle localement...")
model.save_pretrained("./smart-home-assistant-model")
tokenizer.save_pretrained("./smart-home-assistant-model") 
print("Modèle sauvegardé localement.")

# Créer le repo et uploader le modèle
print(f"Upload du modèle vers {repo_id}...")
api = HfApi()
api.create_repo(repo_id=repo_id, exist_ok=True)
api.upload_folder(
    folder_path="./smart-home-assistant-model",
    repo_id=repo_id,
    repo_type="model"
)
print(f"Modèle uploadé avec succès sur Hugging Face à: https://huggingface.co/{repo_id}")

# # Ajouter des métadonnées pour le README
# model_card = f"""---
# language: fr
# license: apache-2.0
# tags:
# - gemma
# - gemma-3-1b
# - smart-home
# - assistant
# - privacy
# - raspberry-pi
# datasets:
# - Epitech/smart-home-assistant-dataset
# ---

# # Smart Home Assistant - Gemma-3 1B

# Ce modèle est un assistant domestique intelligent qui préserve la vie privée en fonctionnant localement sur un Raspberry Pi.

# ## Description

# Ce modèle est une version optimisée de Gemma-3 1B, configurée pour:
# - Traiter les commandes vocales
# - Automatiser les appareils domestiques
# - Fournir des réponses contextuelles
# - Fonctionner hors ligne, sans envoyer de données au cloud

# ## Spécifications techniques

# - **Modèle de base**: Gemma-3 1B Instruct
# - **Méthode d'optimisation**: Adaptateurs LoRA (r=4)
# - **Quantification**: 4-bit pour réduire l'empreinte mémoire
# - **Taille finale**: Compatible avec un Raspberry Pi 4GB
# - **Dataset utilisé**: [Epitech/smart-home-assistant-dataset](https://huggingface.co/datasets/Epitech/smart-home-assistant-dataset)

# ## Utilisation sur Raspberry Pi

# ```python
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# # Charger le modèle
# model_id = "Epitech/smart-home-assistant-gemma-1b"
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(
#     model_id,
#     device_map="auto",
#     load_in_4bit=True,  # Important pour Raspberry Pi
# )

# # Fonction pour générer une réponse
# def get_response(user_input):
#     messages = [{"role": "user", "content": user_input}]
#     prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
#     inputs = tokenizer(prompt, return_tensors="pt")
    
#     outputs = model.generate(
#         input_ids=inputs["input_ids"],
#         max_new_tokens=64,
#         temperature=0.7,
#         top_p=0.95,
#     )
    
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     response = response.split("<start_of_turn>model\\n")[-1].split("<end_of_turn>")[0].strip()
#     return response

# # Exemple
# print(get_response("Allume la lumière du salon"))