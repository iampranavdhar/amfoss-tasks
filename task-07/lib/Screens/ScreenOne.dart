import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';

class ScreenOne extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Stack(
        children: <Widget>[
          Positioned(
              top:70,
              left:0,
              child: Image.asset('assets/art-cloud.png'),),
          Positioned(
              top:10,
              bottom:5,
              child:Image.asset('assets/art-work.png',height: 100000,), ),
          Positioned(
            left: 27,
            bottom:90,
            child: Container(
            alignment: Alignment.bottomLeft,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.end,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                Text('Hello!',style: TextStyle(fontSize: 30, fontWeight: FontWeight.w800,color: Colors.deepPurple)),
                Text('Your own\nprivate Cloud is\none step away.', style:TextStyle(fontSize: 40,fontWeight: FontWeight.w900)),
                SizedBox(width: 10,height: 25,),
                Text('Swipe left to get started.',style:TextStyle(fontSize: 16,fontWeight: FontWeight.w900,color: Colors.deepPurple)),
              ],
            ),
          ),)

        ],
      ),
    );
  }
}
