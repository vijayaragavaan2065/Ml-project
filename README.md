 MLProject - End-to-End Machine Learning Pipeline with Flask Deployment

This project demonstrates a complete end-to-end Machine Learning workflow, including data preprocessing, model training, evaluation, and deployment using Flask.

 Features

- Data ingestion and preprocessing
- Model training and saving (`model.pkl`)
- Preprocessor pipeline saving (`preprocessor.pkl`)
- Flask-based web UI for predictions
- Custom Exception handling and logging
- Modular and scalable project structure

## 🗂️ Project Structure
MLProject/
├── app.py # Flask application entry point
├── artifacts/ # Saved model artifacts
│ ├── data.csv
│ ├── train.csv
│ ├── test.csv
│ ├── model.pkl
│ └── preprocessor.pkl
├── src/
│ ├── init.py
│ ├── components/ # Model training and preprocessing
│ ├── pipeline/
│ │ ├── train_pipeline.py
│ │ └── predict_pipeline.py
│ ├── utils.py
│ └── exception.py
├── templates/
│ └── home.html # Web UI Template
├── static/ # CSS, JS, images if any
├── requirements.txt
└── README.md # Project documentation

## 🧑‍💻 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/MlProject.git
cd MlProject
2. Create and activate a virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Train the model (if not already trained)
Run your training pipeline script (modify path as per your file):

bash
Copy
Edit
python src/pipeline/train_pipeline.py
This generates the model.pkl and preprocessor.pkl files inside the artifacts/ directory.

5. Start the Flask app
bash
Copy
Edit
python app.py
The app will be available at http://127.0.0.1:5000.

🧪 Usage
Open the app in your browser.

Fill in the input form.

Submit to get predictions based on the trained model.

🛠️ Technologies Used
Python 3.9

Flask

Scikit-learn

Pandas / NumPy

Pickle (for model persistence)

HTML / Jinja for UI

📂 Artifacts
model.pkl: Trained model object

preprocessor.pkl: Preprocessing pipeline used before training

train.csv, test.csv: Dataset splits used during model training

🧯 Error Handling
Custom exceptions are handled using the CustomException class for better debugging.




