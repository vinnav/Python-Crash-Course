def makeCar(manufacturer, model, **kwargs):
    kwargs["Manufacturer"] = manufacturer
    kwargs["Model"] = model
    return kwargs

car = makeCar("subaru", "outback", color="blue", tow_package=True)

print(car)