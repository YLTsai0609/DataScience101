# Summary

01. people read lines randomly

02. give yourself some clue to understand what exactly you were doing before.

# Outline

01. Why
02. Be consistent & exact
03. general rules for clues
04. callable clues
05. return value clues
06. avoid none and null
07. specific clues for string
08. specific clues for numeric
09. structrue clues
10. private clues
11. performance lcues
12. paragraph and section

# Why

01. human read lines randomly - To understandf a random line, the lines you need to read back
02. time is money

# Be consistent & exact

Don't

``` Python
user = User(user_id)
buyer = user_id
```

Do

``` Python
buyer = User(user_id)
buyer_id = user_id
```

Don't

``` Python
result = ...
result = ...
```

Do 

``` Python
resp = ...
parsed_dict = ...
```

**Give yourself a clues**

## Examples

**Clue the ops you should use**

Warning

``` Python
page = ...
```

Do

``` Python
page_no = ...
page_html = ...
```

Warning

``` Python
user = User(...)
user = {}
```

Do

``` Python
user = User(...)
user_dict = {}
```

# method or attribute?

method, function -> use verb + noun

Warning

``` Python
resp.text
resp.json # !?
```

Do

``` Python
resp.text

resp.parse_as_json()
```

## General Rule

General rules

| convention | for   |
|------------|-------|
| _no      | numeric |
|plural| sequences, usually is mutable sequence(list in python)|
|_type |if no intutive way|
|_seq| for sequence|
|_gen| for generator|

check in collections.abc

## Callable

| convention | for |
|------------|-----|
| verb_    | imperative sentence |
| is_ |  -> bool  |
|to_<thing>| -> thing|
|from_thing| -> thing|

## Return values

| example | explination |
|------------|-----|
| get_page_no    | numeric which >= 1 |
| query_user     |  -> user object  |
|parse_to_tree| -> tree object|

## Avoid None and Null

Consider:

``` Python
user = query_user(uid)
user_is_valid()

An AttributeError!
```

Two ways :

01. raise Error when you wanna return None
02. Use a dummy object like a dummy user or an empty str, empty list 

## Common strategy

for string 

1. _key (of a dict)
2. _json (means it is a json)
3. _url (means it is a string)
4. _html (means it is jtml)
5. _sql (means sql)
6. _re (means something regular expression like email_re)

for numeric 

01. _no -> >= 1
2. _idx -> >= 0 (or just i, j, k)
3. _secs (means secs)
04. _pct -> percentage!
5. _month, _day, ... (date basis)

## Structrue clues

Don't

``` Python
users = {
 'mosky': 'mosky.tw@gmail.com',
 ...
}

```

Do 

``` Python
uid_email_dict = {
 'mosky': 'mosky.tw@gmail.com',
 ...
}
```

Even Better

``` Python
uid_email_pair = {
 'mosky': 'mosky.tw@gmail.com',
 ...
}

# why?

# becuase

for uid, email in uid_email_pair:
    ...
    # seems perfect right?
```

# Private clues

**don't use me!**

this thing will not out of the module/class

_<name>

# Performance clues

**provide the refactor clue!**
**should I cache it or not?**

| convention     | for                 |
|----------------|---------------------|
| get_ / set_    | memory op           |
| parse_ / calc_ | CPU / GPU bound op  |
| query_         | IO-bound            |
| query or _get_ | IO-bound with cache |

# Paragraph and sections

``` Python

############### check arguments ##############

your code here

############### query from tables ##############

your code here

############### transform##############

your code here
```

# Line Units Up

01. make sure your code follow one way data flow
02. mark #TODO to help the future developer to notice the paragraph of code should be better!

# Reference

[Boost Maintainability](https://speakerdeck.com/mosky/boost-maintainability)
