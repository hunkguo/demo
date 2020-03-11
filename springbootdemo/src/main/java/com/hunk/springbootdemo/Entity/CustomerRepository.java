package com.hunk.springbootdemo.Entity;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.support.JpaRepositoryImplementation;
import com.hunk.springbootdemo.Entity.Customer;

public interface CustomerRepository extends JpaRepository<Customer, Integer> {
}