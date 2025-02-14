from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class ExpenseTrackerApp(App):
    def build(self):
        self.budget = 1000
        self.expenses = []
        self.total_expense = 0

        self.layout = BoxLayout(orientation='vertical')

        self.budget_label = Label(text=f'Budget: {self.budget}')
        self.layout.add_widget(self.budget_label)

        self.expense_input = TextInput(hint_text='Enter expense (amount description)', multiline=False)
        self.layout.add_widget(self.expense_input)

        self.add_expense_button = Button(text='Add Expense')
        self.add_expense_button.bind(on_press=self.add_expense)
        self.layout.add_widget(self.add_expense_button)

        self.expense_list = ScrollView()
        self.expense_label = Label(text='Expenses: \n')
        self.expense_list.add_widget(self.expense_label)
        self.layout.add_widget(self.expense_list)

        return self.layout

    def add_expense(self, instance):
        expense = self.expense_input.text
        if expense:
            amount = float(expense.split()[0])
            self.total_expense += amount
            self.expenses.append(expense)

            self.expense_label.text += f'\n{expense}'

            if self.total_expense > self.budget:
                self.budget_label.text = f'Budget exceeded! Current total: {self.total_expense}'
            else:
                self.budget_label.text = f'Budget: {self.budget - self.total_expense}'


if __name__ == '__main__':
    ExpenseTrackerApp().run()
