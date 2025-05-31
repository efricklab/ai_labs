from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment_vader(text):
    """
    Analyzes the sentiment of a given text using VADER.
    Returns a dictionary containing the polarity scores (pos, neg, neu, compound)
    and a simple sentiment label (Positive, Negative, Neutral).
    """
    analyzer = SentimentIntensityAnalyzer()
    # Get the polarity scores
    # vs is a dictionary: {'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.4215}
    vs = analyzer.polarity_scores(text)

    # Determine sentiment label based on compound score
    # These thresholds are common but can be adjusted:
    # Positive sentiment: compound score >= 0.05
    # Neutral sentiment: -0.05 < compound score < 0.05
    # Negative sentiment: compound score <= -0.05
    compound_score = vs['compound']
    if compound_score >= 0.05:
        sentiment_label = "Positive"
    elif compound_score <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return {
        "text": text,
        "scores": vs,
        "label": sentiment_label
    }

# --- Main part of the program ---
if __name__ == "__main__":
    print("Lab: Simple Sentiment Analysis with VADER")
    print("-----------------------------------------\n")

    # Example sentences to analyze
    sentences = [
        "VADER is smart, handsome, and funny.",
        "VADER is smart, handsome, and funny!",
        "VADER is very smart, handsome, and funny.",
        "VADER is not smart, handsome, nor funny.",
        "The movie was good.",
        "The movie was only so-so.",
        "This is a terrible product, I hate it.",
        "I am feeling okay today.",
        "The weather is just normal.",
        "I love Python programming :)",
        "This is ridiculously good!",
        "This is NOT good.",
        "The book was not bad at all.",
        "It's a bit disappointing, to be honest."
    ]

    print("--- Analyzing Predefined Sentences ---")
    for sentence in sentences:
        analysis_result = analyze_sentiment_vader(sentence)
        print(f"Text: \"{analysis_result['text']}\"")
        print(f"  Scores: {analysis_result['scores']}")
        print(f"  Overall Sentiment: {analysis_result['label']}")
        print("-" * 20)

    print("\n--- Try Your Own Sentence ---")
    while True:
        user_input = input("Enter a sentence (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        if user_input.strip(): # Check if input is not just whitespace
            analysis_result = analyze_sentiment_vader(user_input)
            print(f"  Scores: {analysis_result['scores']}")
            print(f"  Overall Sentiment: {analysis_result['label']}")
            print("-" * 20)
        elif user_input: # If it's empty but not whitespace (e.g., just pressed Enter)
            print("Please enter some text.")
    
