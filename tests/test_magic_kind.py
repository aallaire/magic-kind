
import pytest

from magic_kind import MagicKind


class Soda(MagicKind):
    COLA = "cola"
    LEMON_LIME = "lemon_lime"
    ROOT_BEER = "root_beer"


class HttpCode(MagicKind):
    OK = 200
    NOT_FOUND = 404
    GATEWAY_TIMEOUT = 503


class TestMagicKind:
    def test_soda(self):
        assert Soda.COLA == "cola"
        assert "cola" in Soda
        assert len(Soda) == 3
        assert set([_ for _ in Soda]) == set(["cola", "lemon_lime", "root_beer"])
        assert Soda.get_names() == {"COLA", "LEMON_LIME", "ROOT_BEER"}
        assert Soda.get_dict() == {
            "COLA": "cola",
            "LEMON_LIME": "lemon_lime",
            "ROOT_BEER": "root_beer",
        }
        assert Soda["ROOT_BEER"] == Soda.ROOT_BEER =="root_beer"
        with pytest.raises(KeyError):
            assert Soda["THUMBS_UP"]

    def test_http_code(self):
        assert HttpCode.OK == 200
        assert 404 in HttpCode
        assert 3000 not in HttpCode
        assert HttpCode.get_names() == {"OK", "NOT_FOUND", "GATEWAY_TIMEOUT"}
        assert HttpCode.get_dict() == {
            "OK": 200,
            "NOT_FOUND": 404,
            "GATEWAY_TIMEOUT": 503,
        }
        assert HttpCode["OK"] == HttpCode.OK == 200
        with pytest.raises(KeyError):
            assert HttpCode["FOO"]

