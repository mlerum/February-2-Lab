"""Classes for melon orders."""
class AbstractMelonOrder:
    """Abstract base class that other melon orders inherit from"""

    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = 0

    def get_total(self):

        base_price = 5

        if self.species == 'christmas':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        
        super().__init__(species, qty)

        self.order_type = "government"
        self.passed_inspection = False

    def mark_inspection(self, passed):

        if passed == True:
            self.passed_inspection = True
        elif not passed:
            self.passed_inspection = False

# x = GovernmentMelonOrder(...)
# x is GovernmentMelonOrder
# x is AbstractMelonOrder
        
# if __name__ == '__main__': # Only run if I invoke this file directly - python3 melons.py
#     # some tests that check if the melon classes work right

# # In some other file
# import melons
# order = GovernmentMelonOrder(...)
# stuff under the if statements doesn't run