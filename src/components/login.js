import React, { useState } from 'react';
import axiosInstance from '../axios';
import { useHistory } from 'react-router-dom';
import '../styles/stylereglog.css';
import Header from './header';

export default function SignIn() {
	const history = useHistory();
	const initialFormData = Object.freeze({
		email: '',
		password: '',
	});

	const [formData, updateFormData] = useState(initialFormData);

	const handleChange = (e) => {
		updateFormData({
			...formData,
			[e.target.name]: e.target.value.trim(),
		});
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		console.log(formData);

		axiosInstance
			.post(`token/`, {
				email: formData.email,
				password: formData.password,
			})
			.then((res) => {
				localStorage.setItem('access_token', res.data.access);
				localStorage.setItem('refresh_token', res.data.refresh);
				localStorage.setItem('username', res.data.username);
				localStorage.setItem('user_img', res.data.user_img);
				localStorage.setItem('start_date', res.data.start_date);
				axiosInstance.defaults.headers['Authorization'] =
					'JWT ' + localStorage.getItem('access_token');
				history.push('/');
				//console.log(res);
				//console.log(res.data);
			});
	};


	return (
		<div className="all">
			<Header />
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
				<h2>Login Form</h2>
				<form>
					<div className="inputBox">
					<input type="text" placeholder="Email" onChange={handleChange} label="Email" name="email" id="email"  required />
					</div>
					<div className="inputBox">
					<input type="password" placeholder="Password" onChange={handleChange} label="Password" name="password" id="password"  required />
					</div>
					<div className="inputBox">
					<input type="submit" value="Login" onClick={handleSubmit} />
					</div>
					<p className="forget">Don't have an account?&nbsp;<a href="/register">Sign Up</a></p>
				</form>
				</div>
			</div>
			</div>
      	</section>
		  </div>
	);
}