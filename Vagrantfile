VAGRANTFILE_API_VERSION = "2"

Vagrant.configure (VAGRANTFILE_API_VERSION) do |master|
  master.ssh.insert_key = false
  master.ssh.forward_agent = true

  # Official CentOS 7 box: Backend
  master.vm.define "direct-exam" do |conf|
    conf.vm.hostname = "direct-exam"
    conf.vm.box = "centos/7"
    conf.vm.network "private_network", ip: "10.11.12.13"
    conf.vm.synced_folder ".", "/vagrant", disabled: true

    conf.vm.provider :virtualbox do |vb|
      vb.memory = 4096
      vb.cpus = 2
    end

    conf.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbooks/exam-stack.yml"
      ansible.inventory_path = "hosts/inventory"
      ansible.vault_password_file = "password_file"
    end
  end
end
