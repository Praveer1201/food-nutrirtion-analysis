{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Praveer1201/food-nutrirtion-analysis/blob/main/dietpalnner5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "def get_bmi_category(bmi):\n",
        "    if bmi < 18.5:\n",
        "        return \"underweight\"\n",
        "    elif 18.5 <= bmi <= 24.9:\n",
        "        return \"normal weight\"\n",
        "    elif 25 <= bmi <= 29.9:\n",
        "        return \"overweight\"\n",
        "    else:\n",
        "        return \"obese\"\n",
        "\n",
        "def generate_diet_plan(weight, height):\n",
        "    bmi = weight / (height ** 2)\n",
        "    bmi_category = get_bmi_category(bmi)\n",
        "\n",
        "    if bmi_category == \"underweight\":\n",
        "      diet_plan = {\n",
        "            \"breakfast\": [\n",
        "                {\"monday\": \"Oatmeal with fruit and nuts\", \"calories\": 300},\n",
        "                {\"monday\": \"Yogurt with berries and granola\", \"calories\": 250},\n",
        "                {'tuesday':'2 Paneer paratha ','calories':300},\n",
        "                {'tuesday':'Moong Dal Chilla','calories': 200-250},\n",
        "                {'wednesday':'Paratha (Indian flatbread) with Ghee','calories': 600-700},\n",
        "                {'wednesday':'Paneer Bhurji ','calories': 300},\n",
        "                {'thursday':'Whole Milk','calories': 150},\n",
        "                {'thursday':'Mixed Nuts','calories':200-300},\n",
        "                {'friday':'Banana','calories': 100},\n",
        "                {'friday':'Fruit Yogurt','calories':150},\n",
        "                {'saturday':'Egg Omelette','calories':100-150},\n",
        "                {'saturday':'Sprouts Salad','calories':100},\n",
        "                {'sunday':'Vegetable Poha','calories':110},\n",
        "                {'sunday':'Masala Oats','calories':360},\n",
        "                {'optional':'vegatable noodle','calories':210},\n",
        "            ],\n",
        "            \"lunch\": [\n",
        "                {\"monday\": \"Chicken salad sandwich on whole-wheat bread\", \"calories\": 400},\n",
        "                {'monday': 'Rava Upma', 'calories': 200},\n",
        "                {'monday': 'Poha', 'calories': 250},\n",
        "                {'tuesday': 'Masala Dosa', 'calories': 200},\n",
        "                {'tuesday': 'Paratha with Ghee', 'calories': 300},\n",
        "                {'tuesday': 'Banana Smoothie with Nuts', 'calories': 250},\n",
        "                {'wednesday': 'Brown Rice', 'calories': 215},\n",
        "                {'wednesday': 'Dal Curry(1 cup cooked) ', 'calories': 150},\n",
        "                {'wednesday': 'Chicken Curry (100g)', 'calories': 165},\n",
        "                {'thursday': 'Vegetable Stir-Fry (1 cup)', 'calories': 100},\n",
        "                {'thursday': ' Roti', 'calories': 160},\n",
        "                {'thursday': ' Curd (1 cup)', 'calories': 50},\n",
        "                {'friday': 'Salad with Olive Oil Dressing (1 cup)', 'calories': 50},\n",
        "                {'friday': ' Fruit (1 medium-sized)', 'calories': 80},\n",
        "                {'friday': 'Lassi', 'calories': 150},\n",
        "                {'sarurday': ' Fruit Salad', 'calories': 100},\n",
        "                {'sarurday': ' Paneer (Cottage Cheese) Bhurj ', 'calories':300-400},\n",
        "                {'sarurday': '  Dal Tadka', 'calories':200-250},\n",
        "                {'sunday': 'Jeera Rice ', 'calories':200-250},\n",
        "                {'sunday': 'Vegetable Raita', 'calories':100-150},\n",
        "                {'sunday': ' Dal Makhani', 'calories':300-350},\n",
        "                {'more_options': 'Paneer Tikka', 'calories':300-350},\n",
        "                {'more_options': 'Cucumber and Tomato Salad', 'calories':90},\n",
        "                {'more_options': 'Naan ', 'calories':200},\n",
        "                {'more_options': ' Mixed Vegetable Sabzi ', 'calories':300-400},\n",
        "                {'more_options': ' Avocado and Chickpea Salad', 'calories':300-400},\n",
        "                {'more_options': 'Mango Lass ', 'calories':200-250 },\n",
        "                {'more_options': ' Brown Rice Pulao with Vegetables', 'calories':400-550 },\n",
        "                {'more_options': ' Grilled Chicken ', 'calories':300},\n",
        "                {'more_options': ' Grilled paneer ', 'calories':250},\n",
        "                {'more_options': 'Mixed Vegetable Salad', 'calories':50-100},\n",
        "                {'more_options': 'Paneer Stir-fry (100g) ', 'calories':200},\n",
        "        ],\n",
        "            'dinner': [\n",
        "                {'monday': 'Paneer Tikka', 'calories': 300},\n",
        "                {'monday': 'Vegetable Biryani', 'calories': 400},\n",
        "                {'monday': 'Chicken Curry', 'calories': 350},\n",
        "                {'monday': 'Rajma', 'calories': 200},\n",
        "                {'tuesday': 'Mixed Vegetable Sabzi', 'calories': 150},\n",
        "                {'tuesday': 'Vegetable Pulao', 'calories': 300-450},\n",
        "                {'tuesday': 'Chickpea Curry (Chana Masala)', 'calories': 300-400},\n",
        "                {'tuesday': 'Cucumber Raita', 'calories': 100-150},\n",
        "                {'wednesday': 'Mixed Vegetable Salad', 'calories': 50-100},\n",
        "                {'wednesday': 'Roti ', 'calories': 50-80},\n",
        "                {'wednesday': 'Quinoa Salad ', 'calories':350-480},\n",
        "                {'wednesday': 'Spinach Stir-Fry', 'calories': 50-180},\n",
        "                {'thursday': 'Moong Dal Soup ', 'calories':140},\n",
        "                {'thursday': 'Sprout Salad ', 'calories': 100},\n",
        "                {'thursday': 'Paneer Butter Masala ', 'calories': 300},\n",
        "                {'thursday': 'chicken Butter Masala ', 'calories': 400-450},\n",
        "                {'friday': 'Vegetable Pulao ', 'calories': 250},\n",
        "                {'friday': 'chicken biryani ', 'calories': 500-600},\n",
        "                {'friday': 'Fruit Custard ', 'calories': 150},\n",
        "                {'friday': 'Grilled Chicken  ', 'calories': 350},\n",
        "                {'saturday': 'Grilled paneer ', 'calories': 280},\n",
        "                {'saturday': 'Grilled tofu', 'calories': 266},\n",
        "                {'saturday': 'Mixed Vegetable Salad', 'calories': 100-1500},\n",
        "                {'saturday': 'vegetable Biryani ', 'calories': 200},\n",
        "                {'sunday': 'Paneer Tikka', 'calories': 100-150},\n",
        "                {'sunday': 'Avocado and Chickpea Salad ', 'calories': 550},\n",
        "                {'sunday': 'Mango Lassi: ', 'calories': 200},\n",
        "                {'sunday': 'lassi', 'calories': 150},\n",
        "                {'more_options': 'Cucumber Raita ', 'calories': 50-100},\n",
        "                {'more_options': 'Brown Rice ', 'calories': 200-250},\n",
        "                {'more_options': 'Mixed Vegetable Stir-Fry ', 'calories': 100-150},\n",
        "                {'more_options': 'Yogurt', 'calories': 100-150},\n",
        "                {'more_options': 'Mixed Fruit Salad', 'calories': 50-100},\n",
        "                {'more_options': 'Lentil Soup ', 'calories': 150},\n",
        "                {'more_options': 'whole milk', 'calories': 100-150},\n",
        "                {'more_options': 'Palak Paneer', 'calories': 450-500},\n",
        "                {'more_options': 'Chana Masala ', 'calories': 270},\n",
        "                {'more_options': 'chicken tikka ', 'calories': 350},\n",
        "                {'more_options': 'Aloo Gobi ', 'calories': 150-280},\n",
        "                {'more_options': 'aloo baingan', 'calories': 145},\n",
        "                {'more_options': 'aloo matar', 'calories': 245},\n",
        "                {'more_options': ' aloo bhindi', 'calories': 205},\n",
        "                {'more_options': ' aloo palak', 'calories': 203},\n",
        "                {'more_options': ' aloo methi', 'calories': 243},\n",
        "                {'more_options': ' aloo  sabzi', 'calories':195},\n",
        "                {'more_options': ' bhindi aloo sabzi', 'calories': 185},\n",
        "                {'more_options': ' dahi bhindi sabzi', 'calories': 205},\n",
        "                {'more_options': 'stuffed bhindi sabzi', 'calories': 285},\n",
        "                {'more_options': ' bhindi sabzi', 'calories': 155},\n",
        "\n",
        "            ],\n",
        "            'snacks': [\n",
        "                {'monday': 'Paneer Tikka', 'calories': 300},\n",
        "                {'monday': 'Vegetable Cutlets', 'calories': 200},\n",
        "                {'monday': 'Fruit Chaat', 'calories': 100},\n",
        "                {'monday': 'Sprouts Salad', 'calories': 150},\n",
        "                {'monday': 'Peanut Chaat', 'calories': 200},\n",
        "                {'tuesday': 'Yogurt with Honey and Nuts', 'calories': 200},\n",
        "                {'tuesday': 'Paneer Sandwich', 'calories': 300-350},\n",
        "                {'tuesday': 'Chana Chaat', 'calories': 250-300},\n",
        "                {'tuesday': 'Mixed Nuts and Dried Fruits', 'calories': 200-250},\n",
        "                {'wednesday': 'Vegetable Upma', 'calories': 300-350},\n",
        "                {'wednesday': 'Fruit Yogurt Parfait', 'calories': 200-250},\n",
        "                {'wednesday': 'Almond Date Balls', 'calories': 150},\n",
        "                {'wednesday': 'Chickpea Chaat', 'calories': 150},\n",
        "                {'thursday': 'Banana Peanut Butter Sandwich', 'calories': 250},\n",
        "                {'thursday': 'Peanut Butter Banana Wrap', 'calories': 300},\n",
        "                {'thursday': 'Dhokla', 'calories': 200},\n",
        "                {'thursday': 'Cheese and Vegetable Stuffed Paratha', 'calories': 300},\n",
        "                {'friday': 'Almond and Date Smoothie', 'calories': 300-350},\n",
        "                {'friday': 'Mixed Nuts and Seeds', 'calories': 200},\n",
        "                {'friday': 'Banana and Peanut Butter', 'calories': 200-250},\n",
        "                {'friday': 'Greek Yogurt Parfait', 'calories': 250-300},\n",
        "                {'saturday': 'Peanut Butter Banana Sandwich:', 'calories': 250-300},\n",
        "                {'saturday': 'Sweet Potato Chaat', 'calories': 150-200},\n",
        "                {'saturday': 'Rajma Salad', 'calories': 200-250},\n",
        "                {'sunday': 'Avocado Toast', 'calories': 250-300},\n",
        "                {'sunday': 'Mango Lassi', 'calories': 200-250},\n",
        "                {'sunday': 'Yogurt with Fruit Salad', 'calories': 200},\n",
        "                {'sunday': 'Fruit and Nut Smoothie', 'calories': 250-300},\n",
        "                {'more_options': 'Makhana Snack', 'calories':150- 200},\n",
        "                {'more_options': 'Vegetable Sandwich', 'calories': 300},\n",
        "                {'more_options': 'Oats Upma', 'calories': 200},\n",
        "                {'more_options': 'Boiled Egg Chaat', 'calories': 150},\n",
        "           ],\n",
        "        },\n",
        "    elif bmi_category == \"normal weight\":\n",
        "        diet_plan ={\n",
        "            \"breakfast\": [\n",
        "                {'monday': 'Vegetable Dalia', 'calories': 200},\n",
        "                {'monday': 'Oats Upma', 'calories': 250},\n",
        "                {'monday': 'Whole Wheat Toast with Avocado', 'calories': 300},\n",
        "                {'monday': 'Vegetable Omelette', 'calories': 200},\n",
        "                {'tuesday': 'Fruit Salad with Yogurt', 'calories': 150},\n",
        "                {'tuesday': 'Masala Oats', 'calories': 150},\n",
        "                {'tuesday': 'Yogurt with Fresh Fruit', 'calories': 200},\n",
        "                {'tuesday': 'Green Tea', 'calories': 3},\n",
        "                {'wednesday': 'Vegetable Upma', 'calories': 250},\n",
        "                {'wednesday': 'Moong Dal Chilla', 'calories': 220},\n",
        "                {'wednesday': ' Poha', 'calories': 270},\n",
        "                {'wednesday': 'Vegetable Dalia ', 'calories': 264},\n",
        "                {'thursday': 'Idli with Sambar', 'calories': 330},\n",
        "                {'thursday': 'vegetable Omelette', 'calories': 250},\n",
        "                {'thursday': 'Whole Wheat Paratha with Curd', 'calories': 200},\n",
        "                {'thursday': 'Greek Yogurt Parfait', 'calories': 300},\n",
        "                {'friday': 'Whole Wheat Chapati with Paneer Bhurji ', 'calories': 300},\n",
        "                {'friday': 'dosa with Sambar', 'calories': 300},\n",
        "                {'friday': 'Oats Upma with Yogurt', 'calories': 360},\n",
        "                {'friday': 'Whole Grain Toast', 'calories': 160},\n",
        "                {'saturday': 'Greek Yogurt with Fresh Fruits', 'calories': 150},\n",
        "                {'sarurday': 'Sprouts Chaat', 'calories': 200},\n",
        "                {'saturday': 'Fresh Orange Juice', 'calories': 80},\n",
        "                {'saturday': 'juice', 'calories': 50-100},\n",
        "                {'sunday': 'Herbal Tea', 'calories': 0},\n",
        "                {'sunday': 'Fresh Fruits', 'calories': 50-100},\n",
        "                {'sunday': 'Buttermilk', 'calories': 50-100},\n",
        "                {'sunday': 'milk', 'calories': 150},\n",
        "            ],\n",
        "            'dinner': [\n",
        "                {'monday': 'Tandoori Chicken', 'calories': 250},\n",
        "                {'monday': 'Fish Curry', 'calories': 300},\n",
        "                {'monday': 'Bhindi Masala', 'calories': 150},\n",
        "                {'monday': 'Chana Masala', 'calories': 250},\n",
        "                {'monday': 'Palak Paneer', 'calories': 300},\n",
        "                {'tuesday': 'Brown Rice', 'calories': 200},\n",
        "                {'tuesday': 'Roti ', 'calories': 200},\n",
        "                {'tuesday': 'Dal', 'calories': 150},\n",
        "                {'tuesday': 'Sabzi ', 'calories':100},\n",
        "                {'tuesday': 'Brown Rice', 'calories': 210},\n",
        "                {'wednesday': 'Salad', 'calories': 50},\n",
        "                {'wednesday': 'Curd', 'calories': 150},\n",
        "                {'wednesday': 'Grilled Chicken Salad', 'calories': 345},\n",
        "                {'wednesday': 'Chickpea and Vegetable Curry with Brown Rice', 'calories': 370},\n",
        "                {'wednesday': 'Dal with Quinoa', 'calories': 270},\n",
        "                {'thursday': 'vegetable Stir-Fry with Tofu and Brown Rice', 'calories': 400},\n",
        "                {'thursday': 'Raita ', 'calories': 50},\n",
        "                {'thursday': 'Baked Chicken', 'calories':150},\n",
        "                {'thursday': 'Buttermilk:', 'calories':0},\n",
        "                {'thursday': 'water', 'calories': 0},\n",
        "                {'friday': 'Vegetable Biryani', 'calories': 250},\n",
        "                {'friday': 'chicken biryani', 'calories': 300-350},\n",
        "                {'friday': 'mutton biryani', 'calories': 350-400},\n",
        "                {'friday': 'Chana Masala', 'calories': 280},\n",
        "                {'friday': 'Cucumber Raita:', 'calories': 50},\n",
        "                {'saturday': 'Mixed Vegetable Salad', 'calories': 50-100},\n",
        "                {'saturday': 'Mint Chutney', 'calories': 20},\n",
        "                {'saturday': 'Aloo Gobi ', 'calories': 150-280},\n",
        "                {'saturday': 'aloo baingan', 'calories': 145},\n",
        "                {'saturday': 'aloo matar', 'calories': 245},\n",
        "                {'saturday': ' aloo bhindi', 'calories': 205},\n",
        "                {'sunday': ' aloo palak', 'calories': 203},\n",
        "                {'sunday': ' aloo methi', 'calories': 243},\n",
        "                {'sunday': ' aloo  sabzi', 'calories':195},\n",
        "                {'sunday': ' bhindi aloo sabzi', 'calories': 185},\n",
        "                {'more_options': ' dahi bhindi sabzi', 'calories': 205},\n",
        "                {'more_options': 'stuffed bhindi sabzi', 'calories': 285},\n",
        "                {'more_options': ' bhindi sabzi', 'calories': 155},\n",
        "                {'more_options': 'Grilled Paneer', 'calories': 150},\n",
        "                {'more_options': 'Grilled Chicken', 'calories': 150},\n",
        "                {'more_options': 'Vegetable Pulao', 'calories': 300-400},\n",
        "                {'more_options': 'chickn pulao', 'calories': 350-400},\n",
        "                {'more_options': 'Green Tea:', 'calories':3},\n",
        "                {'more_options': 'Rice', 'calories':100},\n",
        "\n",
        "            ],\n",
        "            'snacks': [\n",
        "                {'monday': 'Roasted Chickpeas', 'calories': 200},\n",
        "                {'monday': 'Cucumber Slices with Hummus', 'calories': 100},\n",
        "                {'monday': 'Dhokla', 'calories': 150},\n",
        "                {'monday': 'Roasted Makhana (Fox Nuts)', 'calories': 100},\n",
        "                {'monday': 'Roasted Peanuts with Jaggery', 'calories': 200},\n",
        "                {'tuesday': 'Sprouted Moong Chaat', 'calories': 150},\n",
        "                {'tuesday': 'vegetable Upma', 'calories': 200},\n",
        "                {'tuesday': 'Masala Oats', 'calories': 50-100},\n",
        "                {'tuesday': 'Greek Yogurt with Fruit', 'calories': 159},\n",
        "                {'tuesday': 'Baked Samosa with Mint Chutney', 'calories': 200},\n",
        "                {'wednesday': 'Cucumber Raita', 'calories':100},\n",
        "                {'wednesday': 'Chana Chaat', 'calories': 180},\n",
        "                {'wednesday': 'Baked Sweet Potato Chaat', 'calories': 150},\n",
        "                {'wednesday': 'Almond and Date Energy Bites:', 'calories': 120},\n",
        "                {'thursday': 'Roasted Chickpeas', 'calories': 150},\n",
        "                {'thursday': 'Fruit Chaat', 'calories': 100},\n",
        "                {'thursday': 'Moong Dal Chilla', 'calories':150},\n",
        "                {'thursday': 'Sprouts Salad', 'calories': 50-100},\n",
        "                {'friday': 'Masala Papad', 'calories':100},\n",
        "                {'friday': 'Yogurt with Berries', 'calories': 120-150},\n",
        "                {'friday': 'Vegetable Sticks with Hummus', 'calories': 50-100},\n",
        "                {'friday': 'Roasted Chana ', 'calories': 90-120},\n",
        "                {'saturday': 'Whole Grain Crackers with Cottage Cheese', 'calories': 120-150},\n",
        "                {'saturday': 'Makhana', 'calories': 50-100},\n",
        "                {'saturday': 'Vegetable Soup', 'calories': 50-70},\n",
        "                {'saturday': 'chicken soup', 'calories': 50},\n",
        "                {'sunday': 'Mixed Nuts ', 'calories': 180},\n",
        "                {'sunday': 'Greek Yogurt with Berries', 'calories':100},\n",
        "                {'sunday': 'Tea', 'calories': 50},\n",
        "                {'sunday': 'Dhokla', 'calories':100},\n",
        "                {'more_options': 'Whole Grain Toast with Peanut Butter ', 'calories': 150},\n",
        "                {'more_options': 'Tea with Biscuits', 'calories': 50-100},\n",
        "                {'more_options': 'Fruit Smoothie ', 'calories': 150},\n",
        "                {'more_options': 'Almonds and Walnuts Mix', 'calories': 150-200},\n",
        "                {'more_options': 'Whole Grain Toast with Avocado', 'calories': 120},\n",
        "                {'more_options': 'Buttermilk ', 'calories': 50-70},\n",
        "                {'more_options': 'milk ', 'calories': 150},\n",
        "                {'more_options': 'Whole Grain Poha', 'calories':200},\n",
        "                {'more_options': 'Paneer Tikka', 'calories': 100-150},\n",
        "                {'more_options': 'black tea', 'calories': 50},\n",
        "                {'more_options': 'Stir-Fried Tofu Cubes', 'calories': 160},\n",
        "                {'more_options': 'Bhel Pur', 'calories': 150},\n",
        "                {'more_options': 'Rice Cake with Peanut Butter', 'calories': 200},\n",
        "                {'more_options': '2 Boiled Egg Chaat', 'calories': 150},\n",
        "                {'more_options': 'Vegetable Sandwich', 'calories': 200},\n",
        "                {'more_options': 'Baked Sweet Potato Fries', 'calories': 120},\n",
        "                {'more_options': 'Whole Wheat Pita with Hummus', 'calories': 150}\n",
        "            ],\n",
        "        },\n",
        "    elif bmi_category == \"overweight\" :\n",
        "        diet_plan ={\n",
        "           \"breakfast\":[\n",
        "                {\"monday\": \"Ragi Dosa\", \"calories\": 150},\n",
        "                {\"tuesday\": \"Multigrain Porridge\", \"calories\": 200},\n",
        "                {'wednesday': 'Besan Cheela', 'calories': 150},\n",
        "                {'thursday': 'Vegetable Uttapam', 'calories': 200},\n",
        "                {'friday': 'Low-Fat Yogurt with Berries', 'calories': 150},\n",
        "                {'saturday': 'Moong Dal Khichdi', 'calories': 150},\n",
        "                {\"sunday\": \"Multigrain Porridge\", \"calories\": 200},\n",
        "            ],\n",
        "            'lunch_dinner': [\n",
        "                {'monday': 'Moong Dal Khichdi', 'calories': 150},\n",
        "                {'tuesday': 'Methi Matar Malai', 'calories': 200},\n",
        "                {'wednesday': 'Roti made from Multigrain Flour', 'calories': 150},\n",
        "                {'thursday': 'Cucumber Raita', 'calories': 100},\n",
        "                {'friday': 'Moong Dal Khichdi', 'calories': 150},\n",
        "                {'saturday': 'Moong Dal Khichdi', 'calories': 150},\n",
        "                {\"sunday\": \"Multigrain Porridge\", \"calories\": 200},\n",
        "            ]\n",
        "\n",
        "    }\n",
        "    return diet_plan\n",
        "weight = float(input(\"Enter your weight in kilograms: \"))\n",
        "height = float(input(\"Enter your height in meters: \"))\n",
        "\n",
        "diet_plan = generate_diet_plan(weight, height)\n",
        "print(diet_plan)"
      ],
      "metadata": {
        "id": "I3icGytliIWG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def get_nutritional_info(food_item):\n",
        "    nutrition_info = {\n",
        "      \"Apple\": {\"calories\": 52, \"protein\": 0.3, \"carbohydrate\": 14, \"fat\": 0.2},\n",
        "      \"Banana\": {\"calories\": 89, \"protein\": 1.1, \"carbohydrate\": 23, \"fat\": 0.3},\n",
        "      \"Orange\": {\"calories\": 47, \"protein\": 1, \"carbohydrate\": 12, \"fat\": 0.1},\n",
        "      \"Grapes\": {\"calories\": 69, \"protein\": 0.7, \"carbohydrate\": 18, \"fat\": 0.2},\n",
        "      \"Mango\": {\"calories\": 60, \"protein\": 0.8, \"carbohydrate\": 15, \"fat\": 0.4},\n",
        "      \"Pineapple\": {\"calories\": 50, \"protein\": 0.5, \"carbohydrate\": 13, \"fat\": 0.1},\n",
        "      \"Watermelon\": {\"calories\": 30, \"protein\": 0.6, \"carbohydrate\": 8, \"fat\": 0.2},\n",
        "      \"Papaya\": {\"calories\": 43, \"protein\": 0.5, \"carbohydrate\": 11, \"fat\": 0.3},\n",
        "      \"Strawberry\": {\"calories\": 33, \"protein\": 0.7, \"carbohydrate\": 8, \"fat\": 0.3},\n",
        "      \"Blueberry\": {\"calories\": 57, \"protein\": 0.7, \"carbohydrate\": 14, \"fat\": 0.3},\n",
        "      \"Kiwi\": {\"calories\": 61, \"protein\": 1.1, \"carbohydrate\": 15, \"fat\": 0.5},\n",
        "      \"Pomegranate\": {\"calories\": 83, \"protein\": 1.7, \"carbohydrate\": 18, \"fat\": 1.2},\n",
        "      \"Guava\": {\"calories\": 68, \"protein\": 2.6, \"carbohydrate\": 14, \"fat\": 0.9},\n",
        "      \"Avocado\": {\"calories\": 160, \"protein\": 2, \"carbohydrate\": 9, \"fat\": 15},\n",
        "      \"chicken\": {\"calories\": 239, \"protein\": 27, \"carbohydrates\": 0, \"fat\": 14},\n",
        "      \"Samosa\": {\"calories\": 320, \"protein\": 6, \"carbohydrate\": 25, \"fat\": 20},\n",
        "      \"Paneer Tikka\": {\"calories\": 260, \"protein\": 14, \"carbohydrate\": 6, \"fat\": 20},\n",
        "      \"Butter Chicken\": {\"calories\": 350, \"protein\": 20, \"carbohydrate\": 15, \"fat\": 25},\n",
        "      \"Chole Bhature\": {\"calories\": 450, \"protein\": 10, \"carbohydrate\": 40, \"fat\": 25},\n",
        "      \"Palak Paneer\": {\"calories\": 230, \"protein\": 12, \"carbohydrate\": 10, \"fat\": 15},\n",
        "      \"Masala Dosa\":{\"calories\": 160, \"protein\": 5, \"carbohydrate\": 30, \"fat\": 3},\n",
        "      \"Pav Bhaji\": {\"calories\": 350, \"protein\": 5, \"carbohydrate\": 55, \"fat\": 15},\n",
        "      \"Aloo Gobi\": {\"calories\": 150, \"protein\": 5, \"carbohydrate\": 20, \"fat\": 7},\n",
        "      \"Rajma Chawal\": {\"calories\": 300, \"protein\": 10, \"carbohydrate\": 50, \"fat\": 5},\n",
        "      \"Chicken Biryani\": {\"calories\": 400, \"protein\": 20, \"carbohydrate\": 45, \"fat\": 15},\n",
        "      \"Rasgulla\": {\"calories\": 150, \"protein\": 2, \"carbohydrate\": 30, \"fat\": 3},\n",
        "      \"Gulab Jamun\": {\"calories\": 250, \"protein\": 3, \"carbohydrate\": 35, \"fat\": 10},\n",
        "      \"Vada Pav\": {\"calories\": 300, \"protein\": 5, \"carbohydrate\": 40, \"fat\": 15},\n",
        "      \"Idli\": {\"calories\": 60, \"protein\": 2, \"carbohydrate\": 10, \"fat\": 1},\n",
        "      \"Medu Vada\": {\"calories\": 200, \"protein\": 3, \"carbohydrate\": 25, \"fat\": 10},\n",
        "      \"Aloo Paratha\": {\"calories\": 320, \"protein\": 8, \"carbohydrate\": 40, \"fat\": 15},\n",
        "      \"Fish Curry\": {\"calories\": 300, \"protein\": 20, \"carbohydrate\": 10, \"fat\": 20},\n",
        "      \"Pakora\": {\"calories\": 200, \"protein\": 4, \"carbohydrate\": 15, \"fat\": 12},\n",
        "      \"Bhindi Masala\": {\"calories\": 150, \"protein\": 3, \"carbohydrate\": 20, \"fat\": 8},\n",
        "      \"Kadhi Pakora\": {\"calories\": 250, \"protein\": 6, \"carbohydrate\": 30, \"fat\": 10},\n",
        "      \"Mango Lassi\": {\"calories\": 200, \"protein\": 5, \"carbohydrate\": 30, \"fat\": 5},\n",
        "      \"Chicken Curry\": {\"calories\": 280, \"protein\": 18, \"carbohydrate\": 12, \"fat\": 15},\n",
        "      \"Baingan Bharta\": {\"calories\": 180, \"protein\": 4, \"carbohydrate\": 20, \"fat\": 10},\n",
        "      \"Poha\": {\"calories\": 150, \"protein\": 3, \"carbohydrate\": 25, \"fat\": 5},\n",
        "      \"Raita\": {\"calories\": 100, \"protein\": 3, \"carbohydrate\": 10, \"fat\": 6},\n",
        "      \"Khichdi\": {\"calories\": 200, \"protein\": 5, \"carbohydrate\": 30, \"fat\": 8},\n",
        "      \"Chicken Tikka\": {\"calories\": 220, \"protein\": 25, \"carbohydrate\": 5, \"fat\": 12},\n",
        "      \"Puri Bhaji\": {\"calories\": 350, \"protein\": 8, \"carbohydrate\": 45, \"fat\": 15},\n",
        "      \"Dahi Vada\": {\"calories\": 180, \"protein\": 6, \"carbohydrate\": 20, \"fat\": 8},\n",
        "      \"Chicken Korma\": {\"calories\": 320, \"protein\": 18, \"carbohydrate\": 15, \"fat\": 22},\n",
        "      \"Mutton Rogan Josh\": {\"calories\": 380, \"protein\": 22, \"carbohydrate\": 10, \"fat\": 28},\n",
        "      \"Aloo Tikki\": {\"calories\": 150, \"protein\": 3, \"carbohydrate\": 20, \"fat\": 8},\n",
        "      \"Chicken 65\": {\"calories\": 280, \"protein\": 20, \"carbohydrate\": 15, \"fat\": 18},\n",
        "      \"Samosa Chaat\": {\"calories\": 300, \"protein\": 8, \"carbohydrate\": 35, \"fat\": 16},\n",
        "      \"Kheer\": {\"calories\": 250, \"protein\": 5, \"carbohydrate\": 40, \"fat\": 8},\n",
        "      \"Raj Kachori\": {\"calories\": 400, \"protein\": 10, \"carbohydrate\": 50, \"fat\": 20},\n",
        "      \"Papdi Chaat\": {\"calories\": 280, \"protein\": 6, \"carbohydrate\": 30, \"fat\": 14},\n",
        "      \"Bhel Puri\": {\"calories\": 200, \"protein\": 4, \"carbohydrate\": 25, \"fat\": 10},\n",
        "      \"Kadai Paneer\": {\"calories\": 280, \"protein\": 15, \"carbohydrate\": 10, \"fat\": 20},\n",
        "      \"Chicken Shawarma\": {\"calories\": 350, \"protein\": 25, \"carbohydrate\":20, \"fat\": 18},\n",
        "      \"Apricot\": {\"calories\": 48, \"protein\": 1.4, \"carbohydrate\": 11, \"fat\": 0.4},\n",
        "      \"Cherry\": {\"calories\": 50, \"protein\": 1, \"carbohydrate\": 12, \"fat\": 0.3},\n",
        "      \"Cantaloupe\": {\"calories\": 34, \"protein\": 0.8, \"carbohydrate\": 8, \"fat\": 0.2},\n",
        "      \"Honeydew Melon\": {\"calories\": 36, \"protein\": 0.5, \"carbohydrate\": 9, \"fat\": 0.1},\n",
        "      \"Raspberry\": {\"calories\": 52, \"protein\": 1.5, \"carbohydrate\": 12, \"fat\": 0.7},\n",
        "      \"Blackberry\": {\"calories\": 43, \"protein\": 1.4, \"carbohydrate\": 10, \"fat\": 0.5},\n",
        "      \"Cranberry\": {\"calories\": 46, \"protein\": 0.4, \"carbohydrate\": 12, \"fat\": 0.1},\n",
        "      \"Mango (ripe)\": {\"calories\": 60, \"protein\": 0.8, \"carbohydrate\": 15, \"fat\": 0.4},\n",
        "      \"Lemon\": {\"calories\": 29, \"protein\": 1.1, \"carbohydrate\": 9, \"fat\": 0.3},\n",
        "      \"Peach\": {\"calories\": 39, \"protein\": 0.9, \"carbohydrate\": 10, \"fat\": 0.3},\n",
        "      \"Pear\": {\"calories\": 57, \"protein\": 0.4, \"carbohydrate\": 15, \"fat\": 0.1},\n",
        "      \"Plum\": {\"calories\": 46, \"protein\": 0.7, \"carbohydrate\": 11, \"fat\": 0.3},\n",
        "      \"Grapefruit\": {\"calories\": 32, \"protein\": 0.6, \"carbohydrate\": 8, \"fat\": 0.1},\n",
        "      \"Lychee\": {\"calories\": 66, \"protein\": 0.8, \"carbohydrate\": 17, \"fat\": 0.4},\n",
        "    }\n",
        "\n",
        "    if food_item in nutrition_info:\n",
        "        result = {\n",
        "            \"food\": food_item.capitalize(),\n",
        "            \"calories\": nutrition_info[food_item][\"calories\"],\n",
        "            \"protein\": nutrition_info[food_item][\"protein\"],\n",
        "            \"carbohydrate\": nutrition_info[food_item][\"carbohydrate\"],\n",
        "            \"fat\": nutrition_info[food_item][\"fat\"],\n",
        "        }\n",
        "    else:\n",
        "        result = {\"error\": f\"Nutritional information not found for '{food_item}'.\"}\n",
        "\n",
        "    return result\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        " food_item = input(\"Enter a food item: \").capitalize()\n",
        " nutritional_info = get_nutritional_info(food_item)\n",
        "\n",
        "if \"error\" not in nutritional_info:\n",
        "        print(f\"\\nNutritional information for {nutritional_info['food']}:\")\n",
        "        print(f\"Calories: {nutritional_info['calories']} kcal\")\n",
        "        print(f\"Protein: {nutritional_info['protein']} g\")\n",
        "        print(f\"Carbohydrates: {nutritional_info['carbohydrate']} g\")\n",
        "        print(f\"Fat: {nutritional_info['fat']} g\")\n",
        "else:\n",
        "        print(nutritional_info[\"error\"])"
      ],
      "metadata": {
        "id": "rhVi5dk85_gb"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}