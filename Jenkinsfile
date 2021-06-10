node {
   stage('Get Source') {
      // copy source code from local file system and test
      // for a Dockerfile to build the Docker image
      git ('https://github.com/arksinha93/python-flask-demo.git')
      if (!fileExists("Dockerfile")) {
         error('Dockerfile missing.')
      }
   }
   stage('Build Docker') {
       // build the docker image from the source code using the BUILD_ID parameter in image name
         sh "sudo docker build -t flask-app ."
   }
   stage("Test and Deploy Docker Container"){
        sh "sudo docker run -p 5000:5000 --name flask-app -d flask-app "
        sh "sudo docker rm --force flask-app"
    }
}
