from storages.backends.s3boto3 import S3Boto3Storage
# from filebrowser_safe.storage import S3BotoStorageMixin
from filebrowser.storage import S3BotoStorageMixin,StorageMixin
import posixpath

class S3Storage(StorageMixin, S3Boto3Storage):
    """Integration between filebrowser and S3 storage."""

    def isdir(self, name):
        if not name:
            # empty name is root dir
            return True

        return name.endswith("/")

    def isfile(self, name):
        return self.exists(name)

    def move(self, old_file_name, new_file_name, allow_overwrite=False):
        raise NotImplementedError()

    def makedirs(self, name):
        raise NotImplementedError("can't create directories")

    def rmtree(self, name):
        raise NotImplementedError("can't remote directory")

    def setpermission(self, name):
        pass

    def path(self, name):
        # needed for upload view
        return posixpath.join("/", name)

