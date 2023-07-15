import * as Yup from "yup";
import { Formik, Form, Field, ErrorMessage } from "formik";
import { AiOutlineArrowRight } from "react-icons/ai";
import "./Login.css";
const SignUp = () => {
  const initialValues = {
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  };

  const validationSchema = Yup.object().shape({
    email: Yup.string()
      .email("Invalid email address")
      .required("Please enter your email"),
    password: Yup.string()
      .min(10)
      .required("Please enter your password")
      .matches(
        /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/,
        "Must contain at least 10 character and a special character"
      ),
  });

  const onSubmit = (values, { setSubmitting }) => {
    setTimeout(() => {
      console.log(values);
      sessionStorage.setItem("name", values.name);
      setSubmitting(false);
      window.open(process.env.REACT_APP_PORT, "_self");
    }, 1000);
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={onSubmit}
    >
      {({ isSubmitting }) => (
        <Form className="main-page">
          <div>Image</div>
          <div className="base">
            {/* <div> */}
            <h1>Welcome</h1>
            <Field
              type="email"
              name="email"
              placeholder="Email"
              className="block"
            />
            <ErrorMessage name="email" component="div" />
            <br />
            <Field
              type="password"
              name="password"
              placeholder="Password "
              className="block"
            />
            <ErrorMessage name="password" component="div" />
            <br />
            {/* </div> */}
            <button type="submit" disabled={isSubmitting} className="submit">
              <AiOutlineArrowRight color="rgba(255, 255, 255, 1)" size={30} />
            </button>
          </div>
        </Form>
      )}
    </Formik>
  );
};

export default SignUp;
