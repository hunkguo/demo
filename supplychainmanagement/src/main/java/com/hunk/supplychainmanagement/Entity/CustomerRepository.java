package com.hunk.supplychainmanagement.Entity;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.support.JpaRepositoryImplementation;
import com.hunk.supplychainmanagement.Entity.Customer;

public interface CustomerRepository extends JpaRepository<Customer, Integer> {
}