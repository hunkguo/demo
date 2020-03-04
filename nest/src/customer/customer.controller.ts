import { Controller,Get,Post,Param,Body } from '@nestjs/common';
import {CreateCustomerDto} from './dto/create-customer.dto';

@Controller('customer')
export class CustomerController {
    @Get()
    findAll(): string{
        return "This is all customer.";
    }

    @Post('create')
    async create(@Body CreateCustomerDto:CreateCustomerDto): string{
        return "create success.";
    }
    @Get(':id')
    findOne(@Param() params): string{
        return 'This is a customer #${params.id}.';
    }

    @Get()
    edit(): string{
        return "edit a customer.";
    }

    @Post()
    save(): string{
        return "edit success."
    }


}
