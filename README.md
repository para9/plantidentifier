# # # Plant image Classification Model
# # # Software and Tools requirement

1.[Github Account](https://github.com)
2.[AWS Account](https://aws.amazon.com/)
3.[VSCodeIDE](https://code.visualstudio.com/)
4.[GitCLI](https://git-scm.com/)
5.[Filezilla Client](https://filezilla-project.org/)
6.[PuTTYgen](https://www.puttygen.com/)
7.[Docker](https://www.docker.com/)

Creta a new environment

---

python3 -m venv env 

---

Activate your enviornment

---

source env/bin/activate

---

Install all the necessary libraries from requirements.txt file

---

pip install -r requiremnts.txt

---

COnfig git user name and email

---

git config --global user.name ""
git config --global user.email "@xx.com"

----

ignore the file not needed to push and create gitignore if not created earlier

----
touch .gitignore
----

add the files to commit to git

---

git add .
git status
---

commit to git

---

git commit -m

---

push all the file to git

------

git push origin main

------

Export modle and preprocessed file to avoid hardcoded path to the files

----
import os

# Define the file paths relative to the project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE_PATH = os.path.join(PROJECT_ROOT, 'models', 'my_model.h5')
PREPROCESSED_FILE_PATH = os.path.join(PROJECT_ROOT, 'preprocessed', 'preprocessed_features.npy')
PLANT_DETAILS_FILE_PATH = os.path.join(PROJECT_ROOT, 'data', 'Plant name and properties.xlsx')
#saved it as config.py
#
---------