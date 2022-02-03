"""Unit tests for configuration handling in Annif"""

import logging
import pytest
import annif.config
from annif.exception import ConfigurationException


def test_find_config_exists_cfg():
    cfg = annif.config.find_config('tests/projects.cfg')
    assert cfg == 'tests/projects.cfg'


def test_find_config_exists_toml():
    cfg = annif.config.find_config('tests/projects.toml')
    assert cfg == 'tests/projects.toml'


def test_find_config_not_exists(caplog):
    with caplog.at_level(logging.WARNING):
        cfg = annif.config.find_config('tests/notfound.cfg')
    assert cfg is None
    assert 'Project configuration file "tests/notfound.cfg" is missing' \
        in caplog.text


def test_find_config_exists_default(monkeypatch):
    # temporarily chdir to the tests directory
    monkeypatch.chdir('tests')
    cfg = annif.config.find_config('')
    assert cfg == 'projects.cfg'


def test_find_config_not_exists_default(monkeypatch, caplog):
    # temporarily chdir to the tests/corpora directory
    monkeypatch.chdir('tests/corpora')
    with caplog.at_level(logging.WARNING):
        cfg = annif.config.find_config('')
    assert cfg is None
    assert 'Could not find project configuration file' in caplog.text


def test_parse_config_cfg():
    cfg = annif.config.parse_config('tests/projects.cfg')
    assert isinstance(cfg, annif.config.AnnifConfigCFG)
    assert len(cfg.project_ids) == 16
    assert cfg['dummy-fi'] is not None


def test_parse_config_toml():
    cfg = annif.config.parse_config('tests/projects.toml')
    assert isinstance(cfg, annif.config.AnnifConfigTOML)
    assert len(cfg.project_ids) == 2
    assert cfg['dummy-fi-toml'] is not None


def test_parse_config_toml_failed(tmpdir):
    conffile = tmpdir.join('projects.toml')
    conffile.write("[section]\nkey=unquoted\n")
    with pytest.raises(ConfigurationException) as excinfo:
        annif.config.parse_config(str(conffile))
    assert 'Invalid value' in str(excinfo.value)
