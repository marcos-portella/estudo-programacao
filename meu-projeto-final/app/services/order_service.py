from typing import Optional, List, Dict, Any, cast
from mysql.connector.abstracts import MySQLConnectionAbstract
from app.models.orders import OrderUpdate, Order
from fastapi import HTTPException
from datetime import datetime


class OrderService:
    @staticmethod
    def list_orders(
        user_email: str,
        db: MySQLConnectionAbstract,
        customer_id: Optional[int] = None
    ) -> List[Dict[str, Any]]:

        cursor = db.cursor(dictionary=True)

        if customer_id:
            print(
                    f"Ação: Usuário {user_email} buscou os pedidos do cliente"
                    f"{customer_id}"
                )

        sql = """
            SELECT o.*, c.nome as customer_name
            FROM orders o
            INNER JOIN customers c ON o.customer_id = c.id
        """

        if customer_id:
            sql += " WHERE o.customer_id = %s"
            cursor.execute(sql, (customer_id,))
        else:
            cursor.execute(sql)

        results = cursor.fetchall()
        cursor.close()

        # Usamos o cast para converter o tipo genérico do MySQL para o nosso
        # tipo esperado
        return cast(List[Dict[str, Any]], results)

    @staticmethod
    def update_order(
        order_id: int, order_data: OrderUpdate, db: MySQLConnectionAbstract,
        user_email: str
    ):
        cursor = db.cursor()

        print(
            f"Ação: Usuário {user_email} atualizou o pedido {order_id}"
        )
        cursor.execute("SELECT id FROM orders WHERE id = %s", (order_id,))
        if not cursor.fetchone():
            cursor.close()
            raise HTTPException(
                status_code=404, detail="Pedido não encontrado"
            )

        # 2. Executar a atualização
        sql = """
            UPDATE orders
            SET description = %s, amount = %s
            WHERE id = %s
        """
        cursor.execute(
            sql, (order_data.description, order_data.amount, order_id)
        )

        db.commit()
        cursor.close()

        return {
            "message": f"Pedido {order_id} atualizado com sucesso!",
            "order_id": order_id,
            "updated_by": user_email
        }

    @staticmethod
    def create_order(
        order: Order, db: MySQLConnectionAbstract, user_email: str
    ):
        cursor = db.cursor()

        print(
                f"Ação: Usuário {user_email} criou um pedido"
            )

        cursor.execute(
            "SELECT id FROM customers WHERE id = %s", (order.customer_id,)
        )
        if not cursor.fetchone():
            cursor.close()
            raise HTTPException(
                status_code=404, detail="Cliente não encontrado"
            )

        # 2. Pegar a data e hora de AGORA no Python
        now = datetime.now()  # Ex: 2026-01-03 16:55:00

        # 3. Inserir incluindo a data
        sql = """
            INSERT INTO orders (description, amount, customer_id, created_at)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(
            sql, (order.description, order.amount, order.customer_id, now)
        )

        db.commit()
        new_id = cursor.lastrowid
        cursor.close()

        return {
            "order_ id": new_id,
            "message": "Pedido criado com sucesso!",
            "timestamp": now,
            "created_by": user_email
        }

    @staticmethod
    def get_order_stats(db: MySQLConnectionAbstract, user_email: str):
        cursor = db.cursor(dictionary=True)

        print(
                f"Ação: Usuário {user_email} buscou os status de vendas"
            )

        sql = """
            SELECT
                COUNT(*) as total_orders,
                SUM(amount) as total_revenue,
                AVG(amount) as average_order_value
            FROM orders
        """

        cursor.execute(sql)
        raw_data = cursor.fetchone()

        stats = cast(Optional[Dict[str, Any]], raw_data)
        cursor.close()

        if not stats:
            return {
                "total_orders": 0,
                "total_revenue": 0.0,
                "average_order_value": 0.0,
                "created_by": user_email
            }

        # Agora o Pylance sabe que stats['chave'] é válido
        return {
            "total_orders": stats['total_orders'] or 0,
            "total_revenue": float(stats['total_revenue'] or 0),
            "average_order_value": float(stats['average_order_value'] or 0),
            "geted_by": user_email
        }
