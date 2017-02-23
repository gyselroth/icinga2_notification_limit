from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

default_task = "publish"

name = "icinga2_mail_notification_limit"
version = "0.0.1"
description = "mail-notification-script for icinga2 with limits configurable per sender"
authors = [Author("Fabian Jucker", "jucker@gyselroth.com")]
url = "https://github.com/gyselroth"

@init
def initialize(project):
    project.depends_on_requirements("requirements.txt")
    project.build_depends_on("mock")
