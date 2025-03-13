select sum(case when left_size <=3 then 1 else 0 end) size3,
sum(case when left_size > 3 and left_size <=4 then 1 else 0 end) size4,
sum(case when left_size > 4 and left_size <=5 then 1 else 0 end) size5,
sum(case when left_size > 5 and left_size <=6 then 1 else 0 end) size6,
sum(case when left_size > 6 and left_size <=7 then 1 else 0 end) size7,
sum(case when left_size > 7 and left_size <=8 then 1 else 0 end) size8,
sum(case when left_size > 8 and left_size <=9 then 1 else 0 end) size9,
sum(case when left_size > 9 and left_size <=10 then 1 else 0 end) size10,
sum(case when left_size > 10  then 1 else 0 end) sizegl10
 from bond_cov b 
 where b.id in(select bond_id from bond_cov_daily bd where high>140 ) 
