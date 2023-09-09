import logging
import pytest
from cse587Autils.SequenceObjects.SiteModel import SiteModel


def test_valid_construction():
    site_prior = 0.2
    site_probs = [[0.25, 0.25, 0.25, 0.25], [0.1, 0.2, 0.3, 0.4]]
    background_probs = [0.25, 0.25, 0.25, 0.25]

    sm = SiteModel(site_prior, site_probs, background_probs)

    assert sm.background_prior == 0.8
    assert len(sm) == 2


def test_logging(caplog):
    caplog.set_level(logging.WARNING)
    sm = SiteModel()
    sm.site_prior = 0.3  # This will log a warning

    assert ("Setting site_prior will also set "
            "background_prior to 1 - site_prior" in caplog.text)


def test_invalid_precision_type():
    sm = SiteModel()
    with pytest.raises(TypeError):
        sm.precision = 'invalid_type'


def test_invalid_tolerance_type():
    sm = SiteModel()
    with pytest.raises(TypeError):
        sm.tolerance = 'invalid_type'


def test_invalid_site_probs_shape():
    sm = SiteModel()
    with pytest.raises(ValueError):
        sm.site_probs = [[0.25, 0.25, 0.25], [0.1, 0.2, 0.3, 0.4]]


def test_invalid_background_probs_length():
    sm = SiteModel()
    with pytest.raises(ValueError):
        sm.background_probs = [0.25, 0.25, 0.25]