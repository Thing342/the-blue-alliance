import unittest2
import datetime

from google.appengine.ext import testbed
from google.appengine.api import urlfetch

from consts.event_type import EventType

from datafeeds.datafeed_usfirst import DatafeedUsfirst

from models.event import Event
from models.team import Team


class TestDatafeedUsfirstEvents(unittest2.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_urlfetch_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_taskqueue_stub(root_path=".")

        self.datafeed = DatafeedUsfirst()

    def tearDown(self):
        self.testbed.deactivate()

## Breaks with new FIRST website -gregmarra 20151122
#    def test_getEvent(self):
        # test with 2011ct

        # event = self.datafeed.getEventDetails("5561")
        # 
        # self.assertEqual(event.key.id(), "2011ct")
        # self.assertEqual(event.name, "Northeast Utilities FIRST Connecticut Regional")
        # self.assertEqual(event.event_type_enum, EventType.REGIONAL)
        # self.assertEqual(event.start_date, datetime.datetime(2011, 3, 31, 0, 0))
        # self.assertEqual(event.end_date, datetime.datetime(2011, 4, 2, 0, 0))
        # self.assertEqual(event.year, 2011)
        # self.assertEqual(event.venue_address, "Connecticut Convention Center\r\n100 Columbus Blvd\r\nHartford, CT 06103\r\nUSA")
        # self.assertEqual(event.website, "http://www.ctfirst.org/ctr")
        # self.assertEqual(event.event_short, "ct")

    def test_getEventAlliances(self):
        event = Event(
            event_short='cur',
            year=2014,
        )
        alliances = self.datafeed.getEventAlliances(event)
        self.assertEqual(
            alliances,
            [
                {'picks': ['frc254', 'frc469', 'frc2848', 'frc74'], 'declines':[] },
                {'picks': ['frc1718', 'frc2451', 'frc573', 'frc2016'], 'declines':[] },
                {'picks': ['frc2928', 'frc2013', 'frc1311', 'frc842'], 'declines':[] },
                {'picks': ['frc180', 'frc125', 'frc1323', 'frc2468'], 'declines':[] },
                {'picks': ['frc118', 'frc359', 'frc4334', 'frc865'], 'declines':[] },
                {'picks': ['frc135', 'frc1241', 'frc11', 'frc68'], 'declines':[] },
                {'picks': ['frc3478', 'frc177', 'frc294', 'frc230'], 'declines':[] },
                {'picks': ['frc624', 'frc987', 'frc3476', 'frc3015'], 'declines':[] },
            ]
        )

## Breaks with new FIRST website -gregmarra 20151122
#    def test_getEventTeams(self):
        # test with 2011ct
        
        # teams = self.datafeed.getEventTeams(2011, "5561")
        # 
        # sort_key = lambda t: t[1]
        # self.assertEqual(
        #     sorted([(team.team_number, team.first_tpid) for team in teams], key=sort_key),
        #     sorted([(383, 41829), (1124, 42285), (155, 41609), (3634, 51637), (999, 42215), (1699, 42751), (173, 41625), (175, 41629), (716, 42049), (178, 41635), (2170, 43331), (3146, 44577), (2168, 43335), (2067, 43175), (181, 41641), (1991, 43133), (3125, 44539), (2785, 44073), (1740, 42765), (1784, 42895), (3654, 51609), (3718, 49891), (558, 41939), (3719, 52081), (230, 41681), (3464, 49827), (177, 41633), (2064, 43159), (195, 41651), (3104, 44463), (3555, 49069), (3141, 44487), (3461, 47483), (3525, 48801), (237, 41691), (3182, 44547), (571, 41947), (176, 41631), (1071, 42251), (2836, 43965), (126, 41585), (157, 41611), (69, 41519), (1027, 42235), (663, 42007), (3585, 50743), (1073, 42255), (501, 41899), (869, 42131), (714, 42047), (1923, 42947), (743, 42051), (20, 41475), (3204, 44731), (1601, 42659), (2791, 43935), (533, 41919), (694, 42027)], key=sort_key)
        # )

## Breaks with new FIRST website -gregmarra 20151122
#    def test_getEventList(self):
        # events = self.datafeed.getEventList(2011)
        # 
        # self.assertEqual(len(events), 58)  # 58 events expected
        # 
        # self.assertEqual(events[0].first_eid, "5519")
        # self.assertEqual(events[0].event_type_enum, EventType.REGIONAL)
        # self.assertEqual(events[0].name, "BAE Systems/Granite State Regional")
        # 
        # self.assertEqual(events[1].first_eid, "5523")
        # self.assertEqual(events[1].event_type_enum, EventType.REGIONAL)
        # self.assertEqual(events[1].name, "New Jersey Regional")
