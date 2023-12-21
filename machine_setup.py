---
- name: Prepare VM
  gather_facts: No
  hosts: lab

  tasks:
    - name: Install packages 
      yum:
        name: [yum-utils, device-mapper-persistent-data, lvm2]
        state: latest

    - name: Add Docker repo
      get_url:
        url: https://download.docker.com/linux/centos/docker-ce.repo
        dest: /etc/yum.repos.d/docer-ce.repo
      become: yes

    - name: Enable Docker Edge repo
      ini_file:
        dest: /etc/yum.repos.d/docer-ce.repo
        section: 'docker-ce-edge'
        option: enabled
        value: 0
      become: yes

    - name: Enable Docker Test repo
      ini_file:
        dest: /etc/yum.repos.d/docer-ce.repo
        section: 'docker-ce-test'
        option: enabled
        value: 0
      become: yes

    - name: Install Docker
      package:
        name: docker-ce
        state: latest
      become: yes

    - name: Pip Install
      package:
        name: python3-pip
        state: latest
      become: yes

    - name: docker-py module for ansible
      pip:
        name: "{{ item }}"
        state: latest
      with_items:
      - six
      - docker-py
    
    - name: Start Docker service
      service:
        name: docker
        state: started
        enabled: yes
      become: yes

    - name: Add user vagrant to docker group
      user:
        name: vagrant
        groups: docker
        append: yes
      become: yes

    - name: Docker Login
      docker_login:
        username: spanudiez
        password: dckr_pat_2q_BHDikd3ndoZ1S6Bt7b2Tz55A
    
    - name: Install Kind
      get_url:
        url: https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
        dest: /usr/local/bin/kind
        mode: "0755"
  
    - name: Copy kind docker proxy config
      ansible.builtin.copy:
        src: /root/ansible_test/files/docker_proxy.yml
        dest: /home/ispanu/docker_proxy.yml
        follow: no

    - name: Check K8s cluster
      command: kind get clusters
      register: result

    - name: Start K8s Cluster
      ansible.builtin.command:
        cmd: kind create cluster --name hello --config /home/ispanu/docker_proxy.yml
      when: result.stdout == "" 
     
    - name: Install kubectl
      become: true
      get_url:
        url: https://dl.k8s.io/release/v1.29.0/bin/linux/amd64/kubectl 
        dest: /usr/local/bin/kubectl
        mode: "0755"
   
    - name: Fetch kubeconfig
      ansible.builtin.fetch:
        src: /root/.kube/config
        dest: /root/.kube/config
        flat: yes
