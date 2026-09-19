from contact.models import ContactMessage
from gallery.models import GalleryImage
from videos.models import Video


def admin_dashboard_counts(request):

    if request.path.startswith('/admin/'):
        return {
            'contact_count': ContactMessage.objects.count(),
            'gallery_count': GalleryImage.objects.count(),
            'video_count': Video.objects.count(),
        }

    return {}