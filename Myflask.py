from flask import Flask, render_template, request
import spacy
import os

app = Flask(__name__)

# Load the trained machine learning model
model_path = 'D:/dataabstarction/model-last'
nlp = spacy.load(model_path)

# Define entity colors
colors = {
    "MICROORGANISM": "#D291BC",
    "CELL": "#39CCCC",
    "GENE": "#2ECC40",
    "COMPOUND": "#6B3FA0",
    "DIESEASE": "#FF4136",
    "SYMPTOMS": "#FF851B",
    "ORG": "#0074D9",
    "PROTEIN": "#B10DC9",
    "AGENT": "#001F3F",
    "MEDICINE": "#AF7AC5",
    "TREATMENT": "#F012BE",
    "TOOL": "#B7950B",
    "PERCENTAGE": "#FF00FF",
    "ENZYME": "#3D9970",
    "NUCLEIC_ACID": "#FFC125",
    "CARDINAL": "#AAAAAA",
    "DATE": "#001F3F",
    "LOC": "#444444",
    "CONDITION": "#FFDAB9",
    "AMINO_ACID": "#FFDB58"
}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tag', methods=['POST'])
def tag_entities():
    text = request.form['input_text']
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Build entity options with colors
    options = {"ents": [ent.label_ for ent in doc.ents], "colors": colors}
    tagged_text = spacy.displacy.render(doc, style='ent', jupyter=False, options=options)
    return render_template('predictions.html', entities=entities, tagged_text=tagged_text)

if __name__ == '__main__':
    app.run(debug=True)
