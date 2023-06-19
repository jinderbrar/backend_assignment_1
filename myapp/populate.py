
from django.utils import timezone
from myapp.models import Contact

# Generate sample data
sample_data = [
    {
        'email': 'lorraine@hillvalley.edu',
        'phone_number': '123456',
        'link_precedence': 'primary',
        'linked_id': None,
    },
    {
        'email': 'mcfly@hillvalley.edu',
        'phone_number': '123456',
        'link_precedence': 'secondary',
        'linked_id': None,  # Will link to above one while populating
    },
    {
        'email': 'george@hillvalley.edu',
        'phone_number': '919191',
        'link_precedence': 'primary',
        'linked_id': None,
    },
    {
        'email': 'biffsucks@hillvalley.edu',
        'phone_number': '717171',
        'link_precedence': 'secondary',
        'linked_id': None,  # Will link to above one while populating
    },
]



def load_sample_data(): 
    # load sample data
    if Contact.objects.count() == 0:
        obj_ids = []
        for idx, data in enumerate(sample_data):
            if idx%2 ==1:
                data['linked_id'] = Contact.objects.get(id = obj_ids[-1])
            obj = Contact(
                email=data['email'],
                phone_number=data['phone_number'],
                link_precedence=data['link_precedence'],
                linked_id=data['linked_id'],
                created_at=timezone.now(),
                updated_at=timezone.now(),
            )
            obj.save()
            obj_ids.append(obj.id)
        