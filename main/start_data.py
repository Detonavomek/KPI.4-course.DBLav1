start_data = """
BEGIN;
CREATE TABLE `Laba1_account` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `amount` integer NOT NULL,
    `manager` varchar(50) NOT NULL,
    `dateCreating` datetime NOT NULL
)
;
CREATE TABLE `Laba1_pet` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(15) NOT NULL,
    `age` integer NOT NULL,
    `specie` varchar(15) NOT NULL
)
;
CREATE TABLE `Laba1_job` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(20) NOT NULL,
    `salary` integer NOT NULL
)
;
CREATE TABLE `Laba1_human` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `account_id` integer NOT NULL,
    `job_id` integer NOT NULL,
    `pet_id` integer NOT NULL,
    `name` varchar(20) NOT NULL,
    `age` integer NOT NULL
)
;
ALTER TABLE `Laba1_human` ADD CONSTRAINT `job_id_refs_id_9de64e76` FOREIGN KEY (`job_id`) REFERENCES `Laba1_job` (`id`);
ALTER TABLE `Laba1_human` ADD CONSTRAINT `pet_id_refs_id_31157d61` FOREIGN KEY (`pet_id`) REFERENCES `Laba1_pet` (`id`);
ALTER TABLE `Laba1_human` ADD CONSTRAINT `account_id_refs_id_55363b5c` FOREIGN KEY (`account_id`) REFERENCES `Laba1_account` (`id`);
INSERT INTO Laba1_job VALUES(111, 'qwerty', 123);
COMMIT;
"""