# Spam Email Detector
# A beginner-friendly machine learning project using Python

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
emails = [
    "Congratulations! You won a free prize. Claim now!",
    "You have won a lottery. Click here to receive your money.",
    "URGENT! You have been selected for a cash reward.",
    "Free gift waiting for you. Claim your prize today.",
    "Meeting is scheduled for tomorrow at 10 AM.",
    "Please send me the project report by evening.",
    "Can we meet for lunch today?",
    "Your assignment submission deadline is tomorrow.",
]

labels = [
    "spam",
    "spam",
    "spam",
    "spam",
    "not spam",
    "not spam",
    "not spam",
    "not spam",
]

# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# Train the machine learning model
model = MultinomialNB()
model.fit(X, labels)

print("=== Spam Email Detector ===")
print("Type an email to classify it.")
print("Type 'exit' to stop.")

while True:
    message = input("\nEnter email: ")

    if message.lower() == "exit":
        print("Goodbye!")
        break

    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)[0]

    print(f"Prediction: {prediction}")
