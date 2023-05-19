-- top 3 cities in July and August
USE `hbtn_0c_0`;
SELECT `city`, AVG(`value`) AS avg_temp
FROM `temperatures`
WHERE `month` = 7 AND `month` = 8
GROUP BY `city`
ORDER BY avg_temp DESC
LIMIT 3;