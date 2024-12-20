from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Load Table 1
data = pd.read_csv('Table1.csv') 
data.columns = ['Index', 'Value']  

@app.route('/')
def display_tables():
    # Render Table 1 as HTML
    table1_html = data.to_html(index=False)

    value_dict = data.set_index('Index')['Value']  # Create a dictionary

    # Calculate values for Table 2
    alpha = value_dict['A5'] + value_dict['A20']  # A5 + A20
    beta = value_dict['A15'] // value_dict['A7']  # A15 / A7 
    charlie = value_dict['A13'] * value_dict['A12']  # A13 * A12

    # Create Table 2
    table2 = pd.DataFrame({
        'Category': ['Alpha', 'Beta', 'Charlie'],
        'Value': [alpha, beta, charlie]
    })

    # Render Table 2 as HTML
    table2_html = table2.to_html(index=False)

    # Render both tables in an HTML template
    return render_template('index.html', table1_html=table1_html, table2_html=table2_html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
