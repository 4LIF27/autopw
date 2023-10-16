<img src="https://i.postimg.cc/C1yfrx67/Screenshot-20230730-115511-Termux.jpg">

### Install 
```python
termux-change-repo
pkg update && pkg upgrade -y
pkg install python -y
pkg install git
pip install inquirer requests bs4 re urllib3
git clone https://github.com/zhukov-z/autopw
cd autopw
```
### Run
```python
python run.py
```
