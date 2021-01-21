from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    desc="""
    Creative and innovative Developer with substantial experience independently and
    collaboratively building lean and efficient applications. Hands-on approach to development,
    testing, and deployment, with a talent for adapting to new ecosystems and toolkits.
    """
    techs=['Python Develpement: Flask, Django, Pandas, Bokeh',
           'Ticketing Sytems: ServiceNow, ZenDesk',
           'System Administration: Debian, Ubuntu, CentOS, Arch, etc.',
           'Containers: Docker, Podman',
           'Databases: MySQL, MS SQL Server, MariaDB',
           'Cloud Services: AWS EC2, Linode, AWS Lambda',
           'JavaScript ES6: Chrome Extension Development',]
    return render_template('index.html',txt=desc,techs=techs)

@app.route('/demos')
def demos():
    return render_template('demos.html')
