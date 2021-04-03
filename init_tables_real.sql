set search_path = "Project"
select * from hotel_brand
delete from hotel_brand where brand = 'joe'
insert into hotel_brand (brand,main_office_location,phone_num) values ('joe',(394,'Red Street', 'Berlin', 'Manitoba', 'Canada'),'132412')
create table hotel_brand(brand varchar(20) primary key , main_office_location address, 
						phone_num varchar(20), num_of_hotels int default 0);
drop table hotel_brand
create table brand_to_hotel(hotelID varchar(20),brand_name varchar(40));
select * from brand_to_hotel
drop table hotel;
drop table brand_to_hotel;
drop table hotel_brand;
select * from hotel
create table hotel(hotelID varchar(20) primary key,stars int, num_of_rooms int, hotel_address address, 
				  contact_email varchar(40), phone_num varchar(20),
				  constraint star_check check (stars >= 1 and stars <= 5),
				  constraint room_num_check check (num_of_rooms > 0));

create table emp_to_hotel(hotelID varchar(20),employee_sin varchar(20));

create table works_under(manager_SIN varchar(20),employee_sin varchar(20));

create table employee(employee_sin varchar(20) primary key, first_name varchar(13),last_name varchar(13),
					 home_address address);
drop table room 
create table room(room_num varchar(15) primary key, is_booked bool,price numeric(7,2),has_tv bool, has_ac bool,
				 room_cap int, room_view varchar(15), can_extend bool,
				 constraint price_check check(price > 0.00));

create table hotel_to_room(room_num varchar(15),hotelID varchar(20));

create table booking(room_num varchar(15),check_in_date date, stay_duration_days int,
					num_ppl int, occupant varchar(15), constraint booking_fkey
					foreign key(room_num) references room(room_num),
					constraint stay_duration_check check (stay_duration_days > 0),
					constraint num_ppl_check check (num_ppl > 0));

create table renting(room_num varchar(15),check_in_date date, stay_duration_days int,
					num_ppl int, occupant varchar(15), constraint booking_fkey
					foreign key(room_num) references room(room_num),
					constraint stay_duration_check check (stay_duration_days > 0),
					constraint num_ppl_check check (num_ppl > 0));
create table customer (sin varchar(15) primary key,first_name varchar(13),last_name varchar(13), 
					  customer_address address, registration_date date);
create type address as (
	street_num int,
	street char(40),
	city char(30),
	province char(30),
	country char(19)
);

