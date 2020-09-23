import exercise
import datetime
from exercise import coolapi


def test_utc_time_to_datetime():
    expected = datetime.datetime(2007, 7, 15, 19).timestamp()
    assert exercise.utc_time_to_timestamp("2007-07-15 19:00:00 UTC") == expected


def test_read_csv():
    reader = exercise.read_from_csv("data.csv")
    assert next(reader) == {
        "id": "67",
        "observed_on_string": "July 15, 2007 12:00",
        "observed_on": "2007-07-15",
        "time_observed_at": "2007-07-15 19:00:00 UTC",
        "time_zone": "Pacific Time (US & Canada)",
        "user_id": "15",
        "user_login": "gdurkee",
        "created_at": "2008-03-26 10:25:54 UTC",
        "updated_at": "2016-06-22 18:16:15 UTC",
        "quality_grade": "casual",
        "license": "CC-BY",
        "url": "http://www.inaturalist.org/observations/67",
        "image_url": "",
        "sound_url": "",
        "tag_list": "",
        "description": "Nesting in pond with 6 young. By mid-September, there was no sign of adult or any young. There was most likely predation from resident goshawk and possibly coyote, but 2 ducklings may have survived and moved by early fall. This was the 2nd year Mallard had nested in this pond.",
        "num_identification_agreements": "0",
        "num_identification_disagreements": "0",
        "captive_cultivated": "false",
        "oauth_application_id": "",
        "place_guess": "McClure Meadow, Kings Canyon National Park, CA, USA",
        "latitude": "37.1875",
        "longitude": "-118.7440032959",
        "positional_accuracy": "",
        "geoprivacy": "",
        "taxon_geoprivacy": "",
        "coordinates_obscured": "false",
        "positioning_method": "",
        "positioning_device": "",
        "species_guess": "Mallard",
        "scientific_name": "Anas platyrhynchos",
        "common_name": "Mallard",
        "iconic_taxon_name": "Aves",
        "taxon_id": "6930",
    }


def test_preprocess():
    original = {
        "id": "67",
        "observed_on_string": "July 15, 2007 12:00",
        "observed_on": "2007-07-15",
        "time_observed_at": "2007-07-15 19:00:00 UTC",
        "time_zone": "Pacific Time (US & Canada)",
        "user_id": "15",
        "user_login": "gdurkee",
        "created_at": "2008-03-26 10:25:54 UTC",
        "updated_at": "2016-06-22 18:16:15 UTC",
        "quality_grade": "casual",
        "license": "CC-BY",
        "url": "http://www.inaturalist.org/observations/67",
        "image_url": "",
        "sound_url": "",
        "tag_list": "",
        "description": "Nesting in pond with 6 young. By mid-September, there was no sign of adult or any young. There was most likely predation from resident goshawk and possibly coyote, but 2 ducklings may have survived and moved by early fall. This was the 2nd year Mallard had nested in this pond.",
        "num_identification_agreements": "0",
        "num_identification_disagreements": "0",
        "captive_cultivated": "false",
        "oauth_application_id": "",
        "place_guess": "McClure Meadow, Kings Canyon National Park, CA, USA",
        "latitude": "37.1875",
        "longitude": "-118.7440032959",
        "positional_accuracy": "",
        "geoprivacy": "",
        "taxon_geoprivacy": "",
        "coordinates_obscured": "false",
        "positioning_method": "",
        "positioning_device": "",
        "species_guess": "Coyote",
        "scientific_name": "Anas platyrhynchos",
        "common_name": "Mallard",
        "iconic_taxon_name": "Aves",
        "taxon_id": "6930",
    }
    result = exercise.preprocess(original)
    assert result is not original
    assert "user_id" not in result
    assert "user_login" not in result
    assert result["species_guess"] == "Coyote"
    assert result["time_observed_at"] == 1184551200.0


def test_transform():
    original = {
        "id": "1238",
        "observed_on_string": "January 12, 2008 17:04",
        "observed_on": "2008-01-12",
        "time_observed_at": 1200215040.0,
        "time_zone": "Pacific Time (US & Canada)",
        "created_at": "2009-01-13 23:26:04 UTC",
        "updated_at": "2018-08-22 00:52:13 UTC",
        "quality_grade": "research",
        "license": "CC0",
        "url": "http://www.inaturalist.org/observations/1238",
        "image_url": "https://static.inaturalist.org/photos/1368/medium.jpg?1444257560",
        "sound_url": "",
        "tag_list": "",
        "description": 'Seriously Matt, how do you <a href="http://flickr.com/photos/mattknoth/sets/72157602051675794/">do it</a>?  I was pretty psyched to see this fellow, but he definitely did not feel the same, and trotted off post haste.  I guess something more than a 18-55mm would have helped...',
        "num_identification_agreements": "4",
        "num_identification_disagreements": "0",
        "captive_cultivated": "false",
        "oauth_application_id": "",
        "place_guess": "Lafayette, California, United States",
        "latitude": "37.9361953735",
        "longitude": "-122.1150054932",
        "positional_accuracy": "",
        "geoprivacy": "",
        "taxon_geoprivacy": "",
        "coordinates_obscured": "false",
        "positioning_method": "",
        "positioning_device": "",
        "species_guess": "Coyote",
        "scientific_name": "Canis latrans",
        "common_name": "Coyote",
        "iconic_taxon_name": "Mammalia",
        "taxon_id": "42051",
    }
    result = exercise.transform(original)
    assert result is not original
    assert result["address"] == {
        "latitude": "37.9361953735",
        "longitude": "-122.1150054932",
    }
    assert result["dates"] == {
        "created_at": "2009-01-13 23:26:04 UTC",
        "updated_at": "2018-08-22 00:52:13 UTC",
    }


def test_send_to_api(monkeypatch):
    data = exercise.transform(
        {
            "id": "1238",
            "observed_on_string": "January 12, 2008 17:04",
            "observed_on": "2008-01-12",
            "time_observed_at": 1200215040.0,
            "time_zone": "Pacific Time (US & Canada)",
            "created_at": "2009-01-13 23:26:04 UTC",
            "updated_at": "2018-08-22 00:52:13 UTC",
            "quality_grade": "research",
            "license": "CC0",
            "url": "http://www.inaturalist.org/observations/1238",
            "image_url": "https://static.inaturalist.org/photos/1368/medium.jpg?1444257560",
            "sound_url": "",
            "tag_list": "",
            "description": 'Seriously Matt, how do you <a href="http://flickr.com/photos/mattknoth/sets/72157602051675794/">do it</a>?  I was pretty psyched to see this fellow, but he definitely did not feel the same, and trotted off post haste.  I guess something more than a 18-55mm would have helped...',
            "num_identification_agreements": "4",
            "num_identification_disagreements": "0",
            "captive_cultivated": "false",
            "oauth_application_id": "",
            "place_guess": "Lafayette, California, United States",
            "latitude": "37.9361953735",
            "longitude": "-122.1150054932",
            "positional_accuracy": "",
            "geoprivacy": "",
            "taxon_geoprivacy": "",
            "coordinates_obscured": "false",
            "positioning_method": "",
            "positioning_device": "",
            "species_guess": "Coyote",
            "scientific_name": "Canis latrans",
            "common_name": "Coyote",
            "iconic_taxon_name": "Mammalia",
            "taxon_id": "42051",
        }
    )

    def mockreturn(x, y, **args):
        return {"status": 200, "message": "cool"}

    monkeypatch.setattr(coolapi.CoolApi, "send_to_api", mockreturn)
    x = exercise.send_to_api(data)
    assert x == 200
