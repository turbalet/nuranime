import React from 'react';
import '../styles/stylee.css';

function Header() {
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
                    <li><a href="#">Manga</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Forum</a></li>
                    <li><a href="#">Contacts</a></li>
                    <li><a href="/login">login/profile</a></li>
                </ul>
                </nav>
            </header>
	);
}

export default Header;