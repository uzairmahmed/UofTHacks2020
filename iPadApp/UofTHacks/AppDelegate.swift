//
//  AppDelegate.swift
//  UofTHacks
//
//  Created by Arjun Dureja on 2020-01-18.
//  Copyright © 2020 Arjun Dureja. All rights reserved.
//

import UIKit
import Firebase
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    var window: UIWindow?
    func application(_ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions:
        [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
      FirebaseApp.configure()
      return true
    }
}

