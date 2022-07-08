import os

from app import create_app


def main():
    PORT = os.environ.get('PORT', 8000)

    app = create_app()
    app.run(host='0.0.0.0', port=PORT)


if __name__ == '__main__':
    main()
