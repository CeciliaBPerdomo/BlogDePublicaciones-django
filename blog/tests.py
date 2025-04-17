from django.test import TestCase
from django.urls import reverse_lazy
from blog.models import Post, Avatar, User
from blog.views import PostCreateView, PostUpdateView, DeletePostView

# Create your tests here.
class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(titulo='Test Post', contenido='Test Content', autor=self.user)

class PostCreateViewTests(TestCase):
    def test_success_url(self):
        url = reverse_lazy('blog:post_list')
        self.assertEqual(PostCreateView.success_url, url)  # Asegúrate de que la URL sea correcta