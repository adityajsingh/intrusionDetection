import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String? longLat = "?";

  String? networkImage =
      "https://thumbs.dreamstime.com/b/emoticon-searching-mascot-vector-cartoon-illustration-emoticon-searching-mascot-vector-cartoon-illustration-original-113901025.jpg";

  FirebaseFirestore _firebaseFirestore = FirebaseFirestore.instance;

  void getImage() {
    _firebaseFirestore
        .collection("device")
        .doc("intruderImage")
        .snapshots()
        .listen((event) {
      setState(() {
        networkImage = event.data()!['image'];
      });
    });

    _firebaseFirestore
        .collection("device")
        .doc("gpsLocation")
        .snapshots()
        .listen((event) {
      setState(() {
        longLat = event.data()!["gpsLoc"];
      });
    });
  }

  @override
  void initState() {
    getImage();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Center(
          child: Text('Intrusion Detection App'),
        ),
      ),
      body: SafeArea(
        child: Container(
          width: MediaQuery.of(context).size.width,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              SizedBox(
                height: MediaQuery.of(context).size.height * 0.4,
                width: MediaQuery.of(context).size.width * 0.9,
                child: Image.network(networkImage!),
              ),
              const SizedBox(
                height: 20,
              ),
              Container(
                height: 60,
                width: MediaQuery.of(context).size.width * 0.9,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(8.0),
                  border: Border.all(width: 2),
                ),
                child: Center(
                  child: Text(
                    longLat!,
                    style: const TextStyle(
                      fontSize: 18.0,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
