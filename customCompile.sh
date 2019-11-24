#git submodule update --init \
#&& \
cd submodules/incubator-datasketches-memory \
&& \
mvn clean install -DskipTests=true \
&& \
cd ../incubator-datasketches-java \
&& \
mvn clean install -DskipTests=true \
&& \
cd ../incubator-datasketches-characterization \
&& \
mvn clean install -DskipTests=true \
&& \
cd ../ \
&& \
cp incubator-datasketches-*/target/*incubating.jar incubator-datasketches-characterization/target/*SNAPSHOT.jar .. \
&& \
cd ../

