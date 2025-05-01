from sentence_transformers import SentenceTransformer, util

# Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# List of threat-related phrases/keywords
threat_phrases = [
    "I will kill you",
    "I have a bomb",
    "I will attack",
    "I will shoot",
    "I will stab you",
    "I will hurt you",
    "I will harm people",
    "I will explode a bomb",
    "taking hostages",
    "committing violence",
    "terror attack"
]

# Encode the threat phrases
threat_embeddings = model.encode(threat_phrases)

def is_threat(text, threshold=0.6):
    # Encode the input text
    text_embedding = model.encode(text)

    # Compute cosine similarity with each threat phrase
    similarities = util.cos_sim(text_embedding, threat_embeddings)

    # Check if any similarity score is above the threshold
    for score in similarities[0]:
        if score >= threshold:
            return True
    return False

# Test sentences
test_sentences = [
    "I will attack you tonight",
    "Let's go watch a movie",
    "There's a bomb in the building",
    "She is just reading a book",
    "I’m going to blow everything up",
    "Time to take hostages and make demands"
]

for sentence in test_sentences:
    result = is_threat(sentence)
    print(f"'{sentence}' => Threat Detected: {result}")

