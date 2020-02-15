## Jokes

An app to share jokes and make other people laugh when they see your jokes.

## Installation

- ``` virtualenv .env -p python3 ```
- ``` source .env/bin/activate ```
- ``` pip3 install virtualenv ```
- ``` pip3 install flask ```
- ``` pip3 freeze > requirements.txt ```

# How to use the app

* Register to have access to the site
* Once registered, you can see all of the posts from other people. Just click one of the posts to see the joke.
* You can post a joke.
* You can also edit your joke or delete them.

# Tables

![alt text](https://i.imgur.com/Lo1Fw2S.jpg?1)

# Wireframes

![alt text](https://i.imgur.com/FaHfXPK.jpg?1)
![alt text](https://i.imgur.com/sLLYGz9.jpg?2)

# Models
-- User
```
class User(UserMixin, Model):
	first_name = CharFeild()
	last_name = CharField()
	email = CharField(unique=True)
	username = CharField(unique=True)
	password = CharField()
```

-- Joke
```
class User(UserMixin, Model):
	title = CharFeild()
	joke = CharField()
	owner = CharField(User, backref='jokes')
	created_at = DateTimeField(default=datetime.datetime.now)
```

# User Stories

The user first must register or log in.

If they pick register, it will bring them to the registration page. Here they can fill out their information such as username, password, first name, last name and email address.

After they registerd, they will be on the home page. Where they can see all of the resent jokes submissions with their titles.

On that page they will have a new link in the nav, which will take them to the create page, my jokes link which will take them to all of theirs posts, home which will take them to the home page with all the posts, and a logout link, which will log them out.

In the new page, they will have a form that will require a title for the joke, and the joke. The onwer will be added automatically.

If they click one of the posts, it will take them to the show page that will have the information about that joke. It will contain the title, joke, author and date. Also, it will have a delete button and edit button, but only if you are the owner of the joke.

When the user back in, it will take them straight to the index page that will have all the most recent activity.

## Nice to have

Allow the user to like post, edit their account, delete their account and jokes with a picture if they preffere.

## Built with

* Flask api
* React

# Author

[Nehemias Alcantara](https://github.com/nemiasalc56)