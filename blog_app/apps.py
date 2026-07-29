from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    name = 'blog_app'
    
    def ready(self):                    # to load the signals
        import blog_app.signals
