from compartidos.exceptions import ExceptionBase


class CustomerDoesNotExist(ExceptionBase):
    """Customer does not exist"""
    message = "Customer {customer_id} does not exist"

    def __init__(self, customer_id: int):
        self.message.format(customer_id=customer_id)
