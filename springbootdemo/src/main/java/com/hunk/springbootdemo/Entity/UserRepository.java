package com.hunk.springbootdemo.Entity;

import org.springframework.data.jpa.repository.JpaRepository;
import com.hunk.springbootdemo.entity.User;

public interface UserRepository extends JpaRepository<User,Long> {
    User findByUserName(String userName);
}
