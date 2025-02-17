import sagemaker
from sagemaker.sklearn.estimator import SKLearn

# Sesión de SageMaker
sagemaker_session = sagemaker.Session()

# Rol de ejecución (toma el rol de la instancia actual)
role = sagemaker.get_execution_role()

# Bucket donde subiste genetico.py
bucket = sagemaker_session.default_bucket()

sklearn_estimator = SKLearn(
    entry_point="8reinas.py",  # El script de entrenamiento
    source_dir=".",  # Donde está el código
    role=role,
    instance_type="ml.t3.large",  # Tipo de instancia (puedes cambiarlo) medium no va
    instance_count=1,
    framework_version="0.23-1",  # Versión de SKLearn
    py_version="py3",
    sagemaker_session=sagemaker_session
)

sklearn_estimator.fit()

#source_dir="s3://sagemaker-jmi/".format(bucket),  # Donde está el código