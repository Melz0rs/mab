CREATE TABLE IF NOT EXISTS notifications (
    title VARCHAR(255) NOT NULL,
    description TEXT,
    notification_id INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (notification_id)
)  ENGINE=INNODB;

