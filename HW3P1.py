class Patient:
    """ base class """

    def __init__(self, name):
        """
        :param name: name of this node
        :param type: type of this node
        """
        self.name = name

    def discharge(self):
        """ abstract method to be overridden in derived classes
        :returns the name and type of the patient when called """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class EmergencyPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        """
        :return: prints the name and type of the patient when called.
        """
        patient_info = [self.name, "Emergency Department Visit"]
        return patient_info

    def get_cost(self):
        cost = 1000
        return cost


class HospitalizedPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        """
        :return: prints the name and type of the patient when called.
        """
        patient_info = [self.name, "Hospitalization"]
        return patient_info

    def get_cost(self):
        cost = 2000
        return cost


class Hospital(Patient):
    def __init__(self, name, future_nodes):
        Patient.__init__(self, name)
        self.futureNodes = future_nodes

    # admit patients by creating a dictionary with patient name as the key, and the type as the value
    def admit(self):
        patient = dict()  # dictionary to store the expected cost of future nodes along with their names as keys
        for Patient in self.futureNodes:
            patient[Patient.name] = Patient.discharge()[1]
        return patient

    # calls the discharge() method on all patients
    def discharge_all(self):
        i = 0
        for Patient in self.futureNodes:
            print(Patient.discharge())
            i += 1

    # returns the total operating cost of the hospital for this day.
    def get_total_cost(self):
        # total_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        cost = 0  # expected cost initialized with the cost of visiting the current node
        i = 0
        for Patient in self.futureNodes:
            cost += Patient.get_cost()
            i += 1
        return cost


#Test  model by admitting 2 patients that needs hospitalization and 3 patients that needs emergency service,

P1 = EmergencyPatient('P1')
P2 = EmergencyPatient('P2')
P3 = EmergencyPatient('P3')
P4 = HospitalizedPatient('P4')
P5 = HospitalizedPatient('P5')
print(P1.discharge())

C1 = Hospital("C1",[P1, P2,P3,P4,P5])
#admit all patients
print('Admitted patient')
admit_dict=C1.admit()
print (admit_dict)
#discahrge them
print('Discharged patient')
C1.discharge_all()
#caculate total cost
all_cost=C1.get_total_cost()
print('Total cost today:', all_cost)