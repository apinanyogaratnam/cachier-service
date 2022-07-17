import os

from dotenv import load_dotenv

from app import create_app

load_dotenv()


def main():
    PORT = os.environ.get('PORT', 8000)

    app = create_app()
    environment = os.environ.get('ENVIRONMENT')

    debug_mode = environment.upper() == 'DEVELOPMENT'

    app.run(host='0.0.0.0', port=PORT, debug=debug_mode)


if __name__ == '__main__':
    main()
