allow_k8s_contexts("k3s-default")

local_resource("k3d", cmd="k3d version")


docker_build(ref="demo-server",
             context=".", 
             dockerfile="server/docker/Dockerfile",
             only=["server"],
             live_update=[
                sync("./server", "/app"),
                run(["/app/target/release/server"])
             ])

k8s_yaml("deploy/server.yaml")
k8s_resource("demo-server", labels="fastapi-service")

k8s_yaml(helm("deploy/loki", name="loki"))
k8s_resource("loki", labels="monitor")

k8s_yaml(helm("deploy/grafana", name="grafana"))
k8s_resource("grafana", labels="monitor", port_forwards=["3000:3000"])

k8s_yaml(helm("deploy/promtail", name="promtail"))
k8s_resource("promtail", labels="monitor")

k8s_yaml(helm("deploy/prometheus", name="prometheus"))
k8s_resource("prometheus-server", labels="monitor")
k8s_resource("prometheus-alertmanager", labels="monitor")
k8s_resource("prometheus-node-exporter", labels="monitor")
k8s_resource("prometheus-kube-state-metrics", labels="monitor")
k8s_resource("prometheus-pushgateway", labels="monitor")