from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Service'

    def __str__(self):
        return self.name

    # Function to create a new service
    def create_service(name):
        try:
            service = Service.objects.create(name=name)
            service.save()
            return service
        except Exception as e:
            # Handle any errors during creation (e.g., database errors)
            print(f"Error creating service: {e}")
            return None
    
    # Function to retrieve all services
    def get_all_services():
        services = Service.objects.all()
        return services
    
    # Function to update a service
    def update_service(service_id, new_name):
        try:
            service = Service.objects.get(pk=service_id)
            service.name = new_name
            service.save()
            return service
        except Service.DoesNotExist:
            # Handle the case where the service ID doesn't exist
            print(f"Service with ID {service_id} not found")
            return None
        
        # Function to delete a service
    def delete_service(service_id):
        try:
            service = Service.objects.get(pk=service_id)
            service.delete()
            return True
        except Service.DoesNotExist:
            # Handle the case where the service ID doesn't exist
            print(f"Service with ID {service_id} not found")
            return False



