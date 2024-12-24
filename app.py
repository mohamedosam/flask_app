from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# تحميل قاعدة البيانات
gender_data = pd.read_csv('assets/gender_list.csv')

@app.route('/check_gender', methods=['POST'])
def check_gender():
    data = request.get_json()
    word = data.get('word', '').strip().lower()
    
    result = gender_data[gender_data['word'] == word]
    
    if not result.empty:
        gender = result['gender'].values[0]
        return jsonify({'gender': gender})
    else:
        return jsonify({'gender': 'unknown'})
    
if __name__ == '__main__':
    app.run(debug=True)
