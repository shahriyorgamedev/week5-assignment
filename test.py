


def calculate_tickets_value(ticket_type, tickets_resolved, priority_level):
    price = 0
    if ticket_type == 'technical':
        if priority_level == 'low':
            price = 20
        elif priority_level == 'medium':
            price = 35
        elif priority_level == 'high':
            price = 55
    elif ticket_type == 'billing':
        if priority_level == 'low':
            price = 15
        elif priority_level == 'medium':
            price = 25
        elif priority_level == 'high':
            price = 40
    elif ticket_type == 'general':
        if priority_level == 'low':
            price = 10
        elif priority_level == 'medium':
            price = 18
        elif priority_level == 'high':
            price = 28

    total_value = tickets_resolved * price
    return total_value



def calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets):
    expected_tickets = 1000 + (agent_quarters * 100)
    ticket_capacity = expected_tickets - baseline_tickets
    efficiency = (resolved_tickets - baseline_tickets) / ticket_capacity * 100
    return round(efficiency, 1)



def determine_performance_level(efficiency_percent):
    if efficiency_percent < 50:
        return "Developing Level"
    elif 50 <= efficiency_percent <= 60:
        return "Competent Level"
    elif 60 < efficiency_percent <= 70:
        return "Proficient Level"
    elif 70 < efficiency_percent <= 85:
        return "Advanced Level"
    else:
        return "Expert Level"



def calculate_performance_bonus(value, tickets, level_multiplier):
    base_bonus = value * 0.05 + tickets * 2
    multiplier = 0

    if level_multiplier == "Developing Level":
        multiplier = 0.5
    elif level_multiplier == "Competent Level":
        multiplier = 1.0
    elif level_multiplier == "Proficient Level":
        multiplier = 1.2
    elif level_multiplier == "Advanced Level":
        multiplier = 1.5
    elif level_multiplier == "Expert Level":
        multiplier = 1.8

    final_bonus = base_bonus * multiplier
    return round(final_bonus, 1)



def needs_additional_training(service_weeks, total_tickets, avg_efficiency):
    if service_weeks >= 6 and avg_efficiency < 50:
        return True
    elif total_tickets < 100 and avg_efficiency < 60:
        return True
    elif service_weeks >= 4 and avg_efficiency < 40:
        return True
    else:
        return False



def generate_quality_report(agent_name, ticket_type, tickets, priority_level, agent_quarters, baseline_tickets, resolved_tickets, service_weeks):
    ticket_value = calculate_tickets_value(ticket_type, tickets, priority_level)
    efficiency = calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets)
    performance_level = determine_performance_level(efficiency)
    performance_bonus = calculate_performance_bonus(ticket_value, tickets, performance_level)
    training_needed = needs_additional_training(service_weeks, tickets, efficiency)

    print("CUSTOMER SERVICE QUALITY MONITOR")
    print("========================================")
    print(f"Quality Report for: {agent_name}")
    print("----------------------------------------")
    print(f"Ticket Type: {ticket_type}")
    print(f"Tickets Resolved: {tickets}")
    print(f"Priority Level: {priority_level}")
    print(f"Tickets Value: ${ticket_value}")
    print("Efficiency Analysis:")
    print(f"Experience: {agent_quarters} quarters, Baseline: {baseline_tickets}, Resolved Tickets: {resolved_tickets}")
    print(f"Efficiency: {efficiency}%")
    print(f"Performance Level: {performance_level}")
    print(f"Performance Bonus: ${performance_bonus}")
    print(f"Service Weeks: {service_weeks}")
    print(f"Additional Training Needed: {'Yes' if training_needed else 'No'}\n")

generate_quality_report("Harper", "technical", 45, "high", agent_quarters=3, baseline_tickets=800, resolved_tickets=1150, service_weeks=3)
generate_quality_report("Indigo", "billing", 60, "medium", agent_quarters=5, baseline_tickets=900, resolved_tickets=1300, service_weeks=5)
generate_quality_report("Jesse", "general", 30, "low", agent_quarters=8, baseline_tickets=850, resolved_tickets=950, service_weeks=7)