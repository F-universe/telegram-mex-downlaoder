from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Configura il percorso per ChromeDriver
chrome_driver_path = 'C:/Users/fabio/OneDrive/Desktop/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe'



# Percorso del file di output
output_file_path = 'C:/Users/fabio/OneDrive/Desktop/telegram/output.txt'

# Configura il servizio di ChromeDriver
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # Avvia il browser in modalità massimizzata

# Avvia il browser
driver = webdriver.Chrome(service=service, options=options)

# Apri Telegram Web
driver.get('https://web.telegram.org/a/#-1001243412416')

# Attendi che l'utente acceda manualmente
input("Premi Invio dopo aver effettuato l'accesso a Telegram...")

# Cerca i messaggi con la classe "message-date-group"
messages = driver.find_elements(By.CLASS_NAME, 'message-date-group')

# Scrivi i dati trovati in un file di testo
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for message in messages:
        # Estrai il testo del messaggio
        message_text = message.text

        # Estrai tutti gli orari all'interno del messaggio
        time_elements = message.find_elements(By.CSS_SELECTOR, 'time')
        
        # Se ci sono orari, aggiungi un separatore dopo ciascuno
        for time_element in time_elements:
            message_time = time_element.text
            output_file.write(f'Orario: {message_time}\n')

        # Scrivi il testo del messaggio
        output_file.write(f'Messaggio:\n{message_text}\n')
        output_file.write('-' * 50 + '\n')  # Separatore tra messaggi

print(f'Dati estratti e salvati in {output_file_path}')

# Chiudi il browser
driver.quit()
