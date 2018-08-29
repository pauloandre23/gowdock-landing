Landing Page do Gowdock
=======================

- templates em `landing_page/templates`  

Rodando Localmente (sem kubernetes)
------------------

para rodar localmente, rode `gunicorn -b :8080 gowdock_landing.wsgi`  


Kubernetes
----------

[Minikube](https://kubernetes.io/docs/tasks/tools/install-kubectl/)  
[Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) ou [Google Cloud SDK](https://cloud.google.com/sdk/)  

O Dockerfile descreve o container que vai rodar o django.  
Usaremos um container pronto do postgres, configurando com envs em `postgresql-*.yml`  

Para rodar localmente no minikube, use os arquivos `postgresql-local.yaml` e `deployment_minikube.yaml`:  

```
    kubectl create -f postgresql-local.yaml
    kubectl create -f deployment_minikube.yaml
```

Para rodar no GCloud, use os arquivos `postgresql-gce.yaml` e `deployment.yaml`:  

``` 
    kubectl create -f postgresql-gce.yaml
    kubectl create -f deployment.yaml
```

Em ambos os casos, será necessário criar o usuário e banco, manualmente, mas só na primeira vez.  

Ambos metodos necessitam do secret definido em `secrets.yaml` para autenticar com o banco. Os segredos ficam codificados em base64, entao se for necessario trocá-los, devem ser codificados antes (por exemplo `cat senha.txt | base64` ).  
