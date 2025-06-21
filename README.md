# MariaDB MaxScale Docker Project

## Overview

This project demonstrates how to use **MariaDB MaxScale**, **Docker**, and **Docker Compose** to create a sharded database environment with two MariaDB servers and a MaxScale router. A Python script is included to connect to MaxScale, query data from the shards, and print the results.

---

## Project Structure (Everything inside `maxscale/` folder under `maxscale-docker/`)

```
maxscale-docker/
└── maxscale/
    ├── sql/
    │   ├── master1/
    │   │   └── shard1.sql      # Initialization script for master1
    │   └── master2/
    │       └── shard2.sql      # Initialization script for master2
    │
    ├── maxscale.cnf.d/
    │   └── example.cnf         # MaxScale configuration
    │
    ├── app.py                  # Python script to connect and query MaxScale
    ├── docker-compose.yml      # Docker Compose configuration file
    └── README.md
```

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

Make sure your shard files are in:

```
sql/master1/shard1.sql
sql/master2/shard2.sql
```

### 2. Start the Cluster

```bash
docker compose down -v && docker compose up -d
```

### 3. Verify the Setup

Check running containers:

```bash
docker ps
```

Check MaxScale status:

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

Run the script to query MaxScale:

```bash
python3 app.py
```

Sample output:

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

Check container logs for issues:

```bash
docker-compose logs master1
docker-compose logs master2
docker-compose logs maxscale
```

---

## Final Notes

- Ensure your `sql/master1` and `sql/master2` folders contain valid `.sql` initialization files.
- MaxScale configuration must match your server and environment.
- The Python script assumes the user `maxuser` and database `all_zipcodes` are properly configured.

---

## License

[MIT License](LICENSE)

---

## Author

Your Name - [Fariiso](https://github.com/Fariiso)
