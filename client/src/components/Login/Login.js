import * as Yup from "yup";
import { Formik, Form, Field, ErrorMessage } from "formik";

import { AiOutlineArrowRight } from "react-icons/ai";

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
      window.open("http://localhost:3000/", "_self");
    }, 1000);
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={onSubmit}
      className="box"
    >
      {({ isSubmitting }) => (
        <Form className="black">
          <div className="box">
            <div>
              <h1>Welcome</h1>
              <br />
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
              <button type="submit" disabled={isSubmitting} id="submit">
                <AiOutlineArrowRight />
              </button>
            </div>
          </div>
        </Form>
      )}
    </Formik>
  );
};

export default SignUp;
