from django.db import transaction


def create_instance(serializer, user, additional_fields):
    with transaction.atomic():
        try:
            instance = serializer.save(created_by=user, **additional_fields)
            return {
                'response': f'{instance.__class__.__name__} created successfully!',
                f'{instance.__class__.__name__.lower()}': instance
            }
        except Exception as ex:
            return {
                'message': 'An error occurred!',
                'response': str(ex)
            }
