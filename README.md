# password_generator

A simple API to generate a random password.

# API description

GET request to https://varvara-passgen.herokuapp.com/passgen/api/v1.0/
<br>
<br>
**Parameters:**
```
passlen (int): Password length
```
**Returns:**
```
{
passlen (int or None): Input password length
response (str or None): Random password
error (str, optional): Error description
}
```

# Command line usage examples

1.
```
$ curl -i -H "Content-Type: application/json" -X GET -d '{"passlen": 10}' https://varvara-passgen.herokuapp.com/passgen/api/v1.0/
>> {"passlen":10,"response":"?'^-6\"Li/'"}
```

2.

```
$ curl -i -H "Content-Type: application/json" -X GET -d '{"passlen": 20}' https://varvara-passgen.herokuapp.com/passgen/api/v1.0/
>> {"passlen":20,"response":"HX@Kiv0=[%sUlBGzlL7n"}
```

# Used technology stack

1. [Python Secrets](https://docs.python.org/3/library/secrets.html/): Python3 module for generating cryptographically strong random numbers
2. [Flask API](https://flask.palletsprojects.com/en/1.1.x/): Web application framework
3. [Heroku server](https://www.heroku.com/): Cloud server platform

# TODO

1. Enable custom alphabet as input
2. Enable password restrictions (i.e. at least one capital letter, etc.)
