echo Tearing down old Docker containers...
docker-compose rm -fs

echo Building new Docker containers...
docker-compose up --build -d