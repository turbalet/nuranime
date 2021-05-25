import React, { Component } from 'react'
import '../styles/stylee.css';
import '../styles/titlestyle.css';
import Header from './header';


export default class anime extends Component {
    render() {
        return (
            <div className="obj1">
                <Header></Header>
                <div className="contmain">
                <div className="contleft">
                    <div className="box">
                    <div className="imgBx">
                        <img src="mushoku.jfif" alt="" />
                    </div>
                    </div>
                    <div className="shortinfo">
                    <h3>2020-2021</h3>
                    <ul>
                        <li>
                        <b>Genre:</b> <a href="#"> Comedy,Isecai,Imba MC</a>
                        </li>
                        <li>
                        <b>Ozvuchka:</b> <a href="#"> Russian,English</a>
                        </li>
                        <li>
                        <b>Producer:</b> <a href="#"> Makananmi Ikadaki</a>
                        </li>
                        <li>
                        <b>Reference manga:</b> <a href="#"> Mushoku tensei alternative world from start reincarnation of workless</a>
                        </li>
                        <li>
                        <b>Author: </b> <a href="#"> Chikamaki Arigato Kosaimas </a>
                        </li>
                        <li>
                        <b>Studio: </b> <a href="#"> Kampaii </a>
                        </li>
                    </ul>
                    </div>
                </div>
                <div className="contright">
                    <h3>Title Name</h3>
                    <div className="descriptiontext">
                    <p>   Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                        , quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                        nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                        sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
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
                            <a href="#" className="comment-author">someguy14</a>
                            <p className="m-0">
                            22 points • 4 days ago
                            </p>
                        </div>
                        </div>
                    </summary>
                    <div className="comment-body">
                        <p>
                        This is really great! I fully agree with what you wrote, and this is sure to help me out in the future. Thank you for posting this.
                        </p>
                        <button type="button" data-toggle="reply-form" data-target="comment-1-reply-form">Reply</button>
                        <button type="button">Flag</button>
                        {/* Reply form start */}
                        <form method="POST" className="reply-form d-none" id="comment-1-reply-form">
                        <textarea placeholder="Reply to comment" rows={4} defaultValue={""} />
                        <button type="submit">Submit</button>
                        <button type="button" data-toggle="reply-form" data-target="comment-1-reply-form">Cancel</button>
                        </form>
                        {/* Reply form end */}
                    </div>
                    <div className="replies">
                        {/* Comment 2 start */}
                        <details open className="comment" id="comment-2">
                        <a href="#comment-2" className="comment-border-link">
                            <span className="sr-only">Jump to comment-2</span>
                        </a>
                        <summary>
                            <div className="comment-heading">
                            <div className="comment-voting">
                                <button type="button">
                                <span aria-hidden="true">▲</span>
                                <span className="sr-only">Vote up</span>
                                </button>
                                <button type="button">
                                <span aria-hidden="true">▼</span>
                                <span className="sr-only">Vote down</span>
                                </button>
                            </div>
                            <div className="comment-info">
                                <a href="#" className="comment-author">randomperson81</a>
                                <p className="m-0">
                                4 points • 3 days ago
                                </p>
                            </div>
                            </div>
                        </summary>
                        <div className="comment-body">
                            <p>
                            Took the words right out of my mouth!
                            </p>
                            <button type="button" data-toggle="reply-form" data-target="comment-2-reply-form">Reply</button>
                            <button type="button">Flag</button>
                            {/* Reply form start */}
                            <form method="POST" className="reply-form d-none" id="comment-2-reply-form">
                            <textarea placeholder="Reply to comment" rows={4} defaultValue={""} />
                            <button type="submit">Submit</button>
                            <button type="button" data-toggle="reply-form" data-target="comment-2-reply-form">Cancel</button>
                            </form>
                            {/* Reply form end */}
                        </div>
                        </details>
                        {/* Comment 2 end */}
                        <a href="#load-more">Load more replies</a>
                    </div>
                    </details>
                    {/* Comment 1 end */}
                </div>
                </div>
                
            </div>
            
        )
    }
}
