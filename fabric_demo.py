# -*-encoding:utf8-*-
import os

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.network import ssh

env.use_ssh_config = True
env.user = 'shiqi.duan'
env.hosts = ['l-df3.vc.cn6']
ssh.util.log_to_file("paramiko.log", 10)

deploy_dir = '/home/q/www/'
project_name = 'sight_manager'
code_dir = '%s%s' % (deploy_dir, project_name)

DEV_PROFILES_FLAG = "dev"
BETA_PROFILES_FLAG = "beta"
PROD_PROFILES_FLAG = "prod"

# 按照flag来设置生产环境和开发环境的host及路径设置
@task(alias='dnr')
def deploy_and_restart(flag=DEV_PROFILES_FLAG):
    deploy()
    copy_profiles(flag)
    restart()

@task
def deploy():
    with settings(warn_only=True):
        if run('test -d %s' % code_dir).failed:
            with cd(deploy_dir):
                run('sudo git clone http://gitlab.corp.qunar.com/vs/sight_manager.git')
    with cd(code_dir):
        run('sudo git pull')

@task
def restart():
    stop()
    start()
    print_pid()

def copy_profiles(flag=DEV_PROFILES_FLAG):
    '''
        拷贝开发和生产环境的配置文件
    '''
    print 'Copy %s configs.' % flag
    if flag == PROD_PROFILES_FLAG:
        config_path = os.path.join(code_dir, 'config')
        with cd(config_path):
            run('sudo cp -f %s/* .' % PROD_PROFILES_FLAG)
        print "Copy prod configs end"
    elif flag == BETA_PROFILES_FLAG:
        raise Exception('Unsupported now.')
    elif flag == DEV_PROFILES_FLAG:
        pass
    else:
        raise Exception('Error flag %s' % flag)
    print 'Copy configs done.'

def stop():
    with settings(warn_only=True):
        run("ps -ef | grep controller | grep -v grep | awk '{print $2}' | xargs sudo kill -9")

def start():
    with cd(code_dir):
        run('sudo chmod +x start.sh')
        run("sudo ./start.sh", pty=False)

def print_pid():
    pid = run("ps -ef | grep controller | grep -v grep | awk '{print $2}'")
    if pid and pid.isdigit():
        print "启动成功 PID: %s" % str(pid)
