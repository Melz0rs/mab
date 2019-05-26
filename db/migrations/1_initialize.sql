CREATE TABLE IF NOT EXISTS notifications (
    notification_id INT NOT NULL
    user_id INT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    PRIMARY KEY (notification_id)
)  ENGINE=INNODB;