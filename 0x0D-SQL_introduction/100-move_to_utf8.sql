-- convert to utf-8
USE `hbtn_0c_0`
ALTER TABLE `first_table`
MODIFY name TEXT
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;