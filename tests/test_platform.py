# test du rapport marché 360 de la plateforme Mercator
from mercator_market_platform.engine import market_full_report

def test_rapport_marche_360():
    contract = market_full_report("383474814")
    assert contract is not None
    assert len(contract.result["market_events"]) >= 1
    assert contract.result["risk_exposure"]["exposure_score"] > 0
    assert len(contract.evidence) >= 3
