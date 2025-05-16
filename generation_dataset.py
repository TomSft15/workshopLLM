import json
import random

# Créer un dataset pour un assistant domestique intelligent
dataset = []

# 1. Contrôle des lumières
light_instructions = [
    {"instruction": "Allume la lumière du salon", "response": "J'ai allumé la lumière du salon."},
    {"instruction": "Éteins toutes les lumières de la maison", "response": "Toutes les lumières de la maison sont maintenant éteintes."},
    {"instruction": "Mets la lumière de la cuisine à 50%", "response": "La luminosité de la cuisine est réglée à 50%."},
    {"instruction": "Active le mode lecture dans la chambre", "response": "Mode lecture activé dans la chambre. La lumière est tamisée et plus chaude."},
    {"instruction": "Est-ce que la lumière du garage est allumée?", "response": "Selon les capteurs locaux, la lumière du garage est actuellement éteinte."}
]

# 2. Thermostat
thermostat_instructions = [
    {"instruction": "Règle le chauffage à 21 degrés", "response": "Le thermostat est maintenant réglé à 21 degrés Celsius."},
    {"instruction": "Quelle est la température actuelle dans la maison?", "response": "La température actuelle dans votre maison est de 19,5 degrés Celsius, selon les capteurs locaux."},
    {"instruction": "Active le mode économie d'énergie", "response": "Mode économie d'énergie activé. La température sera maintenue entre 17 et 19 degrés."},
    {"instruction": "Programme le chauffage pour qu'il s'allume à 6h du matin", "response": "J'ai programmé le chauffage pour qu'il démarre automatiquement à 6h00 du matin."},
    {"instruction": "Éteins la climatisation", "response": "La climatisation a été désactivée dans toute la maison."}
]

# 3. Sécurité
security_instructions = [
    {"instruction": "Verrouille toutes les portes", "response": "Toutes les portes de la maison sont maintenant verrouillées."},
    {"instruction": "Arme le système d'alarme en mode nuit", "response": "Système d'alarme activé en mode nuit. Les capteurs de mouvement intérieurs sont désactivés."},
    {"instruction": "Est-ce que la porte d'entrée est fermée?", "response": "Oui, selon les capteurs locaux, la porte d'entrée est bien fermée et verrouillée."},
    {"instruction": "Montre-moi les images de la caméra du jardin", "response": "Voici les images de la caméra du jardin sur l'écran connecté. Tout semble normal."},
    {"instruction": "Désactive l'alarme", "response": "Le système d'alarme a été désactivé. Vous pouvez entrer et sortir librement."}
]

# 4. Appareils électroménagers
appliance_instructions = [
    {"instruction": "Démarre le lave-vaisselle", "response": "Le lave-vaisselle a été mis en marche avec le programme standard."},
    {"instruction": "Préchauffe le four à 180 degrés", "response": "Le four préchauffe maintenant à 180 degrés Celsius."},
    {"instruction": "Est-ce que la machine à laver a terminé son cycle?", "response": "Oui, le cycle de lavage est terminé. Vous pouvez retirer votre linge."},
    {"instruction": "Programme la cafetière pour demain matin à 7h", "response": "La cafetière est programmée pour préparer du café demain à 7h00."},
    {"instruction": "Éteins tous les appareils de la cuisine", "response": "Tous les appareils de la cuisine sont maintenant éteints, sauf le réfrigérateur."}
]

# 5. Météo locale
weather_instructions = [
    {"instruction": "Quel temps fait-il aujourd'hui?", "response": "Selon les données de la station météo locale, il fait actuellement 22°C avec un ciel partiellement nuageux. L'humidité est de 45%."},
    {"instruction": "Est-ce qu'il va pleuvoir aujourd'hui?", "response": "D'après les données barométriques locales et les prévisions enregistrées ce matin, il y a 30% de chances de pluie dans l'après-midi."},
    {"instruction": "Quelle est la qualité de l'air à l'intérieur?", "response": "La qualité de l'air intérieur est bonne. Le taux de CO2 est de 650 ppm et l'humidité est à un niveau confortable de 40%."},
    {"instruction": "Quelle est la température extérieure?", "response": "La température extérieure est actuellement de 15°C selon le capteur installé sous l'auvent."},
    {"instruction": "Dois-je prendre un parapluie aujourd'hui?", "response": "Selon les données barométriques et les prévisions enregistrées, il serait prudent de prendre un parapluie, car il y a 60% de chances de pluie cet après-midi."}
]

