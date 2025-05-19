import dns.resolver

def enumerate_subdomains(domain):
    # قائمة نطاقات فرعية شائعة (يمكنك توسيعها)
    common_subdomains = [
        'www', 'mail', 'ftp', 'help', 'blog', 'api', 'dev', 'test', 'secure', 'shop',
        'forum', 'news', 'docs', 'support', 'app', 'login', 'staging', 'beta'
    ]
    
    found_subdomains = []
    resolver = dns.resolver.Resolver()
    
    for subdomain in common_subdomains:
        try:
            # بناء النطاق الفرعي (مثل help.x.com)
            target = f"{subdomain}.{domain}"
            # استعلام عن سجل A
            answers = resolver.resolve(target, 'A')
            for answer in answers:
                found_subdomains.append(target)
                print(f"Found subdomain: {target}")
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            # النطاق الفرعي غير موجود
            continue
        except Exception as e:
            print(f"Error checking {target}: {e}")
    
    return found_subdomains

if __name__ == "__main__":
    domain = input("Enter the domain (e.g., x.com): ")
    subdomains = enumerate_subdomains(domain)
    print("\nFound subdomains:")
    for sub in subdomains:
        print(sub)