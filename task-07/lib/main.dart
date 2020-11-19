import 'package:dots_indicator/dots_indicator.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:myapp/Screens/ScreenOne.dart';
import 'package:myapp/Screens/ScreenTwo.dart';

void main() {
  runApp(MyApp());
}
class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: TabBar(),
    );
  }
}

class TabBar extends StatefulWidget {
  @override
  _TabBarState createState(){
    return _TabBarState();
  }
}

class _TabBarState extends State <TabBar> with SingleTickerProviderStateMixin {
  TabController _controller;
  double _selectedIndex = 0.0;

  @override
  void initState() {
    super.initState();
    _controller = TabController(length: 2, vsync: this);
    _controller.addListener(() {
      setState(() {
        _selectedIndex = _controller.index.toDouble();
      }
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        home:
        Scaffold(
          body:
          TabBarView(
            controller: _controller,
            children: [
              ScreenOne(),
              ScreenTwo(),
            ],),
          floatingActionButton: Stack(
            children: <Widget>[
              Positioned(
                left: 150,
                top: 50,
                child: new DotsIndicator(
                  dotsCount: 2,
                  position: _selectedIndex,
                  decorator: DotsDecorator(
                    color: Colors.deepPurple[200],
                    size: const Size.square(9.0),
                    activeSize: const Size(100.0, 11.0),
                    activeShape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5.0)),
                    activeColor: Colors.deepPurple[500]
                  ),
                ),
              ),
              Positioned(
                  left: 40,
                  right: 10,
                  bottom: 0,
                  child: RaisedButton(
                    padding: EdgeInsets.all(18),
                    onPressed: () {},
                    child: Text('Create an account',
                      style: TextStyle(fontSize: 25, color: Colors.white),),
                    color: Colors.deepPurple[500],
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.all(Radius.circular(20)),
                    ),
                  )
              ),
            ],
          ),
        ),
      ),
    );
  }
}