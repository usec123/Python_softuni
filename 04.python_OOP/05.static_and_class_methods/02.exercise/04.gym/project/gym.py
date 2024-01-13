from .customer import Customer
from .trainer import Trainer
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        # subscription = ''
        # customer = ''
        # trainer = ''
        # equipment = ''
        # plan = ''
        subscription, customer, trainer, equipment, exercise_plan = None, None, None, None, None

        for sub in self.subscriptions:
            if sub.id == subscription_id:
                subscription = sub
                break
        for cust in self.customers:
            if cust.id == subscription.customer_id:
                customer = str(cust)
                break
        for tr in self.trainers:
            if tr.id == subscription.trainer_id:
                trainer = str(tr)
                break
        for p in self.plans:
            if p.id == subscription.exercise_id:
                exercise_plan = p
                break
        for eq in self.equipment:
            if eq.id == exercise_plan.equipment_id:
                equipment = str(eq)
                break

        return '\n'.join([str(subscription), customer, trainer, equipment, str(exercise_plan)])
