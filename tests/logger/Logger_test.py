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

    def test_should_use_basic_config_instead_of_config(self):
        ConfigureLogger(log_level=logging.INFO)
        logging.info('testing to console')
        self.assertFalse(os.path.exists('automata.log'))


if __name__ == '__main__':
    unittest.main()
