# todo_list_api
An API which is used to view the tasks and states of tasks of different users

## Available endpoints

### Users

*   GET ``` http://127.0.0.1:5000/users/ ``` : to get a list of all registered users
*   *  GET ``` http://127.0.0.1:5000/users/name/ ``` : to search for a user using their name
*   POST ``` http://127.0.0.1:5000/user/ ``` : to create a user
*   PUT ``` http://127.0.0.1:5000/user/id/ ``` : to edit a user's name (search for the user by using their id)
*   DELETE ``` http://127.0.0.1:5000/user/name/ ``` : to delete a user's account

### Todo Tasks  
*   GET ``` http://127.0.0.1:5000/todos/ ``` : returns a list of all created tasks
*   GET ``` http://127.0.0.1:5000/todo/id/ ``` : returns a specific task based on the user's id
*   POST ``` http://127.0.0.1:5000/todo/ ``` : to create a new task
*   PUT ``` http://127.0.0.1:5000/todo/id/ ``` : to edit a user's task (search for the user via their id)
*   DELETE ``` http://127.0.0.1:5000/todo/id/ ``` : to delete a user's task(s)
   
## How to test endpoints
We test making use of [Postman](https://www.postman.com/)

*   GET all users
![GET users](https://user-images.githubusercontent.com/49791498/103224805-b5a5e600-4928-11eb-8047-b50d72d7a702.png)

*   GET a user by username/name
![GET user](https://user-images.githubusercontent.com/49791498/103224914-06b5da00-4929-11eb-943e-5a2342c96010.png)

*   POST (create a user)
![Create a user](https://user-images.githubusercontent.com/49791498/103225018-4250a400-4929-11eb-90dd-ac08fb151363.png)

*   PUT (edit a user's name)
![edit a user's name](https://user-images.githubusercontent.com/49791498/103225149-9d829680-4929-11eb-9269-e5af7be6ab9f.png)

*   DELETE (delete a user's account)
![Delete a user's account](https://user-images.githubusercontent.com/49791498/103225285-e1759b80-4929-11eb-8fc8-cc4ccc092afe.png)

*   GET all tasks
![view all tasks](https://user-images.githubusercontent.com/49791498/103225424-28639100-492a-11eb-80e4-bf3f03b9cc09.png)

*   GET a specific task
![view a specific task](https://user-images.githubusercontent.com/49791498/103225475-47622300-492a-11eb-860e-494d3f0ce8f9.png)

*   POST (create a task)
![create a task](https://user-images.githubusercontent.com/49791498/103225603-93ad6300-492a-11eb-8298-32cfa0bfeb52.png)

*   PUT (edit a task)
![edit a task](https://user-images.githubusercontent.com/49791498/103225705-da9b5880-492a-11eb-9967-11a15f9a238d.png)

*   DELETE (delete a task)   
![delete a user](https://user-images.githubusercontent.com/49791498/103225909-41207680-492b-11eb-9008-684a6fdecea8.png)
  