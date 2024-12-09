﻿# bottlepos5-QA Script In Python

### **Step to Installitions Process For Windows/Mac**

* Install Python>3 On your System.
* Create Vertual Env [Click Here](https://docs.python.org/3/library/venv.html)
* Activate Vertual Env
* Clone Project:

```
git clone https://github.com/BottlePos/bottlepos5-qa.git
```

* cd bottlepos5-qa
* Run Command:

  ```
  pip3 install -r requirements.txt
  ```
* Downlaod Chrome Driver [Click Here](https://chromedriver.chromium.org/downloads)
* ***Note:- Make Sure Your System Browser and Driver Version are Same!***
* Put ChroméDrive Inside `chromeDriver` Folder
* cd testCases
* Run Command

```
pytest -v -s test_ReceiveItems.py --browser chrome
```
