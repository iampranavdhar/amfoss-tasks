import 'package:flutter/material.dart';

class ScreenTwo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Stack(
      children:<Widget> [
       Positioned(
           top:30,
           left:20,
           right:20,
           child: Image.asset('assets/art-stairs.png')),
        Positioned(
          top: 480,
          left: 35,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget> [
              Text('Your Premium Cloud:' , style: TextStyle(fontSize: 25, fontWeight: FontWeight.w900, color: Colors.deepPurple),),
              SizedBox(width: 10,height: 10,),
              Text('Launch your next\ncampaign within minutes\nwith Cloud Campaign\nMonitor.', style: TextStyle(fontSize: 31,fontWeight: FontWeight.w900),)
            ]
        ),),
      ],

    );
  }
}
