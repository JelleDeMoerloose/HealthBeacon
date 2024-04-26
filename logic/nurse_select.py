from logic.nurse import Nurse
from logic.patient import Patient
from logic.context import IContext
import random
from abc import ABC, abstractmethod


class INurseSelect(ABC):
    @abstractmethod
    def select_nurse(self, patient_id: Patient) -> Nurse:
        pass


class HardcodedNurseSelect(INurseSelect):

    # adding context with depedency injection
    def __init__(self, context: IContext):
        self.context = context

    def select_nurse(self, patient_id: Patient) -> Nurse:
        # bad way of selecting nurse but it is harcoded
        # we will not use patient_id as our way of selecting nurses wont use any context just random
        nurses = self.context
