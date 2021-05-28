from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.renderers import JSONRenderer


# Create your views here.

from .models import Position, Cart, CartPosition, Promocode

class GetPositions(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        show_sale = request.GET.get('show_sale')
        category = request.GET.get('category')
        if show_sale is None or category is None:
            return Response(
                {
                    'result': 'error', 
                    'error': '{}{} is required'.format(
                        'show_sale' if show_sale is None else '',
                        ', category' if category is None else ''
                    )
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        positions = False
        if show_sale == "1":
            positions = Position.objects.filter(category=category, sale_price__isnull=False)
        else:
            positions = Position.objects.filter(category=category, sale_price=None)

        positions_list = [position.to_dict() for position in positions]

        return Response(positions_list)

class GetCart(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (JSONRenderer,)
    
    def get(self, request):
        _id = request.session.get('id')
        cart = None

        if _id is None:
            cart = Cart()
            cart.save()
            request.session['id'] = cart.id
        else:
            cart = Cart.objects.get(id=_id)
        
        json_cart = [item.to_dict() for item in cart.cartposition_set.all()]
        return Response(json_cart)

class AddToCart(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (JSONRenderer,)
    
    def post(self, request):
        _id = request.session.get('id')
        
        position_id = request.data.get('id')
        amount = request.data.get('amount')
        if position_id is None or amount is None:
            return Response(
                {
                    'result': 'error', 
                    'error': '{}{} is required'.format(
                        'position_id' if position_id is None else '',
                        ', amount' if amount is None else ''
                    )
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        cart = None
        if _id is None:
            cart = Cart()
            request.session['id'] = cart.id
        else:
            cart = Cart.objects.get(id=_id)
        
        position_exists = False
        for cart_position in cart.cartposition_set.all():
            if cart_position.position.id == position_id:
                position_exists = True
                cart_position.amount += amount
                cart_position.save()

        position = Position.objects.get(id=position_id)
        if not position_exists:
            cart_position=CartPosition(amount = amount, position=position)
            cart_position.save()
            cart.cartposition_set.add(cart_position)
        
        cart.save()

        return Response({'status': 'ok'})


class SetPositionAmount(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (JSONRenderer,)
    
    def post(self, request):
        _id = request.session.get('id')
        position_id = request.data.get('position_id')
        amount = request.data.get('amount')

        if position_id is None or amount is None:
            return Response(
                {
                    'result': 'error', 
                    'error': '{}{} is required'.format(
                        'position_id' if position_id is None else '',
                        ', amount' if amount is None else ''
                    )
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        cart = Cart.objects.get(id=_id)
        cartposition = cart.cartposition_set.get(position_id=position_id)
        cartposition.amount = amount
        cartposition.save()
        cart.save()

        return Response({'status': 'ok'})


class RemoveFromCart(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (JSONRenderer,)
    
    def post(self, request):
        _id = request.session.get('id')
        position_id = request.data.get('position_id')
        if position_id is None:
            return Response(
                {
                    'result': 'error', 
                    'error': 'position_id is required'.format(position_id)
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        cart = Cart.objects.get(id=_id)
        cart.cartposition_set.get(position_id=position_id).delete()
        cart.save()

        return Response({'status': 'ok'})


class ValidatePromo(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (JSONRenderer,)

    def post(self, request):
        promo = request.data.get('promo')

        if promo is None:
            return Response({'promo is required'}, status=status.HTTP_400_BAD_REQUEST)

        promo_data = None
        try:
            promo_data = Promocode.objects.get(code=promo)
        except:
            return Response({'status': 'no promo'})
        
        promo_status = promo_data.validate()
        if not promo_status[0]:
            return Response({'status': promo_status[1]})
        
        return Response({'status': 'active', 'percent': promo_data.profit_percent})