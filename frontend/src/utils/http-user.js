import axios from 'axios'

export default axios.create({
    // baseURL: 'http://j3a505.p.ssafy.io:8000/api/accounts/',
    baseURL: 'http://ec2-3-35-37-204.ap-northeast-2.compute.amazonaws.com:8000/api/accounts/',
})
