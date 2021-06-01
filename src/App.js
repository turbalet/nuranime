import React, { Component, useEffect, useState } from 'react';
import axiosInstance from './axios';
import Header from './components/header';
import AnimeService from './services/AnimeService';
import Carousel from 'react-elastic-carousel'

const breakPoints = [
	{ width: 1, itemsToShow: 1 },
	{ width: 550, itemsToShow: 2 },
	{ width: 768, itemsToShow: 3 },
	{ width: 100, itemsToShow: 6 },
  ];


class App extends Component {


	constructor(props) {
		super(props)
	
		this.state = {
			 animes: [],
			 ongoings: []
		}

		this.getOngoings = this.getOngoings.bind(this);
		this.getAnonses = this.getAnonses.bind(this);
		this.getTop = this.getTop.bind(this);
		this.animeDetail = this.animeDetail.bind(this);
	}

	animeDetail(id) {
		this.props.history.push("/anime/" + id);
	}


	componentDidMount() {
		// axiosInstance.get('http://127.0.0.1:8000/api/v1/animes/top').then((res) => {
		// 	this.setState({ animes: res.data});
		// });
		// axiosInstance.get('http://127.0.0.1:8000/api/v1/animes?status=Онгоинг').then((res) => {
		// 	this.setState({ ongoings: res.data});
		// });
		Promise.all([
			axiosInstance.get('http://127.0.0.1:8000/api/v1/animes/top'),
			axiosInstance.get('http://127.0.0.1:8000/api/v1/animes/?status=Онгоинг'),
		]).then(([res1, res2]) =>{
			this.setState({
				animes: res1.data,
				ongoings: res2.data
			});
		});
	}

	
	getOngoings() {
		AnimeService.getOngoings().then(res => {
			this.setState({
				animes: res.data
			});
		});
	}

	getTop() {
		AnimeService.getTop().then(res => {
			this.setState({
				animes: res.data
			});
		});
	}

	getAnonses() {
		AnimeService.getAnonses().then(res => {
			this.setState({
				animes: res.data
			});
		});
	}

	render(){

		

		return (
			<div className="obj1">
				<Header />
				<div className="containerbig">
					<div className="containera">
						<div className="seasonTitle"><h3>Аниме текущего сезона</h3></div>
					<Carousel breakPoints={breakPoints}>
        				{this.state.ongoings.map(anime =>
						<div>
								<div className="box" onClick={() => {this.animeDetail(anime.id)}}>
							
								<div className="imgBx">
								<img src={anime.poster} alt="dsad" />
								</div>
								
								<div className="content">
								<h3><b>{anime.title}</b></h3>
									<p>{anime.release_date}</p>
								<p>Alot of battle like bokh BAKH BOM DJHHH!</p>
								</div>
							
								</div>
							
						</div>
						)}
					</Carousel>
					</div>
					<div className="containerb">
					<div className="navigation">
						<div className="categories">
						<ul>
							<li><a className="active" onClick={this.getTop}>Top-100</a></li>
							<li><a className="active" onClick={this.getOngoings}>Ongoing</a></li>
							<li><a className="active" onClick={this.getAnonses}>Anonses</a></li>
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
							this.state.animes.length != 0 ?

							(
								this.state.animes.map(
									anime =>
										<div className="box" id={anime.id} onClick={() => {this.animeDetail(anime.id)}}>
										
											<div className="imgBx">
												<img src={anime.poster} alt="dd" />
											</div>
											
										<div className="content">
											<p>{anime.title}</p>
										</div>
									
										</div>
								)
							) :

							(
								<div><h3 className="seasonTitle">Ближайших аниме-анонсов нет.</h3></div>
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
