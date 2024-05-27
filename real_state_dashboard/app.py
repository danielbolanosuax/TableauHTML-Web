from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Cargar datos del archivo Excel
    file_path = r"C:\Users\Daniel Bolaños\Downloads\real_estate_data.xlsx"
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        return "El archivo no se encontró. Verifique la ruta del archivo.", 404
    except Exception as e:
        return f"Se produjo un error al leer el archivo: {e}", 500

    # Procesar datos (ejemplo: convertir a lista de diccionarios)
    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

