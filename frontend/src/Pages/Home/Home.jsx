import { useState} from "react";
import SignIn from "../Authentication/SignIn";
import SignUp from "../Authentication/SignUp";
import styles from "./Home.module.css";

export default function Home() {
  const [signIn, setSignIn] = useState(true);

  return (
      <section>
        <div className="styles.logo">
          <img src="../../../public/sy_logo.png" alt="logo" />
        </div>
        <div>
          {signIn ? (
            <SignIn setSignIn={setSignIn} />
          ) : (
            <SignUp setSignIn={setSignIn} />
          )}
        </div>
      </section>
  );
}