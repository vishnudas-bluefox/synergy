import { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Authentication.module.css";

export default function SignUp({ setSignIn }) {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
  });
  let navigate = useNavigate();

  const handleSignUp = () => {
    createUserWithEmailAndPassword(auth, form.email, form.password)
      .then((userCred) => {
        updateProfile(auth.currentUser, {
          displayName: form.name,
        })
          .then(() => {
            navigate("/app"); //go to dashboard after auto-sign in
          })
          .catch((error) => {
            console.log(error);
          });
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
          e.preventDefault();
          handleSignUp();
        }}
      >
        <input
          type="text"
          placeholder="What should we call you?"
          required
          onChange={(e) => {
            setForm({ ...form, name: e.target.value });
          }}
        />
        <input
          type="email"
          placeholder="Email"
          required
          onChange={(e) => {
            setForm({ ...form, email: e.target.value });
          }}
        />
        <input
          type="password"
          placeholder="Password"
          required
          onChange={(e) => {
            setForm({ ...form, password: e.target.value });
          }}
        />
        <input type="submit" value="Sign Up" />
      </form>

      <p>
        Already have an account?{" "}
        <span
          onClick={() => setSignIn(true)}
        >
          {" "}
          Sign In
        </span>
      </p>
    </section>
  );
}
