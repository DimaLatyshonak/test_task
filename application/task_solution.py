from application.models import Producer

contract_id = 32812
producer_ids = (
    Producer.objects.filter(products__credit_application__contract__id=contract_id)
    .values_list("id", flat=True)
    .distinct()
)
