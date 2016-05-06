from os.path import splitext

#from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
from django.core.files.uploadedfile import InMemoryUploadedFile
import magic

MAX_SIZE_5MB = 5*1024*1024
MAX_SIZE_10MB = 10*1024*1024

@deconstructible
class FileValidator(object):
    """
    Validator for files, checking the size, extension and mimetype.
    Initialization parameters:
        allowed_extensions: iterable with allowed file extensions
            ie. ('txt', 'doc')
        allowd_mimetypes: iterable with allowed mimetypes
            ie. ('image/png', )
        min_size: minimum number of bytes allowed
            ie. 100
        max_size: maximum number of bytes allowed
            ie. 24*1024*1024 for 24 MB
    Usage example::
        MyModel(models.Model):
            myfile = FileField(validators=FileValidator(max_size=24*1024*1024), ...)
    """

    extension_message = _("Extension '%(extension)s' not allowed. Allowed extensions are: '%(allowed_extensions)s.'")
    mime_message = _("MIME type '%(mimetype)s' is not valid. Allowed types are: %(allowed_mimetypes)s.")
    min_size_message = _('The current file %(size)s, which is too small. The minumum file size is %(allowed_size)s.')
    max_size_message = _('The current file %(size)s, which is too large. The maximum file size is %(allowed_size)s.')

    def __init__(self, *args, **kwargs):
        self.allowed_extensions = kwargs.pop('allowed_extensions', None)
        self.allowed_mimetypes = kwargs.pop('allowed_mimetypes', None)
        self.min_size = kwargs.pop('min_size', 0)
        self.max_size = kwargs.pop('max_size', None)

    def set_context(self, serializer):
        self.instance = getattr(serializer.parent, 'initial_data', None)

    def __call__(self, value):
        """
        Check the extension, content type and file size.
        """
        #print(self.instance)

        # Check the extension
        ext = splitext(value.name)[1][1:].lower()
        if self.allowed_extensions and not ext in self.allowed_extensions:
            message = self.extension_message % {
                'extension' : ext,
                'allowed_extensions': ', '.join(self.allowed_extensions)
            }

            raise serializers.ValidationError(message)

        # Check the content type
        if value.file.__class__ == InMemoryUploadedFile:
            buffer = value.file.file.getvalue()
            #  ..  as the file is already in memory, buffer length should not exhaust the system ...
        else:
            buffer = value.file.read()
            # ... but here this may become an issue ...

        mimetype = magic.from_buffer(buffer, mime=True).decode("utf-8")

        if self.allowed_mimetypes and not mimetype in self.allowed_mimetypes:
            message = self.mime_message % {
                'mimetype': mimetype,
                'allowed_mimetypes': ', '.join(self.allowed_mimetypes)
            }

            raise serializers.ValidationError(message)

        # Check the file size
        if value.file.__class__ == InMemoryUploadedFile:
            filesize = value.file._size
        else:
            filesize = value.size