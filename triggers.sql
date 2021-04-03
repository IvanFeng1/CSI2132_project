create function check_stars_func()
	returns trigger as
$BODY$
BEGIN

if NEW.stars > 5 or NEW.stars < 1 then
	raise exception 'stars must be between 1 and 5 inclusive';
end if;

return new;
end
$BODY$ LANGUAGE plpgsql;

create function check_price_func()
	returns trigger as
$BODY$
BEGIN

if NEW.price <= 0 then
	raise exception 'price must be greater than 0';
end if;

return new;
end
$BODY$ LANGUAGE plpgsql;


create trigger check_star
before update on hotel
for each row 
execute procedure check_stars_func();

create trigger check_price
before update on room
for each row
execute procedure check_price_func();

select * from "Project".hotel