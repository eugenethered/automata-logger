import glob
import logging
import os
import os.path
import unittest

from logger.ConfigureLogger import ConfigureLogger


class ConfigureLoggerTestCase(unittest.TestCase):

    def tearDown(self):
        # delete all log files
        for file in glob.glob('automata.*'):
            os.remove(file)

    def test_should_obtain_config_from_package(self):
        logger = ConfigureLogger()
        result = logger.get_log_config_file_contents('default-log-config.yaml')
        self.assertIsNotNone(result)

    def test_should_load_default_logging_config(self):
        ConfigureLogger()
        log = logging.getLogger('testing')
        log.info('test 1 2 3')
        with open('automata.log') as f:
            log_file_contents = f.read()
        self.assertIsNotNone(log_file_contents)
        self.assertIn('- testing - INFO - test 1 2 3', log_file_contents)

    def test_should_load_default_logging_config_without_specific_name(self):
        ConfigureLogger()
        logging.info('test again 3 2 1')
        with open('automata.log') as f:
            log_file_contents = f.read()
        self.assertIsNotNone(log_file_contents)
        self.assertIn('- root - INFO - test again 3 2 1', log_file_contents)

    def test_should_use_basic_config_instead_of_config(self):
        ConfigureLogger(log_level=logging.INFO)
        logging.info('testing to console')
        self.assertFalse(os.path.exists('automata.log'))


if __name__ == '__main__':
    unittest.main()
