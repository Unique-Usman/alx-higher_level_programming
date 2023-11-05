select city, avg(value) as avg_temp from temperatures group by city order by avg_temp desc;
