# web-directory-scanner
A simple web app that use gobuster and secList to scan URLs looking for hidden directories
![imagen](https://github.com/user-attachments/assets/831361fa-821d-49de-a79b-7a605604e752)
![imagen](https://github.com/user-attachments/assets/554d7f27-c1b1-417b-8ea7-b67e33e829c1)

## How to use?
Just install flask, gobuster

`
pip install flask
sudo apt install gobuster
`

Luego clonar el repositorio de seclist y añadirlo a usr

`
git clone https://github.com/danielmiessler/SecLists.git
sudo mv SecLists /usr/share/seclists
`

Por ultimo solo queda ejecutar la app

`
python3 app.py
`
