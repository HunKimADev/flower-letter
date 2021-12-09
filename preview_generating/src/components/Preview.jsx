import React,{useState} from 'react';
import styled from 'styled-components';
import PreviewImageUrls from './PreviewImageUrls';

const PreviewFrame = styled.div`
    width: 300px;
    position: relative;

    .cover{
        width: 300px;
        position: relative;
    }
    .flower{
        position: absolute;
        height: 240px;
        left:40px;
        bottom: 30px;
    }
    .label{
        position: absolute;
        width:300px;
        left:0;
        bottom:0;
    }
    .title{
        position: absolute;
        top: 80px;
        right: 30px;
        font-family: ${props => props.font};
        font-size: 1.8rem;
        color: ${props => props.textColor};
    }

`;

function Preview () {
    //여기부터
    const text = "너에게 쓰는 편지";
    const [currentCover, setCurrentCover] = useState(PreviewImageUrls.covers.white);
    const flowers = PreviewImageUrls.flowers;
    const currentFont = 'sungsil';
    //여기까지 리덕스로 관리
    return(
        <PreviewFrame textColor={currentCover.textColor} font={currentFont}>
            <img className="cover" src={currentCover.cover}/>
            <img className="flower" src={flowers.rose} />
            <img className="label" src={currentCover.label}/>
            <div className="title">{text}</div>
        </PreviewFrame>);
}


export default Preview;