import axiosInstance from '../axios';


const BASE_URL = 'http://localhost:8000/api/v1/comments/';

 class CommentService {

    getAnimeComments(id) {
        return axiosInstance.get(BASE_URL + id + "/");
    }    

} 
export default new CommentService();