from mercator_market_platform.engine import market_full_report

def test_market_full_report():
    c = market_full_report("383474814")
    assert "mercury" in c.result["engines_used"]
    assert c.confidence > 0.8
