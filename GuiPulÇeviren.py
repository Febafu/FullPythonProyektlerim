import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class CurrencyConverterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.amount_input = TextInput(hint_text='Enter amount', multiline=False)
        self.layout.add_widget(self.amount_input)

        self.from_currency_input = TextInput(hint_text='From currency (e.g., USD)', multiline=False)
        self.layout.add_widget(self.from_currency_input)

        self.to_currency_input = TextInput(hint_text='To currency (e.g., EUR)', multiline=False)
        self.layout.add_widget(self.to_currency_input)

        self.convert_button = Button(text='Convert', size_hint=(None, None), width=200, height=50)
        self.convert_button.bind(on_press=self.convert_currency)
        self.layout.add_widget(self.convert_button)

        self.result_label = Label(text="Result: ")
        self.layout.add_widget(self.result_label)

        return self.layout

    def convert_currency(self, instance):
        amount = self.amount_input.text
        from_currency = self.from_currency_input.text
        to_currency = self.to_currency_input.text

        if amount and from_currency and to_currency:
            api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(api_url)
            data = response.json()

            if 'rates' in data and to_currency in data['rates']:
                rate = data['rates'][to_currency]
                converted_amount = float(amount) * rate
                self.result_label.text = f"Result: {converted_amount} {to_currency}"
            else:
                self.result_label.text = "Invalid currencies"
        else:
            self.result_label.text = "Please fill in all fields"

if __name__ == '__main__':
    CurrencyConverterApp().run()
