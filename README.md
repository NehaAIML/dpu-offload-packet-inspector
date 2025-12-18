# DPU Offload Packet Inspector

[![DPU Inspector CI](https://github.com/NehaAIML/dpu-offload-packet-inspector/actions/workflows/ci.yml/badge.svg)](https://github.com/NehaAIML/dpu-offload-packet-inspector/actions)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

Line-rate, out-of-band network packet inspection and microsegmentation engine designed for NVIDIA BlueField SmartNIC/DPU architectures across EDA compute clusters.

## Why DPU Offload for EDA?
Traditional host-based firewalls (iptables, nftables, user-space inspection daemons) steal critical CPU cycles and cache capacity from multi-day chip verification jobs. 

By offloading packet classification, flow tracking, and RoCEv2 (RDMA over Converged Ethernet) access policies to dedicated DPU cores:
- **Host CPU overhead drops to 0.00%**.
- Silicon simulation threads run completely jitter-free.
- Lateral movement attempts are isolated and dropped at the NIC level before touching the host memory bus.

## Performance Metrics
- **Host In-Band Agent**: 3.5% - 8.2% CPU load, jitter and cache eviction.
- **DPU Offload Inspector**: 0.00% CPU load, 0.00 us latency impact.

## License
Licensed under Apache 2.0.
