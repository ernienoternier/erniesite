story wall

db story:

id
title 
content
date
user


sql:
CREATE TABLE story (
  id serial primary key,
  title text,
  content text,
  created timestamp default now(),
  user text);

  insert into story(title, content, user) values('first story', 'excited','god');   