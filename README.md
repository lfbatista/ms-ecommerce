# ms-ecommerce

### Setting up admin:
```sh
cd /admin
docker-compose up --build --remove-orphans
```

In another console:
```sh
cd /admin
docker-compose exec backend sh
python manage.py makemigrations
python manage.py migrate
```

### Setting up main:
```sh
cd /admin
docker-compose up --build --remove-orphans
```

In another console:
```sh
cd /admin
docker-compose exec backend sh
python manager.py db upgrade
python manager.py db migrate
```

#### Notes:
After the build, you might have to restart the service using `sudo` or change `/.dbdata/` permissions:
```sh
sudo docker-compose up
```

Add some entries to the `products_user` table:
```sql
insert into products_user (id) values (1);
insert into products_user (id) values (2);
insert into products_user (id) values (3);
commit;
```
