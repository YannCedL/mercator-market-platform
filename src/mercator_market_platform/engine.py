# moteur d'agregation de la plateforme economique et financiere MERCATOR

from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus
from beacon_market_event_radar.radar import scan_events
from umbra_market_exposure.exposure import calculate_exposure
from mercury_financial_intel.parser import parse_financials

def market_full_report(siren: str = "383474814") -> ResultContract:
    # genere un rapport economique 360 (evenements + exposition risques + ratios financiers)
    now_iso = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now_iso)
    
    # 1. Événements de marché via Beacon
    beacon_res = scan_events("Airbus")
    
    # 2. Exposition aux risques via Umbra
    umbra_res = calculate_exposure(siren)
    
    # 3. Finances & Ratios via Mercury
    mercury_res = parse_financials(siren)
    
    contract.result = {
        "siren": siren,
        "market_events": beacon_res.result.get("events", []),
        "risk_exposure": umbra_res.result,
        "financial_ratios": mercury_res.result.get("ratios", {}),
        "engines_used": ["beacon", "umbra", "mercury"],
        "status": "rapport_marche_360_complet"
    }
    
    for ev in beacon_res.evidence + umbra_res.evidence + mercury_res.evidence:
        contract.add_evidence(ev)
        
    return contract
