from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from Lands.models import land
from Crops.models import crop
from Inventory.models import Inventory
from Expenses.models import Expenses
from Sales.models import Sale


class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        # Get the farmer who is currently logged in
        farmer = request.user.profile.farmer

        data = {

            # Farmer
            "farmer_name": farmer.name,

            # Lands
            "lands": list(
                land.objects.filter(
                    farmer=farmer
                ).values_list(
                    "land_name",
                    flat=True
                )
            ),

            # Crops
            "crops": list(
                crop.objects.filter(
                    land__farmer=farmer
                ).values_list(
                    "crop_name",
                    flat=True
                )
            ),

            # Inventory
            "inventory": list(
                Inventory.objects.filter(
                    farmer=farmer
                ).values_list(
                    "name",
                    flat=True
                )
            ),

            # Expenses
            "expenses": list(
                Expenses.objects.filter(
                    farmer=farmer
                ).values(
                    "category",
                    "amount",
                    "date"
                )
            ),

            # Sales
            "sales": list(
                Sale.objects.filter(
                    farmer=farmer
                ).values(
                    "Crop__crop_name",
                    "quantity",
                    "price_per_unit",
                    "total_amount",
                    "sale_date",
                    "buyer"
                )
            ),
        }

        return Response(data)
