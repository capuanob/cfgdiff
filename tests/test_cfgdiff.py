import unittest
import cfgdiff


class CfgDiffTestCase(unittest.TestCase):

    def _test_same(self, cls, filea, fileb, parser=None):
        a = cls(filea, ordered=False, parser=parser)
        b = cls(fileb, ordered=False, parser=parser)

        self.assertIsNone(a.error)
        self.assertIsNone(b.error)

        self.assertEqual(a.readlines(), b.readlines())

    def _test_different(self, cls, filea, fileb, parser=None):
        a = cls(filea, ordered=False, parser=parser)
        b = cls(fileb, ordered=False, parser=parser)

        self.assertIsNone(a.error)
        self.assertIsNone(b.error)

        self.assertNotEqual(a.readlines(), b.readlines())


class INIDiffTestCase(CfgDiffTestCase):

    def test_ini_same(self):
        self._test_same(cfgdiff.INIDiff, './tests/test_same_1-a.ini',
                        './tests/test_same_1-b.ini')

    def test_ini_different(self):
        self._test_different(cfgdiff.INIDiff,
                             './tests/test_different_1-a.ini',
                             './tests/test_different_1-b.ini')


class JSONDiffTestCase(CfgDiffTestCase):

    def test_json_same(self):
        self._test_same(cfgdiff.JSONDiff, './tests/test_same_1-a.json',
                        './tests/test_same_1-b.json')

    def test_json_different(self):
        self._test_different(cfgdiff.JSONDiff,
                             './tests/test_different_1-a.json',
                             './tests/test_different_1-b.json')


@unittest.skipUnless('yaml' in cfgdiff.supported_formats, 'requires PyYAML')
class YAMLDiffTestcase(CfgDiffTestCase):

    def test_yaml_same(self):
        self._test_same(cfgdiff.YAMLDiff, './tests/test_same_1-a.yaml',
                        './tests/test_same_1-b.yaml')

    def test_yaml_different(self):
        self._test_different(cfgdiff.YAMLDiff,
                             './tests/test_different_1-a.yaml',
                             './tests/test_different_1-b.yaml')


@unittest.skipUnless('xml' in cfgdiff.supported_formats, 'requires LXML')
class XMLDiffTestCase(CfgDiffTestCase):

    def test_xml_same(self):
        self._test_same(cfgdiff.XMLDiff, './tests/test_same_1-a.xml',
                        './tests/test_same_1-b.xml')

    def test_xml_different(self):
        self._test_different(cfgdiff.XMLDiff,
                             './tests/test_different_1-a.xml',
                             './tests/test_different_1-b.xml')


@unittest.skipUnless('conf' in cfgdiff.supported_formats, 'requires ConfigObj')
class ConfigDiffTestCase(CfgDiffTestCase):

    def test_conf_same(self):
        self._test_same(cfgdiff.ConfigDiff, './tests/test_same_1-a.ini',
                        './tests/test_same_1-b.ini')

    def test_conf_different(self):
        self._test_different(cfgdiff.ConfigDiff,
                             './tests/test_different_1-a.ini',
                             './tests/test_different_1-b.ini')


@unittest.skipUnless('reconf' in cfgdiff.supported_formats,
                     'requires reconfigure')
class ReconfigureDiffTestCase(CfgDiffTestCase):

    def setUp(self):
        configs = __import__('reconfigure.configs', fromlist=['reconfigure'])
        self.parser = configs.SambaConfig

    @unittest.expectedFailure
    def test_reconf_same(self):
        self._test_same(cfgdiff.ReconfigureDiff,
                        './tests/test_same_1-a.ini',
                        './tests/test_same_1-b.ini', self.parser)

    def test_reconf_different(self):
        self._test_different(cfgdiff.ReconfigureDiff,
                             './tests/test_different_1-a.ini',
                             './tests/test_different_1-b.ini', self.parser)


@unittest.skipUnless('zone' in cfgdiff.supported_formats, 'requires dnspython')
class ZoneDiffTestCase(CfgDiffTestCase):

    def test_zone_same(self):
        self._test_same(cfgdiff.ZoneDiff,
                        './tests/test_same_1-a.zone',
                        './tests/test_same_1-b.zone')

    def test_zone_different(self):
        self._test_different(cfgdiff.ZoneDiff,
                             './tests/test_different_1-a.zone',
                             './tests/test_different_1-b.zone')
