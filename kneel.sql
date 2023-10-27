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

SELECT m.id, m.metal, m.price FROM Metals m;
SELECT m.id, m.metal, m.price FROM Metals m WHERE m.id = 2;