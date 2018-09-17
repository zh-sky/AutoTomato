update test_user set age = 11 where id = 2;
update test_user set age = 23 where id = 3;
update test_user set age = 34 where id = 4;
update test_user set age = 45 where id = 5;
update test_user set age = 56 where id = 6;
update test_user set age = 67 where id = 7;
update test_user set age = 78 where id = 8;
update test_user set age = 89 where id = 9;
update test_user set age = 18 where id = 10;
update test_user set age = 30 where id = 11;
update test_user set age = 26 where id = 12;
update test_user set age = 27 where id = 13;

--查询编号，性别，用户名详情 以及组中总人数按照性别分组--
select id,sex,groip_concat(username) as users,count(*) as totalUsers from test_user group by sex;

--统计表中所有记录--
select count(*) as totalUsers from test_user;
select count(id) as totalUsers from test_user;

count(字段)不统计null值

--查询编号，性别，用户名详情，组中总人数，组中最大年龄、最小年龄和平均年龄以及年龄总和--
select id,sex,group_concat(username),
count(*) as totalUsers,
max(age) as max_age,
min(age) as min_age,
avg(age) as avg_age,
sum(age) as sum_age
from test_user
group by sex;

--通过having子句对分组结果进行二次筛选--
--查询性别sex，用户名详情，组中总人数，最大年龄，年龄总和 根据性别分组。
select sex,group_concat(username) as users,
count(*) as totalUsers,
max(age) as max_age,
sum(age) as sum_age
from test_user
group by sex;

-- 查询组中人数大于2的 --
select sex,group_concat(username) as users,
count(*) as totalUsers,
max(age) as max_age,
sum(age) as sum_age
from test_user
group by sex
having count(*) >2;

--查询组中人数大于2并且最大年龄大于80--
select sex,group_concat(username) as users,
count(*) as totalUsers,
max(age) as max_age,
sum(age) as sum_age
from test_user
group by sex
having count(*) >2 and max(age) > 80;

--编号大于等于2的用户--
select sex,group_concat(username) as users,
count(*) as totalUsers,
max(age) as max_age,
sum(age) as sum_age
from test_user
where id >=2
group by sex
having count(*) >2 and max(age) > 60;

--order by 对查询结果进行排序--
--按照id降序排列desc 默认是asc
select *from test_user order by id;
select *from test_user order by id asc;
select *from test_user order by id desc;

--按照年龄升序排列--
select *from test_user order by age;
select *from test_user order by age desc;


--按照id降序年龄升序来排列--
select *from test_user order by id desc,age asc;

--实现随机提取记录--
select *from test_user order by rand();

-- limit限制查询结果显示的条数--
--查询表中前3条记录--
select *from test_user limit 3;
select *from test_user order by id desc limit 5;

--查询表中前一条记录--
select *from cms_user limit 1;

select id,sex,age,group_concat(username),
count(*) as totalUsers,
max(age) as max_age,
min(age) as min_age,
avg(age) as avg_age,
sum(age) as sum_age
from test_user
where id >=3
group by sex
having count(*) >=2
order by age desc
limit 0,2;

--更新用户名为4位的用户 让其已有年龄减三--
update test_user set age=age-3 where username like '____';

--更新前三条记录 年龄加10--
--在更新或者删除的时候 limit只能有一个参数--
update test_user set age=age+10 limit 3;

--删除用户性别为男的用户，按照年龄降序排列，删除前1条记录--
delete from test_user where sex='男' order by age desc limit 1;



--查询test_user表中 id,username,email,sex
--查询provinces表中proName
select u.id,u.username,u.email,u.sex,p.proName
from test_user as u
inner join provinces as p

on u.proId=p.id;

--查询test_user id,username,sex
--查询provinces proName
--条件是test_user的性别为男的用户
select u.id,u.username,u.sex,p.proName
from test_user as u
join
provinces as p
on u.proId=p.id
where u.sex='男';

--根据proName分组
select u.id,u.username,u.sex,p.proName
from test_user as u
join
provinces as p
on u.proId=p.id
where u.sex='男'
group by p.proName;

--对分组结果进行筛选 跳出组中人数大于等于1的--
select u.id,u.username,u.sex,p.proName
from test_user as u
join
provinces as p
on u.proId=p.id
where u.sex='男'
group by p.proName
having count(*) >= 1;

