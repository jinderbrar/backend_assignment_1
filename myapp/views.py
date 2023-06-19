from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Contact

@csrf_exempt  # Disable CSRF protection for simplicity.
def identify_customer(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        phone_number = data.get('phoneNumber')

        if email or phone_number:
            # Check if a primary contact exists
			# for given email and phone number
            primary_contact = Contact.objects.filter(Q(email=email) | Q(phone_number=phone_number), link_precedence='primary').first()

			# if primary contact is there, then fetch secondary contacts linked to it
            if primary_contact:
                primary_contact_info = {
                    'primaryContactId': primary_contact.id,
                    'emails': [primary_contact.email],
                    'phoneNumbers': [primary_contact.phone_number],
                    'secondaryContactIds': []
                }

                # Find secondary contacts linked to the primary contact
                secondary_contacts = Contact.objects.filter(linked_id=primary_contact.id)

                for secondary_contact in secondary_contacts:
                    primary_contact_info['emails'].append(secondary_contact.email)
                    primary_contact_info['phoneNumbers'].append(secondary_contact.phone_number)
                    primary_contact_info['secondaryContactIds'].append(secondary_contact.id)

                response = {
                    'contact': primary_contact_info
                }

                return JsonResponse(response, status=200)
            else:
                # In case primary contanct do not exis
				# create a new primary contact
                new_primary_contact = Contact.objects.create(email=email, phone_number=phone_number, link_precedence='primary')

                response = {
                    'contact': {
                        'primaryContactId': new_primary_contact.id,
                        'emails': [new_primary_contact.email],
                        'phoneNumbers': [new_primary_contact.phone_number],
                        'secondaryContactIds': []
                    }
                }

                return JsonResponse(response, status=200)
        else:
            response = {
                'error': 'No email or phone number provided.'
            }

            return JsonResponse(response, status=400)

    response = {
        'error': 'Invalid request method.'
    }

    return JsonResponse(response, status=405)
