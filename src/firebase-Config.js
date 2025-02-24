import { getAuth } from "firebase/auth";
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "@firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
//https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional 
const firebaseConfig = {
  apiKey: "AIzaSyAIQU-HMY98v6yB--tFddqKzCemgeKD1YI",
  authDomain: "proyectobiblioteca-adc3a.firebaseapp.com",
  projectId: "proyectobiblioteca-adc3a",
  storageBucket: "proyectobiblioteca-adc3a.firebasestorage.app",
  messagingSenderId: "351717461366",
  appId: "1:351717461366:web:74d18468b5a30943ac3e57",
  measurementId: "G-B4SGS30XF3"
};
// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth();
export const db = getFirestore(app); 