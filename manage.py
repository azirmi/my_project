#!/usr/bin/env python
import os
import sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company_auth.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django is not installed. Install it with: pip install -r requirements.txt"
        ) from exc
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    main()
