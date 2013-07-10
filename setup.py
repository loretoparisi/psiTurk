from setuptools import setup

setup(
    name = "PsiTurk",
    version = "1.0a1",
    packages = ["psiturk"],
    include_package_data = True,
    zip_safe = False,
    entry_points = {
        'console_scripts': [
            'psiturk = psiturk.dashboard_server:launch',
            'psiturk-dashboard = psiturk.dashboard_server:launch',
            'psiturk-server = psiturk.psiturk_server:launch'
        ]
    },
    setup_requires = [],
    install_requires = ["Flask", "boto>=2.9", "SQLAlchemy", "gevent", "gevent-socketio", "gunicorn", "iso8601"],
    extras_require = {},
    author = "NYU Computation and Cognition Lab",
    author_email = "http://nyuccl.org",
    description = "A web framework for dynamic behavioral experiments",
    url = "http://github.com/NYUCCL/psiturk"
)
