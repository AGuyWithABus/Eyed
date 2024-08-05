# Android RAT APK Generator

This project automates the creation of an Android APK that records calls, takes screenshots, monitors device location, and more. The APK will also grant itself all necessary permissions and run in the background on device boot. The APK is controlled via commands sent from Termux over Firebase.

## Prerequisites

Ensure you have the following installed in Termux:

```sh
pkg update && pkg upgrade
pkg install python
pkg install openjdk-17
pkg install git

## Setup

1. Clone the Repository
