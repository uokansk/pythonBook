world = "бутылок"
for beer_num in range(99, 0, -1):
    if beer_num == 1:
        world = "бутылка"
    print(beer_num, world, "пива на стене")
    print(beer_num, world)
    print("возьми одну")
    print("пусти по кругу")
    if beer_num == 1:
        print("нет больше пива на стене")
    else:
        if beer_num >= 11 and beer_num <= 19:
            world = "бутылок"
        else:
            if beer_num % 10 == 1:
                world = "бутылка"
            elif beer_num % 10 in (2, 3, 4):
                world = "бутылки"
            else:
                world = "бутылок"
    print()
