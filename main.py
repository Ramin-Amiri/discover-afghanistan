from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


app = QApplication([])

loader = QUiLoader()

ui_file = QFile("main.ui")
ui_file.open(QFile.ReadOnly)

window = loader.load(ui_file)

ui_file.close()


province_data = {

    "Kabul": {
        "capital": "Kabul",
        "food": "Kabuli Pulao",
        "population": "5.3 million",
        "description": "Capital city of Afghanistan and its largest urban center."
    },

    "Herat": {
        "capital": "Herat",
        "food": "Mantu",
        "population": "670,000",
        "description": "Known for poetry, art, and historical architecture."
    },

    "Kandahar": {
        "capital": "Kandahar",
        "food": "Lamb dishes",
        "population": "730,000",
        "description": "Historic city in southern Afghanistan."
    },

    "Mazar-i-Sharif": {
        "capital": "Mazar-i-Sharif",
        "food": "Ashak",
        "population": "570,000",
        "description": "Known for the famous Blue Mosque."
    },

    "Bamyan": {
        "capital": "Bamyan",
        "food": "Local potato dishes",
        "population": "100,000",
        "description": "Famous for mountains and ancient Buddha sites."
    }

}

    

def show_info():

    province = window.provinceBox.currentText()

    data = province_data[province]

    window.capitalLabel.setText(
        f"Capital: {data['capital']}"
    )

    window.foodLabel.setText(
        f"Food: {data['food']}"
    )

    window.populationLabel.setText(
        f"Population: {data['population']}"
    )

    window.descriptionLabel.setText(
        f"Description: {data['description']}"
    )


window.showButton.clicked.connect(show_info)

window.setWindowTitle("Discover Afghanistan")

window.show()

app.exec()