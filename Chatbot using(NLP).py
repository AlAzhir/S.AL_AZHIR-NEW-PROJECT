import nltk
import random
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np  # Add this import for NumPy

# Download the NLTK data (if not already downloaded)
nltk.download('punkt')

# Define the training data - you can extend this list
training_data = [
    ("Hello!", "hello"),
    ("Hi there!", "hello"),
    ("How are you?", "how_are_you"),
    # Add more training examples here
]

# Create a dictionary of intents
intents = {
    "hello": ["Hello!", "Hi there!"],
    "how_are_you": ["I am doing fine, and you?"],
    # Add more intents and responses here
}

# Tokenize and preprocess the training data using NLTK
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text for text, _ in training_data])
X = tokenizer.texts_to_sequences([text for text, _ in training_data])
X = pad_sequences(X)  # Pad sequences

# Convert y to numerical labels
y = [intent for _, intent in training_data]  # Simplified y
y_numeric = [list(intents.keys()).index(intent) for intent in y]

# Convert X and y_numeric to NumPy arrays
X = np.array(X)
y_numeric = np.array(y_numeric)

# Define the model using TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=16),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(len(intents), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y_numeric, epochs=100, verbose=0)

# Chatbot function
def chatbot_response(user_message):
    user_message_sequence = tokenizer.texts_to_sequences([user_message])
    user_message_sequence = pad_sequences(user_message_sequence)
    predicted_intent = model.predict(user_message_sequence)
    predicted_intent = list(intents.keys())[predicted_intent.argmax()]

    if predicted_intent in intents:
        return random.choice(intents[predicted_intent])
    else:
        return "I'm not sure how to respond to that."

# Main chat loop
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break

    bot_response = chatbot_response(user_input)
    print('Bot:', bot_response)
