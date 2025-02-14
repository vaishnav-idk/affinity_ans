/* 
Question 1
asked to find the number of number of tigers part of the taxonomy database
 */

 select * from taxonomy where species like 'Panthera tigris%';

 /* hint was to use scientific name of tigers however directly using the name showed an empty set because of the subspieces labled using baracket used like pattern match*/

 --to get count of the number of rows we use count aggregate function

 select count(*) from taxonomy where species like 'Panthera tigris%'

 /*answer was 8
 +----------+
| count(*) |
+----------+
|        8 |
+----------+
*/

/* Question 2 
what is the ncb_id of the Sumatran tiger
*/
--the scientfic names was found from earlie select query 
mysql> select ncbi_id,species from taxonomy where species like '%Panthera tigris sumatrae%';
/*
+---------+-------------------------------------------+
| ncbi_id | species                                   |
+---------+-------------------------------------------+
|    9695 | Panthera tigris sumatrae (Sumatran tiger) |
+---------+-------------------------------------------+
1 row in set (0.65 sec)
*/


/* 
Question 3
 Find all the columns that can be used to connect the tables in the given database.

 Answer: * rafam_acc and clan_acc connected via clan membership table
		* rfam_acc and rfamseq_acc connected via full full region table
		* ncbi_id in both rframdseq and taxonomy tables

 */
