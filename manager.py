from autotest import app

from autotest.env import env_view
from autotest.home import home_views
from autotest.interface import if_view
from autotest.login import login_views
from autotest.task import task_views

app.register_blueprint(if_view)
app.register_blueprint(env_view)
app.register_blueprint(login_views)
app.register_blueprint(home_views)
app.register_blueprint(task_views)


if __name__ == '__main__':
    app.run(debug=True,port=8784)
