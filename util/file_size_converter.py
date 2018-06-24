
class FileSizeConverter:

    @staticmethod
    def convert_size(self, file_size):
        if file_size.lower().endswith('gb'):
            value = int(file_size[-2])
            return value * 1024 * 1024 * 1024
        elif file_size.lower().endswith('mb'):
            value = int(file_size[-2])
            return value * 1024 * 1024
            pass
        elif file_size.lower().endswith('kb'):
            value = int(file_size[-2])
            return value * 1024
            pass
        elif file_size.lower().endswith('b'):
            value = int(file_size[-1])
            return value
        else:
            raise ValueError('Conversion not supported for: {0}'.format(file_size))

