# Password Manager Mac App

This is a simple password manager app for macOS. You can use this app to generate strong passwords, store them, and search for passwords by website name. The app is packaged using PyInstaller for easy distribution.

## Installation

Before running the app, make sure you have Python and PyInstaller installed.

```bash
pip install pyinstaller

Build the App
To build the macOS app, follow these steps:

Navigate to the folder containing your Python script (e.g., your_script_name.py).

Run PyInstaller to package your Python script as an executable macOS application:

bash
Copy code
pyinstaller --onefile your_script_name.py
Replace your_script_name.py with the actual name of your Python script.

After PyInstaller finishes, you'll find a dist folder within your app folder. Inside this folder, there will be an executable file with the same name as your Python script.

Run the App
To run the app, follow these steps:

Double-click the executable file found in the dist folder. This will open the password manager app on your Mac.

Use the app to generate passwords, store them, and search for passwords by website name.

Contributing
If you'd like to contribute to this project, feel free to open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
PyInstaller - Used to package the app.

Happy password managing!🤓

