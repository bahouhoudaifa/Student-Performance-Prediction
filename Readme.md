# Student Performance Prediction

This project is a Flask web application that predicts a student's performance index using a multiple linear regression model.

The model uses these input features:

- Hours Studied
- Previous Scores
- Extracurricular Activities
- Sleep Hours
- Sample Question Papers Practiced

## Requirements

- Python 3.9 or newer
- A CSV dataset named `Transformed_Student_Performance.csv`

The CSV must contain these columns:

```text
Hours Studied
Previous Scores
Extracurricular Activities
Sleep Hours
Sample Question Papers Practiced
Performance Index
```


## Run the application

With the virtual environment activated, run:

```powershell
python app.py
```

The Flask development server will start at:

```text
http://127.0.0.1:5000
```

Open that address in a web browser, enter the student's information, and submit the form to view the predicted performance index.

To stop the server, press `Ctrl+C` in PowerShell.

## Project structure

```text
pr/
├── app.py
├── Readme.md
└── templates/
	└── index.html
```

## Notes

- The application runs Flask in debug mode for local development.
- The regression model is trained when `app.py` starts.
- The displayed prediction is formatted as a value out of 100.
