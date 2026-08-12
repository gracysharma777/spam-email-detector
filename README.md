📧 Spam Email Detector

A beginner-friendly machine learning project that classifies messages as Spam or Not Spam using Python and Scikit-learn.

🎯 Project Overview

Spam messages are unwanted messages that may contain misleading offers, fake rewards, or suspicious links.

This project demonstrates how a machine learning model can learn patterns from example messages and use those patterns to classify new messages.

🧠 How It Works

The project follows these steps:

1. Collect sample email messages.
2. Label them as "spam" or "not spam".
3. Convert the text into numerical features using CountVectorizer.
4. Train a Multinomial Naive Bayes machine learning model.
5. Enter a new message.
6. The model predicts whether the message is spam or not spam.

Workflow

Email Message
      ↓
Text Vectorization
      ↓
Machine Learning Model
      ↓
Spam / Not Spam

🛠️ Technologies Used

- Python
- Scikit-learn
- Natural Language Processing (NLP)
- Multinomial Naive Bayes
- CountVectorizer
- Git & GitHub

📂 Project Structure

spam-email-detector/
│
├── spam_detector.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/gracysharma777/spam-email-detector.git

Move into the project directory:

cd spam-email-detector

Install the required library:

pip install -r requirements.txt

▶️ Run the Project

Run:

python spam_detector.py

Then enter an email message when prompted.

Type "exit" to stop the program.

💡 Example

Input

Congratulations! You won a free prize. Claim now!

Output

Prediction: spam

Another example:

Please send me the project report by evening.

The model should classify it as:

Prediction: not spam

🚀 Future Improvements

This project can be improved by:

- Using a larger real-world dataset.
- Adding train/test data splitting.
- Measuring accuracy, precision, recall, and F1-score.
- Trying different machine learning algorithms.
- Building a simple web interface.
- Improving text preprocessing.
- Deploying the model as a web application.

📚 What I Learned

Through this project, I learned the basics of:

- Python programming
- Text classification
- Natural Language Processing
- Machine learning model training
- Feature extraction
- Git and GitHub
- Project documentation

👩‍💻 Author

Gracy Sharma

Building, learning, and experimenting with Python and AI/ML.
