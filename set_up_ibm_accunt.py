from qiskit_ibm_runtime import QiskitRuntimeService

TOKEN = ""

# Save an IBM Quantum account and set it as your default account.
QiskitRuntimeService.save_account(channel="ibm_quantum", token=TOKEN, set_as_default=True)


# test if the account is set up correctly


from qiskit.test.reference_circuits import ReferenceCircuits
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

# You'll need to specify the credentials when initializing QiskitRuntimeService, if they were not previously saved.
service = QiskitRuntimeService()
backend = service.backend("ibmq_qasm_simulator")
job = Sampler(backend).run(ReferenceCircuits.bell())
print(f"job id: {job.job_id()}")
result = job.result()
print(result)