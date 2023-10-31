CREATE TABLE `Metals` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `caret` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `metal_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Sizes`(`id`)
);


INSERT INTO `Metals` VALUES (null,"Gold", 200.00);
INSERT INTO `Metals` VALUES (null,"Silver", 120.50);
INSERT INTO `Metals` VALUES (null,"Copper", 90.75);

INSERT INTO `Styles` VALUES (null,"Round", 1500.00);
INSERT INTO `Styles` VALUES (null,"Heart", 1250.50);
INSERT INTO `Styles` VALUES (null,"Pear", 1100.75);

INSERT INTO `Sizes` VALUES (null,"Small", 1000.00);
INSERT INTO `Sizes` VALUES (null,"Medium", 5000.50);
INSERT INTO `Sizes` VALUES (null,"Large", 9000.75);

-- Order 1: Gold Round Small
INSERT INTO `Orders` (`metal_id`, `style_id`, `size_id`) 
VALUES (
  (SELECT `id` FROM `Metals` WHERE `metal` = 'Gold'),
  (SELECT `id` FROM `Styles` WHERE `style` = 'Round'),
  (SELECT `id` FROM `Sizes` WHERE `caret` = 'Small')
);

-- Order 2: Silver Heart Medium
INSERT INTO `Orders` (`metal_id`, `style_id`, `size_id`) 
VALUES (
  (SELECT `id` FROM `Metals` WHERE `metal` = 'Silver'),
  (SELECT `id` FROM `Styles` WHERE `style` = 'Heart'),
  (SELECT `id` FROM `Sizes` WHERE `caret` = 'Medium')
);

-- Order 3: Copper Pear Large
INSERT INTO `Orders` (`metal_id`, `style_id`, `size_id`) 
VALUES (
  (SELECT `id` FROM `Metals` WHERE `metal` = 'Copper'),
  (SELECT `id` FROM `Styles` WHERE `style` = 'Pear'),
  (SELECT `id` FROM `Sizes` WHERE `caret` = 'Large')
);

-- Order 4: Gold Heart Large
INSERT INTO `Orders` (`metal_id`, `style_id`, `size_id`) 
VALUES (
  (SELECT `id` FROM `Metals` WHERE `metal` = 'Gold'),
  (SELECT `id` FROM `Styles` WHERE `style` = 'Heart'),
  (SELECT `id` FROM `Sizes` WHERE `caret` = 'Large')
);

-- Order 5: Silver Round Small
INSERT INTO `Orders` (`metal_id`, `style_id`, `size_id`) 
VALUES (
  (SELECT `id` FROM `Metals` WHERE `metal` = 'Silver'),
  (SELECT `id` FROM `Styles` WHERE `style` = 'Round'),
  (SELECT `id` FROM `Sizes` WHERE `caret` = 'Small')
);


SELECT m.id, m.metal, m.price FROM Metals m;
SELECT m.id, m.metal, m.price FROM Metals m WHERE m.id = 2;
SELECT o.id, o.metal_id, o.style_id, o.size_id FROM Orders o;

SELECT Orders.id, Metals.metal, Styles.style, Sizes.caret
FROM Orders
JOIN Metals ON Orders.metal_id = Metals.id
JOIN Styles ON Orders.style_id = Styles.id
JOIN Sizes ON Orders.size_id = Sizes.id;

  SELECT Orders.id, Orders.metal_id, Orders.style_id, Orders.size_id, Metals.id AS metal_id, Metals.metal, Metals.price
    FROM Orders
    JOIN Metals ON Orders.metal_id = Metals.id
    WHERE Orders.id = 1;