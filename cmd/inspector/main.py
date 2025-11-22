from pkg.engine.inspector import DPUFlowInspector

def main():
    print("DPU Offload Packet Inspector [SmartNIC Out-of-Band Data Plane]")
    inspector = DPUFlowInspector(dpu_cores=8)
    allowed = inspector.evaluate_flow("10.240.12.4", "10.240.12.8", "RoCEv2", 4791)
    print(f"Flow [RoCEv2 RDMA Fabric]: Allowed={allowed} (Evaluated on DPU)")
    blocked = inspector.evaluate_flow("10.240.12.4", "198.51.100.22", "TCP", 443)
    print(f"Flow [External Exfiltration]: Allowed={blocked} (Dropped at SmartNIC line-rate)")

if __name__ == "__main__":
    main()
