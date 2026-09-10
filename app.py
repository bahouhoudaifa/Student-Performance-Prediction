import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Load the dataset and create the regression model
# df = pd.read_csv(r"C:\Users\dell\Transformed_Student_Performance.csv")
file_path = r"C:\Users\dell\Transformed_Student_Performance.csv"  
df = pd.read_csv(file_path)


X = df[["Hours Studied", "Previous Scores", "Extracurricular Activities", "Sleep Hours", "Sample Question Papers Practiced"]]
y = df["Performance Index"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the values from the form
        hours_studied = float(request.form["hours_studied"])
        previous_scores = float(request.form["previous_scores"])
        extracurricular_activities = float(request.form["extracurricular_activities"])
        sleep_hours = float(request.form["sleep_hours"])
        sample_question_papers_practiced = float(request.form["sample_question_papers"])

        # Prepare input data for prediction
        input_data = pd.DataFrame([[hours_studied, previous_scores, extracurricular_activities, sleep_hours, sample_question_papers_practiced]],
                                  columns=["Hours Studied", "Previous Scores", "Extracurricular Activities", "Sleep Hours", "Sample Question Papers Practiced"])

        # Predict performance index
        prediction = reg.predict(input_data)
        result = f"L'indice de performance prédit est : {prediction[0]:,.2f}"

        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
