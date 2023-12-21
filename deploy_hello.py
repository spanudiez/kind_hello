---
- name: deploy hello 
  gather_facts: No
  hosts: lab

  tasks:
#    - name: Check that K8s is up

    - name: copy helm dir to k8s server
      ansible.builtin.copy:
        src: /root/ansible_test/helm
        dest: /home/ispanu/
        follow: no


#    - name: create nginx image

#    - name: deploy app 

