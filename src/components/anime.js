import React, { Component } from 'react'
import '../styles/stylee.css';
import '../styles/titlestyle.css';
import Header from './header';
import axiosInstance from '../axios';
import CommentService from '../services/CommentService';

export default class anime extends Component {



    constructor(props) {
        super(props)
    


        this.state = {
             anime: {},
             genres: [],
             studio: {},
             date: "",
             comments: []
        }
    }
    

    componentDidMount() {
        axiosInstance.get('http://127.0.0.1:8000/api/v1/anime/detail/' + window.location.pathname.split('/')[2] + '/')
        .then(res => {
            this.setState({
                anime: res.data,
                genres: res.data.genres,
                studio: res.data.studio
            });
            this.setState({
                date: this.state.anime.release_date.split("-")[0]
            });
            console.log(this.state.date);
            console.log(res.data);
            console.log(res.data.studio);
            console.log(res.data.genres);
        });

        CommentService.getAnimeComments(window.location.pathname.split('/')[2]).
        then(res => {
            this.setState({
                comments: res.data
            });
        });
    }


    render() {
        return (
            <div className="obj1">
                <Header></Header>
                <div className="contmain">
                <div className="contleft">
                    <div className="box">
                    <div className="imgBx">
                        <img src={this.state.anime.poster} alt="" />
                    </div>
                    </div>
                    <div className="shortinfo">
                    <h3>{this.state.date}</h3>
                    <ul>
                        <li>
                        <b>Genre:</b> 
                        {
                            this.state.genres.map(genre => <div><a href="/genre" className="genre">{genre.genre_name}</a><br/></div>)
                        }
                        </li>
                        <li>
                        <b>Producer:</b> <a href="#"> Makananmi Ikadaki</a>
                        </li>
                        <li>
                        <b>Author: </b> <a href="#"> Chikamaki Arigato Kosaimas </a>
                        </li>
                        <li>
                        <b>Studio: </b> <a href="#">{this.state.studio.studio_name}</a>
                        </li>
                    </ul>
                    </div>
                </div>
                <div className="contright">
                    <h3>{this.state.anime.title}</h3>
                    <div className="descriptiontext">
                    <p>{this.state.anime.description}</p>
                    </div>
                    <div className="videocase">
                    <figure id="video_player">
                        <figcaption>
                        <ul>
                            <li><a href="video1.mp4"><div className="chaterbitton"> <h4>1</h4> </div> </a></li>
                            <li><a href="video2.mp4"><div className="chaterbitton"> <h4>2</h4> </div> </a></li>
                            <li><a href="video3.mp4"><div className="chaterbitton"> <h4>3</h4> </div> </a></li>
                            <li><a href="video1.mp4"><div className="chaterbitton"> <h4>4</h4> </div> </a></li>
                            <li><a href="video1.mp4"><div className="chaterbitton"> <h4>5</h4> </div> </a></li>
                            <li><a href="video1.mp4"><div className="chaterbitton"> <h4>6</h4> </div> </a></li>
                        </ul>
                        </figcaption>
                        <video poster="poster.jpg" controls width="800px" height="400px">
                        <source src="video1.mp4" type="video/mp4" />
                        <source src="video1.webm" type="video/webm" />
                        </video>
                    </figure>
                    </div>
                </div>
                </div>
                <div className="commentsection">
                <div className="comment-thread">
                    {/* Comment 1 start */}
                    <details open className="comment" id="comment-1">
                    <a href="#comment-1" className="comment-border-link">
                        <span className="sr-only">Jump to comment-1</span>
                    </a>
                    {this.state.comments.map(
							comment =>
                    <div>
                    <summary>
                        <div className="comment-heading">
                        <div className="comment-voting">
                            <button type="button">
                            <span aria-hidden="true">✛</span>
                            <span className="sr-only">Vote up</span>
                            </button>
                            <button type="button">
                            <span aria-hidden="true">⚊</span>
                            <span className="sr-only">Vote down</span>
                            </button>
                        </div>
                        <div className="comment-info">
                            <a href="#" className="comment-author">{comment.user.username}</a>
                            <p className="m-0">
                            {comment.commented_date}
                            </p>
                        </div>
                        </div>
                    </summary>
                    <div className="comment-body">
    
                               
                                    <p>
                                    {comment.message}
                                    </p>
                                    <button type="button" data-toggle="reply-form" data-target="comment-1-reply-form">Reply</button>
                                    <button type="button">Flag</button>
                                    <form method="POST" className="reply-form d-none" id="comment-1-reply-form">
                                    <textarea placeholder="Reply to comment" rows={4} defaultValue={""} />
                                    <button type="submit">Submit</button>
                                    <button type="button" data-toggle="reply-form" data-target="comment-1-reply-form">Cancel</button>
                                    </form>
                              


                    </div>
                    
                    </div>
                     )}
                    </details>
                    {/* Comment 1 end */}
                </div>
                   
                </div>
                
            </div>
            
        )
    }
}
