# Photo Galore
 An app that displays images

## Built by Brian Mutuma

### Project description
- Photo galore is a gallery where one can upload images detailed with; location, description and its category.

## USER STORIES
View my photos as posted.
Click on a single photo to expand it and also view the details of that specific photo. The photo details must appear on a modal within the same route as the main page.
Search for different categories of photos. (ie. HIking, code)
Copy a link to the photo to share with your friends.

# SetUp / Installation Requirements
0. Clone the repo by running:
- https://github.com/Brian-M-code/photo-galore.git
0. Navigate to the project directory;
1. cd Gallery
1. Create a virtual environment and activate it
`python3 -m venv virtual`
`. virtual/bin/activate`
2. Create a database using postgress, type the following commands;
`$psql`
3. Then run the command to create a new database
`create database gallery`
4. Install dependencies
`pip install -r requirements.txt`
5. Create database migrations
`python3 manage.py makemigrations photoz`
`python3 manage.py migrate`
6. Run the app
`python3 manage.py runserver`

## TECHNOLOGIES USED
1. Django
4. Bootstrap
3. Postgres

## For infor on collaboration, follow along the normal procedure and let's get collaborating.

### Livelink
- https://g-galore.herokuapp.com/

