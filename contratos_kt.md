# Contratos Back-Front HU S2

## => CRUDs users

## 1. ListarUsers

### URL:

```
/users
```

### METHOD:

#### GET

### PARAMS:

```
?user_email=int
````

el param de user_email no es obligatorio y sirve para devolver el detalle del customer

### BODY:

```
null
````

### RESPONSE:

```
{
    count: int,
    next: http://next.page,
    previous: null,
    results:
        [
            {
                name: string,
                username: string,
                email: string,
                is_active: boolean,
                is_superuser: boolean,
                is_staff: boolean
            },
            {
                name: string,
                username: string,
                email: string,
                is_active: boolean,
                is_superuser: boolean,
                is_staff: boolean
            },
            {
                name: string,
                username: string,
                email: string,
                is_active: boolean,
                is_superuser: boolean,
                is_staff: boolean
            },
            …
        ]
}
```

La respuesta es páginada teniendo como carga útil el array results.

## 2. Info me

### URL:

```
/users/me
```

### METHOD:

#### GET

### PARAMS:

```
null
````

### BODY:

```
null
````

### RESPONSE:

```
{
    name: string,
    username: string,
    email: string,
    is_active: boolean,
    is_superuser: boolean,
    is_staff: boolean,
    tools: [
        {
            title: string,
            description: string,
            url: string,
            image: string,
        }
    ]
    
}
```

La respuesta es páginada teniendo como carga útil el array results.
