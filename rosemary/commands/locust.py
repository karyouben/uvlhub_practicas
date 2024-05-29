import os
import subprocess
import click

@click.command('locust', help="Launches Locust for load testing based on the environment.")
def locust():

    base_dir = os.path.abspath(os.path.dirname(__file__))
    working_dir = os.getenv('WORKING_DIR', '')
    app_dir = os.path.join(working_dir, 'app/')
    core_dir = os.path.join(working_dir, 'core/')

    if working_dir in ['/app', '/app/']:

        click.echo("You are in a Docker environment!")

        click.echo("To use locust in a Docker environment, run the following command on your machine's host:")
        click.echo("\n\tdocker compose -f docker/docker-compose.dev.yml up locust -d\n")

        pass

    elif working_dir == '':
        click.echo("Starting Locust in local environment on port 8089...")
       
        locustfile_path = f'{core_dir}bootstraps/locustfile_bootstrap.py'
        subprocess.run(['locust', '-f', locustfile_path])  

    elif working_dir == '/vagrant/':
        click.echo("Starting Locust in Vagrant environment on port 8089...")
        subprocess.run(['vagrant', 'ssh', '--command', f'locust -f /vagrant/app/locustfile.py --headless -u 10 -r 1 --host=http://localhost:8990'])
    else:
        click.echo(click.style(f"Unrecognized WORKING_DIR: {working_dir}", fg='red'))