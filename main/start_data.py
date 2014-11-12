start_data = """
BEGIN;
CREATE TABLE `table1` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `field1` integer NOT NULL,
    `field2` varchar(255) NOT NULL,
    `date` datetime NOT NULL
);
CREATE TABLE `table2` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `field3` integer NOT NULL,
    `field4` varchar(255) NOT NULL,
    `date` datetime NOT NULL
);
CREATE TABLE `table3` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `table1_id` integer NOT NULL,
    `table2_id` integer NOT NULL,
    `field5` varchar(255) NOT NULL
);
ALTER TABLE `table3` ADD CONSTRAINT `table1_table3` FOREIGN KEY (`table1_id`) REFERENCES `table1` (`id`);
ALTER TABLE `table3` ADD CONSTRAINT `table2_table3` FOREIGN KEY (`table2_id`) REFERENCES `table2` (`id`);
COMMIT;
"""
