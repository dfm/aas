pragma foreign_keys = ON;

drop table if exists sessions;
create table sessions (
  id integer primary key autoincrement,
  aas_id integer,
  title text,
  date text,
  type text,
  room text
);

drop table if exists abstracts;
create table abstracts (
  id integer primary key autoincrement,
  session_id integer references sessions(id),
  aas_id integer,
  title text,
  abstract text,
  counts text
);


drop table if exists authors;
create table authors (
  id integer primary key autoincrement,
  abstract_id integer references abstracts(id),
  name text
);
