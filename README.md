# MariaDB MaxScale Docker Project

## Overview

This project demonstrates how to use **MariaDB MaxScale**, **Docker**, and **Docker Compose** to create a sharded database environment with two MariaDB servers and a MaxScale router. A Python script is included to connect to MaxScale, query data from the shards, and print the results.

---

## Project Structure

```
maxscale-docker/
│
├── maxscale/
│   ├── sql/
│   │   ├── master1/
│   │   │   └── shard1.sql      # Initialization script for master1
│   │   └── master2/
│   │       └── shard2.sql      # Initialization script for master2
│   │
│   ├── maxscale.cnf.d/
│   │   └── example.cnf         # MaxScale configuration
│   │
│   ├── app.py                  # Python script to connect and query MaxScale
│   ├── docker-compose.yml      # Docker Compose configuration
│   ├── Dockerfile
│   └── README.md
```

> 💡 **Note:** This layout allows for easy organization of all MaxScale-related services inside the `maxscale` directory, making it cleaner for multi-project repositories.

---

## Requirements

Install the following software on your Ubuntu-based environment:

- Python 3
- Docker
- Docker Compose
- MariaDB Client (optional for manual testing)
- MySQL Connector for Python:
  ```bash
  sudo apt install mysql-connector-python
  ```

---

## Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/maxscale-docker.git
cd maxscale-docker/maxscale
```

Ensure your shard files exist at:

```
sql/master1/shard1.sql
sql/master2/shard2.sql
```

### 2. Start the Cluster

```bash
docker compose down -v && docker compose up -d
```

### 3. Verify the Setup

Check that all containers are running:

```bash
docker ps
```

Check MaxScale's routing:

```bash
docker exec -it maxscale-maxscale-1 maxctrl list servers
```

Expected output:

```
┌─────────┬─────────┬──────┬─────────────┬──────────────────┬──────┬─────────────────┐
│ Server  │ Address │ Port │ Connections │ State            │ GTID │ Monitor         │
├─────────┼─────────┼──────┼─────────────┼──────────────────┼──────┼─────────────────┤
│ server1 │ master1 │ 3306 │ 0           │ Master, Running  │      │ MariaDBdMonitor │
│ server2 │ master2 │ 3306 │ 0           │ Master, Running  │      │ MariaDBdMonitor │
└─────────┴─────────┴──────┴─────────────┴──────────────────┴──────┴─────────────────┘
```

---

## Using the Python Script

Run the following:

```bash
python3 app.py
```

This connects to MaxScale and executes queries from both shards.

---

## Docker Compose Configuration

```yaml
version: '2'
services:
  master1:
    image: mariadb:10.3
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: 'Y'
    volumes:
      - ./sql/master1:/docker-entrypoint-initdb.d
    command: mysqld --log-bin=mariadb-bin --binlog-format=ROW --server-id=3000
    ports:
      - "4001:3306"

  master2:
    image: mariadb:10.3
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: 'Y'
    volumes:
      - ./sql/master2:/docker-entrypoint-initdb.d
    command: mysqld --log-bin=mariadb-bin --binlog-format=ROW --server-id=3001
    ports:
      - "4002:3306"

  maxscale:
    image: mariadb/maxscale:latest
    depends_on:
      - master1
      - master2
    volumes:
      - ./maxscale.cnf.d:/etc/maxscale.cnf.d
    ports:
      - "4006:4006"
      - "4008:4008"
      - "8989:8989"
      - "4000:4000"
```

---

## Example Output

Sample output from running the Python script:

```
310512823
414603701
78000331
27252433
13272241
162927074
641553264
11794999
```

---

## Troubleshooting

To debug container logs:

```bash
docker-compose logs master1
docker-compose logs master2
docker-compose logs maxscale
```

---

## Final Notes

- Ensure your `sql/master1` and `sql/master2` folders contain valid `.sql` files.
- MaxScale configuration must match your actual server setup.
- Python script assumes `maxuser` and the `all_zipcodes` database are correctly configured.

---

## License

[MIT License](LICENSE)

---

## Author

Your Name - [Fariiso](https://github.com/Fariiso)

