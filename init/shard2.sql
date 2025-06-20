-- Create a sample database for shard2
CREATE DATABASE IF NOT EXISTS shard_db;
USE shard_db;

-- Create a sample table
CREATE TABLE IF NOT EXISTS sample_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Insert a record to indicate which shard this is
INSERT INTO sample_table (name) VALUES ('Record from shard2');
