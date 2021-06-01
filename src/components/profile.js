import React, { Component } from 'react';
import '../styles/styleprofile.css';
import Header from './header';
import '../styles/stylee.css';
import axiosInstance from '../axios';



export default class profile extends Component {

    constructor(props) {
        super(props)
    
        this.state = {
             watching: []
        }
    }
    

    componentDidMount() {
        axiosInstance.get('http://127.0.0.1:8000/api/v1/profile/anime-list/1').
        then(res => {
            this.setState({
                watching: res.data
            });
        });
    }



    render() {
        return (
                <div className="obj1">
                    <Header></Header>
                    <br></br>
                <div className="containermain">
                    <div className="containerprofile">
                    <div className="imagebox">
                        <img src={localStorage.getItem("user_img")} alt="" />
                    </div>
                    <div className="dada">
                        <label htmlFor="myfile" className="chous">Change avatar</label>
                        <input type="file" className="my" id="myfile" name="myfile" multiple="multiple" />
                    </div>
                    <ul>
                        <li>Username: {localStorage.getItem("username")}</li>
                        <li>Email: user@email.com</li>
                        <li>Start date: {localStorage.getItem("start_date")}</li>
                        
                    </ul>
                    </div>
                    <div className="containerright">
                    <div className="typelist">
                        <ul>
                        <li>Watching</li>
                        <li>In Plans</li>
                        <li>Thrown</li>
                        </ul>
                    </div>
                    <div className="listresult">
                        <table id="titleunit">
                        <thead>
                            <tr>
                            <th>No:</th>
                            <th>Title</th>
                            <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        {this.state.watching.map(anime =>
                            
                            <tr>
                            <th>1</th>
                            <td>{anime.anime.title}</td>
                            <td>
                                <button type="button" name="button" />
                                <button className="btn"><i className="fa fa-trash" /></button>
                                <button type="button" name="button" />
                                <button type="button" name="button" />
                            </td>
                            </tr>
                            )}
                        </tbody>
                        </table>
                    </div>
                    </div>
                </div>
                </div>
        )
    }
}
