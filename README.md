# django-query-condition
Demo for using Django query condition.

## Installation
1. create a virtualenv
    ```shell
    virtualenv .venv
    ```

2. activate virtualenv
    ```shell
    . .venv/bin/activate
    ```

3. install packages
    ```shell
    make install
    ```
4. setup pre-commit
    ```shell
    pre-commit install
    ```

## Development
Update packages
```shell
make compile && make sync
```

Running tests
```shell
pytest
```
