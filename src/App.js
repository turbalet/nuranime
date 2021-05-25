import React, { Component, useEffect, useState } from 'react';
import axiosInstance from './axios';
import Header from './components/header';
import AnimeService from './services/AnimeService';

class App extends Component {


	constructor(props) {
		super(props)
	
		this.state = {
			 animes: []
		}
	}


	componentDidMount() {
		axiosInstance.get('http://127.0.0.1:8000/api/v1/animes/').then((res) => {
			this.setState({ animes: res.data});
		});
	}
	


	render(){
		return (
			<div className="obj1">
				<Header />
				<div className="containerbig">
					<div className="containera">
					<div className="box">
						<div className="imgBx">
						<img src="https://media-exp1.licdn.com/dms/image/C560BAQHMnA03XDdf3w/company-logo_200_200/0/1519855918965?e=2159024400&v=beta&t=CrP5Le1mWICRcaxIGNBuajHcHGFPuyNA5C8DI339lSk" alt="dsad" />
						</div>
						<div className="content">
						<h3>Jujutsu Kaisen</h3>
						<h4>2020-2021</h4>
						<h4>Alot of battle like bokh BAKH BOM DJHHH!</h4>
						</div>
					</div>
					<div className="box">
						<div className="imgBx">
						<img src="" alt="Hanako" />
						</div>
						<div className="content">
						<div className="icon">
							<img src alt="" />
						</div>
						<h3>Mushoku Tensei</h3>
						<h4>2020-2021</h4>
						<h4>A lot of wives for one MC!</h4>
						</div>
					</div>
					<div className="box">
						<div className="imgBx">
						<img src="titans.jfif" alt="" />
						</div>
						<div className="content">
						<div className="icon">
							<img src alt="" />
						</div>
						<h3>Attack on Titans</h3>
						<h4>2011-2022</h4>
						<h4>A lot psychical diseases after watching!</h4>
						</div>
					</div>
					<div className="box">
						<div className="imgBx">
						<img src="mushoku.jfif" alt="" />
						</div>
						<div className="content">
						<div className="icon">
							<img src alt="" />
						</div>
						<h3>Mushoku Tensei</h3>
						<h4>2020-2021</h4>
						<h4>A lot of wives for one MC!</h4>
						</div>
					</div>
					<div className="box">
						<div className="imgBx">
						<img src="mushoku.jfif" alt="" />
						</div>
						<div className="content">
						<div className="icon">
							<img src alt="" />
						</div>
						<h3>Mushoku Tensei</h3>
						<h4>2020-2021</h4>
						<h4>A lot of wives for one MC!</h4>
						</div>
					</div>
					</div>
					<div className="containerb">
					<div className="navigation">
						<div className="categories">
						<ul>
							<li><a href="#" className="active">Top-100</a></li>
							<li><a href="#" className="active">Ongoing</a></li>
							<li><a href="#" className="active">Anonses</a></li>
						</ul>
						</div>
						<div className="social">
						<ul>
							<li><a href="#" className="active">inst</a></li>
							<li><a href="#" className="active">telegr</a></li>
							<li><a href="#" className="active">vkont</a></li>
						</ul>
						</div>
					</div>
					<div className="explore">
						{
							this.state.animes.map(
								anime =>
									<div className="box">
									<div className="imgBx">
										<img src={anime.poster} alt="dd" />
									</div>
									<div className="content">
										<h3>{anime.title}</h3>
										<h4>{anime.release_date}</h4>
									</div>
									</div>
							)
						}
					</div>
					</div>
			</div>
		</div>
		);
	}
}

export default App;
