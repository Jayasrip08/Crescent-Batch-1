# Backend Development – Today's Task
## Topic: REST API – Data Manipulation

### Objective

Extend the portfolio website created in the previous class by implementing REST API operations.

Today, you will use **GET, POST, PUT, and DELETE** requests to manage portfolio data.

You may implement the task using any backend technology taught in class.

---

## Starting Point

Your portfolio already contains pages such as:

- Home
- About
- Contact

Now add a collection of **projects** to your backend.

You do **not** need to use a database.

Store some sample project data temporarily in your backend application.

Example data:

```json
[
    {
        "id": 1,
        "title": "Portfolio Website",
        "description": "My personal portfolio website"
    },
    {
        "id": 2,
        "title": "Weather App",
        "description": "A simple weather application"
    }
]
```

---

# Task 1 – GET All Projects

Create an endpoint:

```text
GET /projects
```

It should return all available projects.

Expected response:

```json
[
    {
        "id": 1,
        "title": "Portfolio Website",
        "description": "My personal portfolio website"
    },
    {
        "id": 2,
        "title": "Weather App",
        "description": "A simple weather application"
    }
]
```

---

# Task 2 – GET Project by ID

Create an endpoint:

```text
GET /projects/:id
```

Example:

```text
GET /projects/1
```

It should return only the project with ID `1`.

If the project does not exist, return:

```text
404 Not Found
```

---

# Task 3 – POST a New Project

Create an endpoint:

```text
POST /projects
```

Send project information through the request body.

Example:

```json
{
    "title": "Student Management System",
    "description": "A simple student management application"
}
```

Your backend should:

1. Receive the data.
2. Create a new project.
3. Assign an ID.
4. Add it to the existing project collection.
5. Return the newly created project.

Use:

```text
201 Created
```

for a successful creation.

---

# Task 4 – PUT to Update a Project

Create an endpoint:

```text
PUT /projects/:id
```

Example:

```text
PUT /projects/2
```

Request body:

```json
{
    "title": "Updated Weather App",
    "description": "Weather application with additional features"
}
```

Update the corresponding project.

If the project does not exist, return:

```text
404 Not Found
```

---

# Task 5 – DELETE a Project

Create an endpoint:

```text
DELETE /projects/:id
```

Example:

```text
DELETE /projects/2
```

Remove the corresponding project.

Return a response such as:

```json
{
    "message": "Project deleted successfully"
}
```

If the project does not exist, return:

```text
404 Not Found
```

---

# Task 6 – Test Your API

Use an API testing tool to test all four HTTP methods.

Test:

```text
GET     /projects

GET     /projects/1

POST    /projects

PUT     /projects/1

DELETE  /projects/1
```

Make sure your POST and PUT requests send data as JSON.

---

# Bonus Task – Middleware

Create a simple middleware that logs information about every incoming request.

It should display:

```text
Method: GET
URL: /projects
```

Another example:

```text
Method: POST
URL: /projects
```

The middleware should run before the corresponding route is processed.

---

# Expected Outcome

By the end of the task, your portfolio backend should support:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/projects` | View all projects |
| GET | `/projects/:id` | View one project |
| POST | `/projects` | Add a project |
| PUT | `/projects/:id` | Update a project |
| DELETE | `/projects/:id` | Delete a project |

The main goal is to understand how **GET retrieves data, POST creates data, PUT modifies existing data, and DELETE removes data** through a REST API.