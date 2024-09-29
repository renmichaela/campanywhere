from django.contrib import admin
from django.contrib.auth.models import User
from expenses.models import Attendee, Expense, Payment, Reimbursement
from django.urls import include, path
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amount', 'date']

class ReimbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement
        fields = ['amount', 'date']

class AttendeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    payments = PaymentSerializer(many=True)
    reimbursements = ReimbursementSerializer(many=True)

    class Meta:
        model = Attendee
        fields = [
            'year',
            'user',
            'days_attending',
            'camping_type',
            'festival_virgin',
            'camping_expense_share_weight',
            'electric_expense_share_weight',
            'share_of_camping_expenses',
            'share_of_paid_camping_expenses',
            'share_of_electric_expenses',
            'share_of_paid_electric_expenses',
            'running_total_owed',
            'projected_total_owed',
            'group_costs_paid',
            'total_payments_made',
            'outstanding_balance',
            'total_reimbursed',
            'payments',
            'reimbursements'
        ]

class ExpenseSerializer(serializers.ModelSerializer):
    paid_by = AttendeeSerializer()
    class Meta:
        model = Expense
        fields = ['id', 'name', 'type', 'amount', 'date', 'description', 'paid_by', 'type_label']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'expenses', ExpenseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]