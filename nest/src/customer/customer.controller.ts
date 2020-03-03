import { Controller,Get,Post,Param } from '@nestjs/common';

@Controller('customer')
export class CustomerController {
    @Get()
    findAll(): string{
        return "This is all customer.";
    }

    @Post('create')
    create(): string{
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
