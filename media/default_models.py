class Image(ImageBase):
    '''
        Image model that can be attached to any other Django model using
        generic relations. It is simply non-abstract subclass of
        :class:`~generic_images.models.AbstractAttachedImage`
    '''
    class Meta:
        ordering = ['-order']