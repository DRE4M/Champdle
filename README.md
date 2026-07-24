# Champdle

http://yeardayhour.duckdns.org:3100/

League of Legends champion guessing game inspired by [Semantle](https://semantle.novalis.org/)

## Clone

```bash
git clone --recursive https://github.com/DRE4M/Champdle.git
```

## Start server

```bash
docker-compose -f docker-compose.prod.yml up -d # http://localhost:3100/
```

## Generate old_secret.csv

```bash
cd backend
poetry run poe export-old-secret 10
```

## Validate data

```bash
cd backend
poetry run poe validate-data
```

## Data source

champions.csv and champion icons are based on League of Legends DataDragon and CommunityDragon datasets.

# LICENSE

MIT
