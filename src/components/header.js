import React, { Component } from 'react';
import '../styles/stylee.css';


class Header extends Component {

    constructor(props) {
        super(props)
    
        this.state = {
             user: null
        }
    }
    
    componentDidMount() {
        if(localStorage.getItem("access_token")) {
            this.setState(state => {
                state.user = {
                    username: localStorage.getItem("username"),
                    user_img: localStorage.getItem("user_img"),
                    start_date: localStorage.getItem("start_date")
                };
            });
        }
    }

    isAuth() {
        
    }
    
    render(){
        return (
            <header>
                    <nav>
                    <ul>
                        <li>
                            <div>
                                <img src="logowide.png" alt="" />
                            </div>
                        </li>
                        <li className="logo"><a href="/">NurAnime </a></li>
                        <input className="searchbar" type="search" name="" value="" placeholder="search..." />
                        <li><a href="#">Anime</a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="#">Forum</a></li>
                        <li><a href="#">Contacts</a></li>
                        {
                        this.state.user != null ?
                            (<li><a href="/profile">{this.state.user.username}</a></li>)
                        :
                            (<li><a href="/login">login/profile</a></li>)
                        }
                    
                        
                    </ul>
                    </nav>
                </header>
        );
    }
}

export default Header;