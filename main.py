
import re
from typing import Dict
TEST_DATA = [
    ("I am very happy today", "joy"),
    ("I feel sad and lonely", "sadness"),
    ("I am really angry about this", "anger"),
    ("I feel very scared and anxious", "fear"),
    ("That is disgusting and horrible", "disgust"),
    ("I am excited for the future", "anticipation"),
    ("I trust you completely", "trust"),
    ("I am shocked and surprised", "surprise"),
]

LEXICON: Dict[str, str] = {
    # Joy
    "happy": "joy", "happiness": "joy", "joyful": "joy", "joy": "joy",
    "excited": "joy", "elated": "joy", "thrilled": "joy", "delighted": "joy",
    "ecstatic": "joy", "cheerful": "joy", "glad": "joy", "pleased": "joy",
    "wonderful": "joy", "fantastic": "joy", "great": "joy", "love": "joy",
    "blessed": "joy", "grateful": "joy", "thankful": "joy", "proud": "joy",
    "laugh": "joy", "smile": "joy", "fun": "joy", "enjoy": "joy",
    "celebrate": "joy", "celebration": "joy", "promotion": "joy",
    "winning": "joy", "victory": "joy", "content": "joy", "euphoric": "joy",
    "blissful": "joy", "amazing": "joy", "incredible": "joy",

    # Sadness
    "sad": "sadness", "sadness": "sadness", "unhappy": "sadness",
    "depressed": "sadness", "depression": "sadness", "miserable": "sadness",
    "grief": "sadness", "grieve": "sadness", "heartbroken": "sadness",
    "devastated": "sadness", "cry": "sadness", "tears": "sadness",
    "weep": "sadness", "miss": "sadness", "lonely": "sadness", "depressed":"sad",
    "hopeless": "sadness", "helpless": "sadness", "empty": "sadness",
    "pain": "sadness", "hurt": "sadness", "sorrow": "sadness",
    "regret": "sadness", "disappointed": "sadness", "gloomy": "sadness",
    "melancholy": "sadness", "broken": "sadness", "shattered": "sadness",
    "despair": "sadness", "mourning": "sadness", "forlorn": "sadness",

    # Anger
    "angry": "anger", "anger": "anger", "furious": "anger", "rage": "anger",
    "enraged": "anger", "mad": "anger", "livid": "anger", "outraged": "anger",
    "frustrated": "anger", "frustration": "anger", "annoyed": "anger",
    "irritated": "anger", "hate": "anger", "hatred": "anger",
    "despise": "anger", "loathe": "anger", "unfair": "anger",
    "injustice": "anger", "betrayed": "anger", "betrayal": "anger",
    "scream": "anger", "yell": "anger", "infuriated": "anger",
    "hostile": "anger", "bitter": "anger", "resentful": "anger",
    "resentment": "anger", "indignant": "anger", "wrath": "anger",
    "seething": "anger", "aggravated": "anger", "exasperated": "anger",

    # Fear
    "afraid": "fear", "fear": "fear", "scared": "fear", "frightened": "fear",
    "terrified": "fear", "terror": "fear", "panic": "fear", "anxious": "fear",
    "anxiety": "fear", "worried": "fear", "worry": "fear", "nervous": "fear",
    "dread": "fear", "dreading": "fear", "phobia": "fear", "nightmare": "fear",
    "horror": "fear", "uneasy": "fear", "insecure": "fear", "paranoid": "fear",
    "stressed": "fear", "stress": "fear", "shaking": "fear",
    "overwhelmed": "fear", "intimidated": "fear", "petrified": "fear",
    "alarmed": "fear", "apprehensive": "fear", "threatened": "fear",

    # Surprise
    "surprised": "surprise", "surprise": "surprise", "shocked": "surprise",
    "shock": "surprise", "astonished": "surprise", "amazed": "surprise",
    "stunned": "surprise", "unexpected": "surprise", "suddenly": "surprise",
    "unbelievable": "surprise", "wow": "surprise", "whoa": "surprise",
    "speechless": "surprise", "flabbergasted": "surprise",
    "dumbfounded": "surprise", "bewildered": "surprise",
    "startled": "surprise", "astounded": "surprise", "aghast": "surprise",

    # Disgust
    "disgusted": "disgust", "disgust": "disgust", "revolted": "disgust",
    "repulsed": "disgust", "gross": "disgust", "nasty": "disgust",
    "nauseated": "disgust", "vile": "disgust", "filthy": "disgust",
    "awful": "disgust", "horrible": "disgust", "appalled": "disgust",
    "disgusting": "disgust", "abhorrent": "disgust", "loathsome": "disgust",
    "repellent": "disgust", "offensive": "disgust", "foul": "disgust",
    "putrid": "disgust", "rotten": "disgust", "detestable": "disgust",

    # Anticipation
    "anticipate": "anticipation", "anticipation": "anticipation",
    "eager": "anticipation", "eagerness": "anticipation",
    "hope": "anticipation", "hoping": "anticipation", "hopeful": "anticipation",
    "expect": "anticipation", "expecting": "anticipation",
    "planning": "anticipation", "upcoming": "anticipation",
    "future": "anticipation", "dream": "anticipation", "ready": "anticipation",
    "countdown": "anticipation", "yearning": "anticipation",
    "longing": "anticipation", "optimistic": "anticipation",
    "prepare": "anticipation", "craving": "anticipation",

    # Trust
    "trust": "trust", "trustworthy": "trust", "reliable": "trust",
    "dependable": "trust", "faith": "trust", "confident": "trust",
    "confidence": "trust", "safe": "trust", "secure": "trust",
    "honest": "trust", "honesty": "trust", "loyal": "trust", "loyalty": "trust",
    "committed": "trust", "dedicated": "trust", "support": "trust",
    "supported": "trust", "compassion": "trust", "respect": "trust",
    "admire": "trust", "integrity": "trust", "sincere": "trust",
    "genuine": "trust", "reassured": "trust",
}

def evaluate_accuracy():
    correct = 0
    total = len(TEST_DATA)

    for text, true_label in TEST_DATA:
        predicted = classify(text)

        if predicted == true_label:
            correct += 1

        print(f"Text: {text}")
        print(f"True: {true_label} | Predicted: {predicted}\n")

    accuracy = correct / total
    print(f"Accuracy: {accuracy * 100:.2f}%")
    
def classify(text: str) -> str:
    """Return the base emotion for the given text."""
    words = re.findall(r"[a-z']+", text.lower())
    counts: Dict[str, int] = {}
    for word in words:
        if word in LEXICON:
            emotion = LEXICON[word]
            counts[emotion] = counts.get(emotion, 0) + 1

    if not counts:
        # No known keywords — default to the closest guess by most frequent word tone
        return "anticipation"   # forward-looking default for ambiguous input

    return max(counts, key=counts.get)

def main():
    print("\nEmotion Classifier  |  Type 'quit' to exit\n")
    while True:
        try:
            text = input("You   > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        
        if not text:
            continue
        if text.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        emotion = classify(text)
        print(f"Emotion > {emotion.upper()}\n")
        print("Running accuracy test...\n")

        evaluate_accuracy()


if __name__ == "__main__":
    main()