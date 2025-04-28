import os
import io
import math
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def bookings_chart(request):
    # Sample data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    active = [100, 800, 500, 700, 800, 900, 1000, 800, 700, 800, 800, 900]
    cancelled = [500, 250, 150, 170, 170, 290, 50, 100, 200, 150, 30, 60]

    active_scaled = [a/100 for a in active]
    cancelled_scaled = [c/100 for c in cancelled]

    x = range(len(months))

    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar charts
    ax.bar(x, active_scaled, color='blue', label='Active Booking' ,zorder=2)
    ax.bar(x, cancelled_scaled, bottom=active_scaled, color='lavender', label='Cancelled Bookings',zorder=2)

    # Bar labels
    for i in range(len(x)):
        ax.text(i, active_scaled[i] / 2 , str(active[i]), ha='center', color='white', fontweight='bold', fontsize=8)
        ax.text(i, active_scaled[i] + cancelled_scaled[i] / 2, str(cancelled[i]), ha='center', color='black', fontsize=8)


   # After bar plotting
    max_y = max([a + c for a, c in zip(active_scaled, cancelled_scaled)])
    max_y_rounded = math.ceil(max_y)

    for y_value in range(2, max_y_rounded + 2, 2):
        ax.axhline(y=y_value, color='grey', linestyle='-', linewidth=1, zorder=1)


    # Labels and styles
    ax.set_xticks(x)
    ax.set_xticklabels(months)
    ax.set_ylabel('Bookings (in hundreds)')
    ax.set_xlabel('Months')
    ax.set_title(
    "Bookings’ Insight",
    loc='left',
    fontsize=18,
    color='#484848',
    pad=20
)

    ax.legend(
    loc='upper right',  
    bbox_to_anchor=(1, 1.05),
    ncol=2,              
    fontsize=10,
    frameon=False
)



    # Remove top and right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Output image to buffer
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    # Save the image to the media folder
    image_name = 'bookings_chart.png'
    image_path = os.path.join(settings.MEDIA_ROOT, 'chart', image_name)


    with open(image_path, 'wb') as f:
        f.write(buf.read())

    # Return the image URL
    image_url = f"{settings.MEDIA_URL}chart/{image_name}"

    return JsonResponse({'image_url': image_url})

