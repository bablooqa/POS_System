pytest -v -s --html=Reports/additem.html testCases/test_addItem.py --browser chrome
pytest -v -s --html=Reports/additem.html testCases/test_CheckCentralItem.py --browser chrome
pytest -v -s --html=Reports/additem.html testCases/test_addItem.py --browser firefox
pytest -v -s --html=Reports/additem.html testCases/test_CheckCentralItem.py --browser firefox

Rem pytest -s -v -m "sanity" --html=./Reports/sanity_result.html testCases/test_login.py --browser chrome
Rem pytest -s -v -m "sanity or regression" --html=./Reports/sanity_result.html testCases/ --browser chrome
Rem pytest -s -v -m "sanity and regression" --html=./Reports/sanity_result.html testCases/ --browser chrome
Rem pytest -s -v -m "regression" --html=./Reports/sanity_result.html testCases/ --browser chrome

Rem pytest -s -v -m "sanity" --html=./Reports/sanity_result.html testCases/test_login.py --browser firefox
Rem pytest -s -v -m "sanity or regression" --html=./Reports/sanity_result.html testCases/ --browser firefox
Rem pytest -s -v -m "sanity and regression" --html=./Reports/sanity_result.html testCases/ --browser firefox
Rem pytest -s -v -m "regression" --html=./Reports/sanity_result.html testCases/ --browser firefox
 


