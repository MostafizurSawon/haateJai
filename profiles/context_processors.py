from .models import UserAccount, UserSocialAccount, Cart
# from Tasks.models import Task
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
import random

def user_data(request):
    if request.user.is_authenticated:
        try:
            # Fetch or create UserAccount
            user_account, created = UserAccount.objects.get_or_create(
                user=request.user,
                defaults={
                    'image': random.choice(UserAccount.images),  # Set default image if created
                    'hometown': 'Dhaka',  # Provide any other required default values here
                }
            )

            # Fetch or create UserSocialAccount
            user_social_account, created = UserSocialAccount.objects.get_or_create(
                user=request.user
            )
            
            cart, created = Cart.objects.get_or_create(
                user=user_account
            )
            cart_items = cart.products.all()
            total_price = sum(product.price for product in cart_items)
            # print(total_price)
            
            # print(cart.created_at)
            # Add these objects to the context so they can be used in templates
            return {
                'data': user_account,
                'user_social_account': user_social_account,
                'cart': cart,
                'total': total_price,
            }

        except (UserAccount.DoesNotExist, UserSocialAccount.DoesNotExist, Cart.DoesNotExist):
            # If any of the objects don't exist or creation fails, return an empty context
            return {}

        except IntegrityError:
            # Handle any IntegrityErrors (like if duplicate entries are attempted)
            return {}

    # Return empty context if the user is not authenticated
    return {}
