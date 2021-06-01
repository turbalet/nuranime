import React, { useState } from 'react';
import axiosInstance from '../axios';
import { useHistory } from 'react-router-dom';
import Header from './header';

export default function SignUp() {
	const history = useHistory();
	const initialFormData = Object.freeze({
		email: '',
		username: '',
		password: '',
	});

	const [formData, updateFormData] = useState(initialFormData);

	const handleChange = (e) => {
		updateFormData({
			...formData,
			// Trimming any whitespace
			[e.target.name]: e.target.value.trim(),
		});
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		console.log(formData);

		axiosInstance
			.post(`user/create/`, {
				email: formData.email,
				username: formData.username,
				password: formData.password,
			})
			.then((res) => {
				history.push('/login');
				console.log(res);
				console.log(res.data);
			});
	};


	return (
		<div className="all">
			<Header></Header>
			<br></br>
			<br></br>
			<br></br>
			<br></br>
			<section>
				<div className="color" />
				<div className="color" />
				<div className="color" />
				<div className="box">
				<div className="square">
				</div>
				<div className="container">
					<div className="form">
					<h2>Register</h2>
					<form>
						<div className="inputBox">
						<input type="text" placeholder="Email" name="email" id="email" onChange={handleChange} />
						</div>
						<div className="inputBox">
						<input type="text" placeholder="Username" name="username" id="username" onChange={handleChange} />
						</div>
						<div className="inputBox">
						<input type="password" placeholder="Password" name="password" id="password" onChange={handleChange} />
						</div>
						<div className="inputBox">
						<input type="submit" id="reg" value="Register" onClick={handleSubmit} />
						</div>
						<p className="forget">Already have an account?&nbsp;<a href="/login">Log In</a></p>
					</form>
					</div>
				</div>
				</div>
		</section>
	  </div>
	);
}