from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import NetworkLog, IPSRule, Alert


class AddLog(APIView):
    def post(self, request):
        client = request.data["client"]
        server = request.data["server"]
        port = request.data["port"]
        protocol = request.data["protocol"]
        tls = request.data["tls"]
        size = request.data["size"]
        action = "No Action"
        create_log = False

        try:
            rule = IPSRule.objects.get(address__endswith=server)
            if rule is not None:
                create_log = True
                if rule.rule_type == "tls" and not tls:
                    action = rule.action
                elif rule.rule_type == "address":
                    action = rule.action
                elif rule.rule_type == "proto" and protocol == rule.pattern:
                    action = rule.action
                elif rule.rule_type == "size" and size > rule.threshold:
                    action = rule.action
                elif rule.rule_type == "port" and str(port) == rule.pattern:
                    action = rule.action

        except IPSRule.DoesNotExist:
            pass

        if create_log:
            new_log = NetworkLog(
                client=client,
                server=server,
                port=port,
                protocol=protocol,
                tls=tls,
                size=size,
                action=action
            )

            new_log.save()

        if action == "alert":
            new_alert = Alert(log=new_log)
            new_alert.save()

        return Response({"status": {"code": 0, "message": "success"}},
                        status.HTTP_200_OK) if action == "No Action" else Response(
            {"status": {"code": 1, "message": action}}, status.HTTP_200_OK)
