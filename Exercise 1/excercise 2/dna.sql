/* 
Question 1
asked to find the number of number of tigers part of the taxonomy database
 */

 select * from taxonomy where species like '%Panthera tigris%';

 /* hint was to use scientific name of tigers however directly using the name showed an empty set because of the subspieces labled using baracket used like pattern match*/

 --to get count of the number of rows we use count aggregate function

 select count(*) from taxonomy where species like '%Panthera tigris%'

 /*answer was 8
 +----------+
| count(*) |
+----------+
|        8 |
+----------+
*/

