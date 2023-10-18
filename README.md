# todo_assessment
To-Do Web App

To Run the both applications, please see below steps:

1. git clone https://github.com/ZakesB/todo_assessment.git
2. cd todo_assessment
3. *run* docker build -t todo-server-app . 
4. *run*  docker build -t todo-portal-app .  
5. docker run -d --name todo-server-app -p 5001:5001 todo-server-app 
6. docker run -d --name todo-portal-app -p 5002:5002 todo-portal-app
7. In your browser, access the To-Do web app with: http://localhost:5002