--按照id升序排列--
select u.id,u.username,u.sex,p.proName
from test_user as u
join
provinces as p
on u.proId=p.id
where u.sex='男'
group by p.proName
having count(*) >= 1
order by u.id;

--限制显示条数--
select u.id,u.username,u.sex,p.proName
from test_user as u
join
provinces as p
on u.proId=p.id
where u.sex='男'
group by p.proName
having count(*) >= 1
order by u.id
limit 0,2;


-- 查询cms_new中的id,title,
-- 查询cms_cate中的cateName,
select n.id,n.title,c.cateName
from cms_news as n
join
cms_cate as c
on n.cId = c.id;

-- cms_news id,title
-- cms_admin username role
select n.id,n.title,a.username,a.role
from
cms_news as n
join
cms_admin as a
on n.aId = a.id;

-- cms_news id.title
-- cms_cate cateName
-- cms_admin username role
select n.id,n.title,c.cateName,a.username,a.role
from
cms_cate as c
join
cms_news as n
on c.id = n.cId
join
cms_admin as a
on n.aId = a.id;

-- 左外连接 left join  右外连接right join--


--创建部门表 deparment(主表)--
-- id,depName depDesc
create table if not exists deparment(
id tinyint unsigned auto_increment key,
depName varchar(20) not null unique
)engine=innodb;

insert deparment(depName) values ('教学部'),
	('市场部'),
	('运营部'),
	('督导部');

-- 创建员工表employee(字表)--
create table if not exists employee(
id smallint unsigned auto_increment key,
username varchar(20) not null unique,
depId tinyint unsigned
-- constraint emp_fk_dep foreign key(depId) references deparment(id)
-- foreign key(depId) refrecens deparment(id) on delete cascade on update cascade;--删除和添加的级联关系
)engine=innodb;

insert employee(username,depId) values ('king',1),
	('lulu',2),
	('tom',3),
	('kate',4);

--删除督导部-
delete from deparment where depName='督导部';


------------l联合查询----------
--联合查询 union去除重复
select username from employee union select username from test_user;
union all 只是简单的合并到一起 
select username from employee union all select username from test_user;


-------子查询---------
-- 由【not】in引发的子查询 --
select id,username from employee where id in (select id from deparment);

select id,username from employee where id not in (select id from deparment);


--创建学院表student
--id username score
create table if not exists student(
id tinyint unsigned auto_increment key,
username varchar(20) not null unique,
score tinyint unsigned
);

insert student(username,score) values ('king1',95),
	('king2',85),
	('king3',95),
	('king4',75),
	('king5',88),
	('king6',65),
	('king7',78),
	('king8',49),
	('king9',55);

-- 创建奖学金scholarship
-- id,level

create table if not exists scholarship(
id tinyint unsigned auto_increment key,
level tinyint unsigned
);

insert scholarship(level) values (90),(80),(70);

select id,username from student where score >=(select level from scholarship where id=1);

-- 查询所有获得奖学金的学员--
select id,username from student where score >=any(select level from scholarship);
select id,username from student where score >=some(select level from scholarship);

--查询获得一等奖学金的--
select id,username,score from student where score >=all(select level from scholarship);

-- 查询没有获得奖学金的学院--
select id,username,score from student where score <all(select level from scholarship

-- ^匹配字符开始的部分 --
-- 查询用户名以t开始的用户--
select *from test_user where username regexp '^t';


-- 创建普通索引--

create table test9(
id tinyint unsigned,
username varchar(20),
index in_id(id),
key in_username(username)
);

-- 创建唯一索引 --
create table test10(
id tinyint unsigned auto_increment key,
username varchar(20) not null unique,
card char(18) not null,
unique key uni_card(card)
);

-- 创建全文索引 --
create table test11(
id tinyint unsigned auto_increment key,
username varchar(20) not null unique,
userDesc varchar(20) not null,
fulltext index full_userDesc(userDesc)
);

-- 创建单列索引 --
create table test12(
id tinyint unsigned auto_increment key,
test1 varchar(20) not null,
test2 varchar(20) not null,
test3 varchar(20) not null,
test4 varchar(20) not null,
test5 varchar(20) not null,
index mul_t1_t2_t3(test1,test2,test3)
);



