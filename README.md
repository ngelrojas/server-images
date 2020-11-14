### server images

- chmod +x app/entrypoint.sh
- chmod +x app/entrypoint.prod.sh

### run development environment
```python 
    docker-compose up -d --build
 ```

### run production envronment
```python
    docker-compose -f docker-compose.prod.yml up -d --build
``` 
