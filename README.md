# Second-hand Trading Platform 

<div align="center">
  <img src="./assets/cover.png" alt="logo" width="600">
</div>

## Introduction
The website is for the final project of web app programming course @ NTU. In this project, a second-hand trading platform website is designed, and there are lots of function included like chating room, articles slider and campaign block.

## Prerequisites
* [python requirements](./requirements.txt)
* redius server
* virtual environment (optional)

## Setup & Run
1. Clone the repository to the local side.
```
https://github.com/KoKoLates/trading-platform-website.git
```

2. Navigate to the project directory.
3. Create and activate a virtual environment. It is recommended to use virtual environments to isolate project dependencies. (optional)
```shell
python -m venv .venve
.venv\Script\activate # for windows user
```

4. Install the required packages.
```shell
pip install -r requirements.txt
```
5. Open another new terminal window and run the following command for the Redis server.
```shell
redis-server
```
6. Run the development server. 
```shell
python manager.py runserver
```
7. Then you could access to our project website in brower at [`http://localhost:8000`](http://localhost:8000)


## Overview
Please note that the above instructions assume a windows-based system. If you are using a other operating system, make sure to use the appropriate commands or tools as needed. 
<br><br>
[`report`](./assets/final_report.pdf) 、 [`demo slide`](./assets/final_slides.pdf)