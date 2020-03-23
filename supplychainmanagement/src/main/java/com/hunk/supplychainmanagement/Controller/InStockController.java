package com.hunk.supplychainmanagement.Controller;

import com.hunk.supplychainmanagement.Entity.Product;
import com.hunk.supplychainmanagement.Entity.Purchase;
import com.hunk.supplychainmanagement.Entity.ProductRepository;
import com.hunk.supplychainmanagement.Entity.PurchaseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.math.BigDecimal;
import java.util.List;

@Controller
@RequestMapping("/instock")
public class InStockController {
    @Autowired
    private PurchaseRepository purchaseRepository;
    @Autowired
    private ProductRepository productRepository;

    @GetMapping("detail/{id}")
    public String index(@PathVariable("id") int id, Model model){
        //产品列表
        //产品进货数量 产品进货总价  产品进货平均价格  销售数量  销售总金额  退货数量  退货金额
        //存货数量=进货数量-销售数量+退货数量
        //利润= 销售总金额-存货数量*进货平均价格

        Product product=productRepository.getOne(id);
        List<Purchase> list=purchaseRepository.findByProduct(product);

        int purchaseCount = 0;
        BigDecimal purchaseSum=new BigDecimal(0);
        for (int i=0; i<list.size(); i++){
            Purchase purchase = list.get(i);
            purchaseCount++;
            purchaseSum=purchaseSum.add(purchase.getPrice());
        }

        model.addAttribute("purchasecount",purchaseCount);
        model.addAttribute("purchasesum",purchaseSum);
        model.addAttribute("product",product);
        return "instock/detail";
    }
}
