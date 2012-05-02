import os, sys

if __name__ == '__main__':
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    
    if len(sys.argv) == 1:
        # Use name of parent directory as app name
        app_name = os.path.split(os.path.abspath(os.path.join(
            os.path.realpath(__file__), os.path.pardir)
        ))[1]

        testModules = [app_name,]
    else:
        testModules = sys.argv[1:]

    from django.test.simple import DjangoTestSuiteRunner
    runner = DjangoTestSuiteRunner()
    failures = runner.run_tests(testModules, verbosity=1, interactive=True)

    sys.exit(failures)

