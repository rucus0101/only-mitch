CURRENT_DIR := $(shell pwd)

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start: ## Deploy ceos lab
	sudo containerlab deploy --debug --topo $(CURRENT_DIR)/avd_inventory/clab/topology.clab.yml --max-workers 2 --timeout 5m --reconfigure

.PHONY: stop
stop: ## Destroy ceos lab
	sudo containerlab destroy --debug --topo $(CURRENT_DIR)/avd_inventory/clab/topology.clab.yml --cleanup

.PHONY: build_evpn_vxlan
build_evpn_vxlan: ## Generate AVD configs
	cd $(CURRENT_DIR)/avd_inventory; ansible-playbook playbooks/build_evpn_fabric.yml

.PHONY: deploy_evpn_vxlan
deploy_evpn_vxlan: ## Deploy AVD configs using eAPI
	cd $(CURRENT_DIR)/avd_inventory; ansible-playbook playbooks/deploy_evpn_fabric.yml

.PHONY: diff_evpn_vxlan
diff_evpn_vxlan: ## Show the diff between running config and designed config
	cd $(CURRENT_DIR)/avd_inventory; ansible-playbook --diff --check playbooks/deploy_evpn_fabric.yml

.PHONY: validate_evpn_vxlan
validate_evpn_vxlan: ## validate the network state
	cd $(CURRENT_DIR)/avd_inventory; ansible-playbook playbooks/validate_evpn_fabric.yml

.PHONY: cmdo
cmdo: ## get cmdo snapshot
	./cmdo -i $(CURRENT_DIR)/avd_inventory/cmdo_inventory.yml -t
