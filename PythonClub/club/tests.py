from django.test import TestCase
from .models import Meeting, Minutes, Resource, Event
from .forms import MeetingForm
from datetime import datetime
from django.urls import reverse

# Create your tests here.
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting = Meeting(meetingtitle = 'Setup')
        self.assertEqual(str(meeting), meeting.meetingtitle)
        meeting = Meeting(meetingtitle = 'Config')
        self.assertEqual(str(meeting), meeting.meetingtitle)
        meeting = Meeting(meetingtitle = 'First View')
        self.assertEqual(str(meeting), meeting.meetingtitle)
        meeting = Meeting(meetingtitle = 'Create List Page')
        self.assertEqual(str(meeting), meeting.meetingtitle)
        meeting = Meeting(meetingtitle = 'Models')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tableName(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MinutesTest(TestCase):
    def test_tableName(self):
        self.assertEqual(str(Minutes._meta.db_table), 'minutes')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource = Resource(resourcename = 'The Django Book')
        self.assertEqual(str(resource), resource.resourcename)
        resource = Resource(resourcename = 'Django Documents Tutorial')
        self.assertEqual(str(resource), resource.resourcename)
        resource = Resource(resourcename = 'Django Girls Tutorial')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tableName(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_tableName(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/index.html')

class TestGetMeeting(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/meetings', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/meetings.html')

class New_Meeting_Form_Test(TestCase):

    #Valid Form Data
    def test_MeetingForm_is_valid(self):
        form = MeetingForm(data={'meetingtitle': "Models", 'meetingdate': "2019-01-23", 'meetinglocation': "Broadway Edison Building", 'agenda': "Create Model Classes, Register Model Classes with Admin, Migrate Models, and Create Superuser"})
        self.assertTrue(form.is_valid())

    #Invalid Form Data
    def test_MeetingForm_invalid(self):
        form = MeetingForm(data={'meetingtitle': "Tests", 'meetingdate': "2019-02-27", 'meetinglocation': "Broadway Edison Building", 'agenda': "Test forms"})
        self.assertFalse(form.is_valid())

