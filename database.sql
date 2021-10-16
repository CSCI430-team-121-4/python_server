CREATE TABLE IF NOT EXISTS `user` (
    `user_id` INTEGER PRIMARY KEY AUTOINCREMENT, 
    `password` VARCHAR(255), 
    `username` VARCHAR(255) UNIQUE, 
    `createdAt` DATETIME NOT NULL, 
    `updatedAt` DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS `sessions` (
    `session_id` VARCHAR(255) NOT NULL PRIMARY KEY,
    `user_id` INTEGER NOT NULL REFERENCES `user` (`user_id`),
    `createdAt` DATETIME NOT NULL,
    `updatedAt` DATETIME NOT NULL
);