from sentence_transformers import SentenceTransformer, util
"""
This module provides functionality to detect threat-related content in text using sentence embeddings.
Functions:
    is_threat(text: str, threshold: float = 0.6) -> bool:
        Determines if the input text is similar to any predefined threat-related phrases
        using cosine similarity of sentence embeddings. Returns True if a threat is detected,
        otherwise returns False.
Usage:
    - Loads a pre-trained SentenceTransformer model ('all-MiniLM-L6-v2').
    - Encodes a list of threat-related phrases.
    - For a given input text, computes its embedding and compares it to the threat phrase embeddings.
    - If the similarity with any threat phrase exceeds the specified threshold, the text is flagged as a threat.
Example:
    result = is_threat("I will attack you tonight")
    print(result)  # Output: True or False depending on similarity
"""



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

