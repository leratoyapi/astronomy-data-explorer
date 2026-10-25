CREATE SCHEMA `astronomy` ;

-- here is my apod table. 
CREATE TABLE `astronomy`.`apod` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data` DATE NULL,
  `title` VARCHAR(150) NULL,
  `explanation` TEXT(600) NULL,
  `url` VARCHAR(530) NULL,
  `media_type` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SELECT * FROM astronomy.apod;

ALTER TABLE `astronomy`.`apod` 
CHANGE COLUMN `data` `date` DATE NULL DEFAULT NULL ;