# 6. Routines
routine_instructions = [
    {"instruction": "Active la routine du matin", "response": "Routine matinale activée : les volets du salon et de la cuisine s'ouvrent, la cafetière se met en marche, et la température est réglée à 21 degrés."},
    {"instruction": "Configure une nouvelle routine pour le soir", "response": "Pour configurer une nouvelle routine du soir, veuillez me dire quelles actions vous souhaitez inclure et à quelle heure elle doit s'activer."},
    {"instruction": "Désactive la routine du weekend", "response": "La routine du weekend a été désactivée. Elle ne se déclenchera pas automatiquement."},
    {"instruction": "Quelle routine est actuellement active?", "response": "Aucune routine n'est active en ce moment. La prochaine routine programmée est 'Soirée' à 19h00."},
    {"instruction": "Active le mode 'Je suis absent'", "response": "Mode 'absent' activé. Les lumières s'allumeront aléatoirement, le chauffage est réglé sur économie et le système de sécurité est armé."}
]

# 7. Cuisine et recettes
recipe_instructions = [
    {"instruction": "Suggère-moi une recette pour le dîner", "response": "Voici une suggestion basée sur les recettes enregistrées localement : Pâtes aux légumes de saison. Vous avez tous les ingrédients nécessaires d'après votre dernière liste."},
    {"instruction": "Comment faire une omelette?", "response": "Pour faire une omelette, battez 2-3 œufs, ajoutez sel et poivre. Faites chauffer un peu d'huile dans une poêle, versez les œufs et laissez cuire à feu moyen. Vous pouvez ajouter des garnitures de votre choix."},
    {"instruction": "Lance le minuteur pour 10 minutes", "response": "Minuteur réglé pour 10 minutes. Je vous préviendrai quand le temps sera écoulé."},
    {"instruction": "Combien de calories dans une pomme?", "response": "Selon la base de données nutritionnelles stockée localement, une pomme moyenne contient environ 95 calories."},
    {"instruction": "Ajoute du lait à ma liste de courses", "response": "J'ai ajouté le lait à votre liste de courses locale."}
]

# 8. Liste de courses
shopping_instructions = [
    {"instruction": "Ajoute du pain à ma liste de courses", "response": "J'ai ajouté 'pain' à votre liste de courses."},
    {"instruction": "Montre-moi ma liste de courses actuelle", "response": "Votre liste de courses actuelle contient : lait, œufs, pommes, céréales et maintenant pain."},
    {"instruction": "Supprime les œufs de ma liste de courses", "response": "J'ai supprimé 'œufs' de votre liste de courses."},
    {"instruction": "Vide ma liste de courses", "response": "Votre liste de courses a été vidée."},
    {"instruction": "Quel est le dernier élément ajouté à ma liste?", "response": "Le dernier élément ajouté à votre liste de courses est 'pain'."}
]

# Ajouter toutes les instructions au dataset
for category in [light_instructions, thermostat_instructions, security_instructions, 
                appliance_instructions, weather_instructions, routine_instructions, 
                recipe_instructions, shopping_instructions]:
    dataset.extend(category)

# Ajouter quelques instructions supplémentaires et variations
additional_instructions = []

# Variations pour les contrôles de lumière
light_locations = ["salon", "cuisine", "chambre principale", "salle de bain", "couloir", "bureau"]
light_actions = ["allume", "éteins", "baisse", "augmente", "mets en veilleuse"]

for action in light_actions:
    for location in light_locations:
        instruction = f"{action} la lumière de la {location}"
        response = f"J'ai {action[:-1]}é la lumière de la {location}."
        additional_instructions.append({"instruction": instruction, "response": response})

# Variations pour les questions de température
for room in ["salon", "cuisine", "chambre", "salle de bain"]:
    temp = random.randint(18, 24)
    additional_instructions.append({
        "instruction": f"Quelle est la température dans la {room}?",
        "response": f"La température dans la {room} est actuellement de {temp} degrés Celsius."
    })

# Sélectionnez un sous-ensemble aléatoire des variations pour éviter un dataset trop grand
random.shuffle(additional_instructions)
dataset.extend(additional_instructions[:25])

# Sauvegarder le dataset
with open('smart_home_assistant_dataset.json', 'w', encoding='utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"Dataset créé avec {len(dataset)} exemples.")