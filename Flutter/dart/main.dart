void main() {
  // Variables -------------------------------------------------
  var name = "Name";
  String name2 = "John";
  print("To jest var: $name");
  print("A to jest String: $name2");

  var x = 41;
  int otherX = 14;
  print("To jest Var: $x");
  print("To jest Integer: $otherX");

  double someDouble = 0.76;
  print("Dynamic: $someDouble");

  dynamic itsStrange = "Yes it is";
  print("Dynamic: $itsStrange");

  var something;
  print("Dynamic: $something");
  something = "Michael";
  print("Dynamic: $something");
  something = 41;
  print("Dynamic: $something");

  const String fullName = "John Elder";
  final String nickName = "J";
  print("Const: $fullName");
  print("Final: $nickName");

  bool hasName = true;
  print("Boolean: $hasName");

  // Data Types -------------------------------------------------
  // LISTS (Fixed Length (blah), Growable aka normal lists (chad))
  // starts notaion at 0 as usual
  var myList = [1, 2, 3];
  print("Lista: $myList");
  print("First (zero'th) element of the list: ${myList[0]}");

  myList[0] = 41;
  print("List after change: $myList");

  var emptyList = [];
  print("That's empty list: $emptyList");

  emptyList.add(17);
  print("Empty List after addition: $emptyList");

  emptyList.addAll([5, 3, 6]); //just pass another list
  print("Empty List after Add All addition: $emptyList");

  myList.insert(1, 17);
  print("Inserting value on specific position in list: $myList");

  myList.insertAll(1, [4, 3, 5]); //Again just pass another list
  print("insterAll function: $myList");

  var mixedList = [1, 2, 'Placki', 4.21];
  print("That's mixed list: $mixedList");

  mixedList.remove('Placki');
  print("After .remove('Placki'): $mixedList");

  mixedList.removeAt(0); //only index of the list
  print("Mixed list after .removeAt(0): $mixedList");

  //MAPS (Python Dictionary) Key-Value pairs
  var toppings = {"John": "Pepperoni", "Mary": "Cheese"};
  print("That's Map: $toppings");
  print(
      "That's value under keyword John (toppings['John']): ${toppings['John']}");

  print(
      "That's all values of a map (.values): $toppings.values"); //Something like 'property' property in Python

  print("All keys of a map (.keys): ${toppings.keys}"); //Same thing as .values

  toppings["Tim"] = "Sausage"; //adding to a map
  print(toppings);

  toppings.addAll({
    "Tina": "Bacon",
    "Steve": "Supreme"
  }); //like in list, here we pass an another Map
  print("Map after adding another map (.addAll({})): $toppings");

  toppings.remove("Steve");
  print("Map .remove('Steve'): $toppings");
  toppings.clear(); // Removes everything
  print("Toppings after .clear(): $toppings");
  // Loops --------------------------------------------------------------------------------------
  //FOR Loop
  var num = 5;
  for (var i = num; i >= 1; i--) {
    print(i);
  }

  //FOR IN Loop
  var names = ["john", "tina", "steve"];
  for (name in names) {
    print(name);
  }

  //WHILE Loop
  while (num >= 1) {
    print(num);
    num--;
  }

  // IF STATEMENTS ---------------------------------------------------------------------------------
  //IF | IF ELSE | IF ELSE IF
  // > < >= <= !=
  var num2 = 3;

  if (num2 == 5) {
    print("The number is 5");
  } else if (num2 == 3) {
    print("Number is 3!");
  } else {
    print("The number is not 5");
  }

  // Functions ---------------------------------------------------------------------------------
  myFunc() {
    print("Hello World!");
  }

  returnFunc() {
    return "Return Hello World!";
  }

  myFunc();

  var thing = returnFunc();
  print("Function returning value assigned to a variable: $thing");

  stringFunc(String name) {
    return "Hello $name";
  }

  String hello = stringFunc("Michael");
  print(hello);

  stringFunc2(String name1, [name2]) {
    return "Hello $name1 and $name2";
  }

  // func(name) - od po prostu parametr może być Null
  // func(String name) - Konkretna definicja parametru, nie może być Null i czymś innym
  //func([name]) - parametr opcjonalny. Domyślna wartość - Null
  //func({name}) - tzw keyword argument ale jednocześnie opcjonalny. Czyli przy deklaracji trzeba wpisac func(name: "cokolwiek"). I TU JEST DWUKROPEK!!!!

  var hello2 = stringFunc2('Siulek', 'Damian');
  print(hello2);

  var hello3 = stringFunc2('John');
  print(hello3);

  keywordFunc({name}) {
    print(name);
  }

  keywordFunc(name: "Michael");

  funcWithDefault(
      {name =
          'Friends'}) //W przypadku ustalanai wartości defaultowej dajemy znak "=".
  {
    print(name);
  }

  funcWithDefault(name: "Michael");
  funcWithDefault();

  // USER INPUT -----------------------------------------------------------------------------------
  // Totalnie Trzeba importować import 'dart:io';
  print("Enter Your Name: ");
  //var yourName = stdin.readLineSync();
  //print("Hello $yourName");

  //String otherName = stdin.readLineSync(); tu wyskoczy błąd ponieważ dokładnie zdefiniowane zmienne nie mogą być null
  //String? otherName = stdin
  //.readLineSync(); // Tutaj będzie git ponieważ "?" po typie zmiennej sprawia że ta zmienan może być Nullem pomimo zdefiniowanego typu
  //print("Hello $otherName");

  // CONVERT STRINGS, INTS adn DOUBLES -----------------------------------------------------------------------------------
  var a, b, c;
  a = 40;
  b = "1";
  c = a +
      int.parse(
          b); //generalnie to po prostu typ zmiennej na jaką chcemy zmienić i .parse()
  print("$a + $b = $c");

  var d, e, f;
  d = 40;
  e = "0.1";
  f = d +
      double.parse(
          e); //generalnie to po prostu typ zmiennej na jaką chcemy zmienić i .parse()
  print(f);

  var g, h, i;
  g = 40;
  h = '1';
  i = g.toString() +
      h; //konwersja czegoś na stringa wygląda trochę inaczej. Nazwa zmiennej.toString()
  print(i);
  // CONVERTING USER INPUT -----------------------------------------------------------------------
  //var numy = stdin.readLineSync();
  //print(numy + 10); - to wyrzuci error bo readLine zwraca "string"
  //var numy2 = int.parse(numy) + 10; - to też nie da rady ponieważ wartość może być nullem.
  //var numy3 = int.parse(numy ?? '0') to jest własciwa konwersja user inputu. to '0' jest wartością defaultowa w razie gdyby użytkownik nie podał niczego.

  // FIZZBUZZ -----------------------------------------------------------------------
  // int number1 = 1;
  // while (number1 <= 100) {
  //   if (number1 % 5 == 0 && number1 % 3 == 0) {
  //     print("$number1 FizzBuzz!");
  //   } else if (number1 % 3 == 0) {
  //     print("$number1 Fizz");
  //   } else if (number1 % 5 == 0) {
  //     print("$number1 Buzz");
  //   } else {
  //     print(number1);
  //   }

  //   number1++;
  // }

  // CLASSES -------------------------------------------------------------------------
  // Create Person Class
  Person p1 = Person("Michael", "Male", 29);
  p1.showPerson();
  print(p1.name);
  print(p1.age);
  print(p1.sex);

  Person p2 = Person("Mary", "Female", 30);
  p2.showPerson();
}

//STANDARD CLASS
class Person {
  //Pola Klasy. "?" - oznacza że mogą być Null
  String? name, sex;
  int? age;

  //Konstruktor
  Person(String name, sex, int age) {
    this.name = name;
    this.sex = sex;
    this.age = age;
  }

  //Nie trzeba mieć konstruktora w klasie.

  void nameSetter(String name) {
    this.name = name;
  }

  void sexSetter(String sex) {
    this.sex = sex;
  }

  void ageSetter(int age) {
    this.age = age;
  }

  //Metody
  void showPerson() {
    //Co ciekawe w opór nie trzeba przekazywać this do metody oraz wpisywac jej przed każdym polem. Mega dziwne
    print("Name = $name");
    print("Sex = $sex");
    print("Age = $age");
  }
}
