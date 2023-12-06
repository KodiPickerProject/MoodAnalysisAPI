
# Mood Analysis API

Due to Kodi limitations we created an API for the user to run on their local machine.


## Installation

- Download the latest release and place it in a folder on your local machine.
- Unzip the folder, MoodAnalysisAPI-main.zip
- Navigate to the directory of the unzipped folder and, make the script, requirements.sh executable and then run exec.sh.
- Once all the dependencies are properly installed, run the flask app by using the following command, 'python3 -m flask run'
- Ensure the API is running on http://127.0.0.1:5000.
- While the API is running you can now open QuickPicker and do the following:
    - Select 'Mood'
    - Select 'Update Movie Info'
    - Select 'Yes'

```bash
  unzip MoodAnalysisAPI.zip
  cd MoodAnalysisAPI
  chmod +x requirements.sh
  ./requirements.sh
```
### Note
- After you have ran requirements.sh and wish to update your movie info, you can simply run...
```bash
  python3 -m flask run
```
- And proceed to open QuickPicker:
    - Select 'Mood'
    - Select 'Update Movie Info'
    - Select 'Yes'
