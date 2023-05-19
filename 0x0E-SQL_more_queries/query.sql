USE hbtn_0d_tvshows;
CREATE TABLE `tv_show_genres` (   
    `show_id` int(11) NOT NULL,  
    `genre_id` int(11) NOT NULL, 
    KEY  `show_id` (`show_id`),  
    KEY `genre_id` (`genre_id`),  
    CONSTRAINT `tv_show_genres_ibfk_1` FOREIGN KEY (`show_id`) REFERENCES `tv_shows` (`id`),  
    CONSTRAINT `tv_show_genres_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `tv_genres` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;