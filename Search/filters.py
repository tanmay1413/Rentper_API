import django_filters # type: ignore
from hotels.models import Hotel,Room
from Bookings.models import Booking
from django.db.models import Q

class HotelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    city = django_filters.CharFilter(field_name='address__city', lookup_expr='exact')
    state = django_filters.CharFilter(field_name='address__state', lookup_expr='exact')
    check_in_date = django_filters.DateFilter(method='filter_by_availability')
    check_out_date = django_filters.DateFilter(method='filter_by_availability')
    guest = django_filters.NumberFilter(field_name='room__occupancy_limit', lookup_expr='gte')

    class Meta:
        model = Hotel
        fields = ['name', 'city', 'state', 'check_in_date', 'check_out_date', 'guest']

    def filter_by_availability(self, queryset, name, value):
        check_in_date = self.data.get('check_in_date')
        check_out_date = self.data.get('check_out_date')

        if check_in_date and check_out_date:
            overlapping_booking = Booking.objects.filter(
                Q(check_in_date__lt=check_out_date) & Q(check_out_date__gt=check_in_date)
            ).values_list('room__hotel', flat=True)

            return queryset.exclude(id__in=overlapping_booking)

        return queryset


class RoomFilter(django_filters.FilterSet):
    room_type = django_filters.CharFilter(field_name='room_type', lookup_expr='iexact')
    class Meta:
        model=Room
        fields=['room_type']