from whitenoise.storage import CompressedManifestStaticFilesStorage
from whitenoise.storage import MissingFileError

class IgnoreErrorsStaticFilesStorage(CompressedManifestStaticFilesStorage):
    def post_process(self, *args, **kwargs):
        try:
            # Call the default post-process method
            return super().post_process(*args, **kwargs)
        except MissingFileError as e:
            # Catch the MissingFileError and log it

            # You can return None to skip the problematic file and continue
            return None
        except Exception as e:
            # Catch any other exception and log it
            print(f"Error processing static file: {e}")
            return
