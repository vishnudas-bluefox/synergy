import { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Authentication.module.css";

export default function SignIn({ setSignIn }) {
  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  let navigate = useNavigate();

  const handleSignIn = () => {
    signInWithEmailAndPassword(auth, form.email, form.password)
      .then((userCred) => {
        navigate("/app"); //go to dashboard after sign in
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <section
    className={styles.form}>
      <form
        
        onSubmit={(e) => {
          handleSignIn();
          e.preventDefault();
        }}
      >
        <input
          type="email"
          placeholder="email"
          required
          onChange={(e) => setForm({ ...form, email: e.target.value })}
        />
        <input
          type="password"
          placeholder="password"
          required
          onChange={(e) => setForm({ ...form, password: e.target.value })}
        />
        <input type="submit" value="Sign In" />
      </form>

      <p>
        Don't have an account?{" "}
        <span
          onClick={() => setSignIn(false)}
        >
          {" "}
          Sign Up
        </span>
      </p>
    </section>
  );
}
