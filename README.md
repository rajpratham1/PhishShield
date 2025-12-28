# PhishShield: AI-Powered Phishing URL Detector

PhishShield is a web application designed to protect users from phishing attacks by analyzing URLs and predicting whether they lead to malicious websites. It leverages a machine learning model to provide real-time classification of URLs, offering a simple and effective first line of of defense against online fraud.

The application provides a clean user interface where a user can enter a URL. The backend then extracts key features from the URL and uses a pre-trained `RandomForestClassifier` to determine if the site is likely safe or a phishing attempt.

## How It Works

The detection process follows two main steps:

1.  **Feature Extraction**: When a user submits a URL, the backend processes it to extract a set of numerical features that the machine learning model can understand. The current features include:
    *   **URL Length**: Malicious URLs are often unusually long.
    *   **Presence of '@' Symbol**: Legitimate URLs rarely contain this symbol in the domain name.
    *   **Presence of '-' Symbol**: Often used to make phishing domains look legitimate (e.g., `your-bank-login.com`).
    *   **Presence of '//' Redirect**: Multiple slashes can indicate a redirect to a different, potentially malicious, site.
    *   **HTTPS Protocol**: Checks if the URL uses a secure `https` connection. While many phishing sites now use HTTPS, its absence is a red flag.

2.  **Prediction**: The extracted features are then passed to a pre-trained `RandomForestClassifier`. This model has been trained on a labeled dataset of thousands of safe and phishing URLs and has learned to recognize the patterns that distinguish them. The model outputs a prediction ("Safe" or "Phishing") along with a confidence score.

## Features

*   **Real-time URL Analysis**: Instantly check if a URL is suspicious.
*   **ML-Powered Detection**: Utilizes a `RandomForestClassifier` model trained on URL features to detect phishing patterns.
*   **Confidence Score**: Provides a confidence score for each prediction, indicating the model's certainty.
*   **Simple Web Interface**: Easy-to-use interface for submitting URLs for analysis.
*   **Extensible Feature Set**: The feature extraction logic is designed to be easily extendable.

## Technology Stack

*   **Backend**: Python, Flask
*   **Machine Learning**: Scikit-learn, Pandas, Joblib
*   **Frontend**: HTML, Bootstrap 5

## Project Structure

```
PhishShield/
├── app.py                  # Main Flask application
├── train_model.py          # Script to train the ML model
├── process_dataset.py      # Script to process the raw dataset
├── phishing_features.py    # Feature extraction logic
├── model.pkl               # Trained machine learning model
├── requirements.txt        # Python dependencies
├── phishing_urls.csv       # Processed dataset of URLs and labels
├── templates/
│   ├── index.html          # Home page for URL submission
│   └── result.html         # Page to display analysis results
└── static/
    ├── style.css           # Custom styles
    └── logo.jpg            # Project logo
```

## Setup and Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/PhishShield.git
    cd PhishShield
    ```

2.  **Create and activate a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Run the application**:
    ```bash
    python app.py
    ```

2.  **Open your web browser** and go to `http://127.0.0.1:5000`.

3.  Enter a URL in the input field and click "Check Safety" to see the prediction.

## Improving The Model

The `RandomForestClassifier` provides a good baseline, but its predictive power can be enhanced:

*   **Experiment with Different Models**: Try more advanced ensemble models like **XGBoost** or **LightGBM**, or even a simple **Neural Network** built with TensorFlow/Keras.
*   **Expand the Feature Set**: The more information the model has, the better it can perform. Consider adding:
    *   **Lexical Features**: Analyze the number of digits, subdomains, and special characters in the URL.
    *   **Domain-Based Features**: Use a library like `python-whois` to check the domain's age or expiration date. Phishing sites often have recently created domains.
    *   **Content-Based Features**: For a more advanced system, you could crawl the page and analyze its content for suspicious keywords, hidden iframes, or forms that submit to a different domain.

## Potential Future Enhancements

This project has a strong foundation that can be built upon. Here are some ideas for future development:

*   **Browser Extension**: Create a Chrome or Firefox extension that automatically checks the user's current URL and displays a warning for suspicious sites. This would make the tool far more practical for daily use.
*   **Public API**: Expose the prediction functionality as a public REST API. This would allow other developers to integrate PhishShield's detection capabilities into their own applications.
*   **User Feedback Loop**: Add a feature that allows users to report if a URL was classified incorrectly. This feedback could be collected and used to retrain and improve the model over time.
*   **QR Code Analysis**: Add a feature to upload an image of a QR code. The application would first extract the URL from the image and then perform the phishing analysis on it.
*   **Modern Frontend**: Rebuild the frontend using a modern JavaScript framework like **React** or **Vue.js** to create a more dynamic and responsive user experience.
*   **Dockerization**: Package the application in a Docker container for easy, consistent deployment across different environments.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
