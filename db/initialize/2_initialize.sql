CREATE TABLE IF NOT EXISTS users (
    title VARCHAR(255) NOT NULL,
    description TEXT,
    user_id INT NOT NULL,
    PRIMARY KEY (user_id)
)  ENGINE=INNODB;

