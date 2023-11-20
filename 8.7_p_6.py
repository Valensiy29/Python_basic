def swap_name_sites(site_name,site_count,site):
    for key,i in site.items():
        if isinstance(i, dict):
            next = swap_name_sites(site_name, site_count, i)
            if site[key] == 'title':
                next[key] = 'Куплю/продам', site_name
            elif 'h2' in next[key]:
                next['h2'] = 'У нас самая низкая цена на', site_name
                return site
    return site


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

site_count = int(input('введите сколько будет сайтов: '))

site_name = input('введите название продукта')
swap_name_sites(site_name,site_count,site)




