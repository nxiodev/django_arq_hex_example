from api.engine.domain.entities import entities_customers as entity


def constructor_customer_entities(customer_orm) -> entity.Customer:
    return entity.Customer(
        id=customer_orm.id,
        name=customer_orm.name,
        paternal_surname=customer_orm.paternal_surname,
        email=customer_orm.email,
    )
