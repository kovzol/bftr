create table groupkinds (
 id int serial,
 name varchar(20)
 );

insert into groupkinds (name) values ('good');
insert into groupkinds (name) values ('evil');
insert into groupkinds (name) values ('neutral');

create table species (
 id int serial,
 name varchar(20),
 groupkind int references groupkind(id),
 strength int
 );

create function groupkind_id(varchar) as
 'select id from groupkind where name like $1 || ''%'' order by name limit 1'
 language 'sql';

insert into species (name, groupkind, strength) values ('cavalry', 'g', 10);
insert into species (name, groupkind, strength) values ('infantry', 'g', 6);
insert into species (name, groupkind, strength) values ('elf', 'g', 12);
insert into species (name, groupkind, strength) values ('dwarf', 'g', 11);
insert into species (name, groupkind, strength) values ('hobbit', 'g', 2);
insert into species (name, groupkind, strength) values ('troll', 'e', 10);
insert into species (name, groupkind, strength) values ('orc', 'e', 3);
insert into species (name, groupkind, strength) values ('nazgul', 'e', 20);
insert into species (name, groupkind, strength) values ('wolf', 'e', 4);

create table game (
 id int serial,
 start timestamp not null default now(),
 end timestamp,
 paused boolean,
 pause_request int references groupkind(id));

-- Warning: this is incomplete!
