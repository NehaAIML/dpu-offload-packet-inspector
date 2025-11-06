import time
from typing import Dict, List, Tuple

class DPUFlowInspector:
    def __init__(self, dpu_cores: int = 8):
        self.dpu_cores = dpu_cores
        self.allowed_subnets = {"10.240.0.0/16", "10.241.0.0/16"}
        self.flow_table: Dict[str, Tuple[str, int]] = {}
        self.inspected_count = 0

    def evaluate_flow(self, src_ip: str, dst_ip: str, protocol: str, port: int) -> bool:
        self.inspected_count += 1
        flow_key = f"{src_ip}->{dst_ip}:{protocol}:{port}"

        if flow_key in self.flow_table:
            return True

        if protocol == "RoCEv2" and port in (4791, 1089):
            self.flow_table[flow_key] = ("ALLOW", int(time.time()))
            return True

        if not dst_ip.startswith("10.24"):
            return False

        self.flow_table[flow_key] = ("ALLOW", int(time.time()))
        return True
