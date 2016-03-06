import math

X_COORD = 0
Y_COORD = 1
Z_COORD = 2


class Point:
    """A point with K coordinates.

    While the point can have the desired number of dimensions, the first three are usually called
    X_COORD, Y_COORD and Z_COORD and they are at position 0, 1 and 2 of the coordinate list.
    """

    def __init__(self, coordList):
        """A K dimensional point from a list with K dimensions.

        :type coordList: list
        :param coordList: a list with all the coordinates for the point
        """
        for coord in coordList:
            if math.isnan(coord) : raise ValueError("Coordinates cannot be NaN!")
            if math.isinf(coord) : raise ValueError("Coordinates cannot be Inf!")

        self.coords = coordList[:]

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return self.coords != other.coords

    def dimensions(self):
        return len(self.coords)

    def squaredDistanceTo(self, other):
        """The squared distance from this point to the other given point.

        :type other: Point
        :param other: another point to calculate the squared distance to.
        :return: the squared distance from this point and the other point given
        """
        sq = 0
        for idx, coord in enumerate(self.coords):
            dc = coord - other.coords[idx]
            sq += dc * dc

        return sq


    def distanceTo(self, other):
        """The distance from this point to the other given point.

        :type other: Point
        :param other: another point to calculate the distance to.
        :return: the distance from this point and the other point given
        """
        return math.sqrt(self.squaredDistanceTo(other))


class Node:
    """A node of the K dimenional tree.
    """
    def __init__(self, point, recHV = None):
        """Create a node with the give point.

        :type point: Point
        :param point: The point for this node.
        """
        self.point = point
        self.recHV = recHV
        self.left = None
        self.right = None


class KdTree:
    """A set of points, internally represented as a kdTree for fast proximity search.
    """

    _root = None
    _count = 0
    _dim = 2

    def __init__(self, dimensions = 2):
        self._dim = dimensions

    def isEmpty(self):
        return self._root == None

    def size(self):
        return self._count

    def insert(self, point):
        """
        Add the point to the set (if it is not already in the set)

        :param point: the point to add to the set
        :type point: Point
        """
        self._root = self.insertRec(self._root, point, 0)

    def insertRec(self, node, point, level):
        if node == None:
            self._count += 1
            node = Node(point)
            return node

        ldist = self.leveled_distance(node, point, level)

        if ldist < 0 :
            node.left = self.insertRec(node.left, point, level + 1)
        elif ldist != 0 or node.point != point:
            node.right = self.insertRec(node.right, point, level + 1)
        return node


    def _dimByLevel(self, level):
        return level % self._dim

    def leveled_distance(self, node, point, level):
        """
        Compares two points (the node's point and the given point) on a coordinate based on the node level,
         reporting if the point coordinate is smaller, equal or bigger than the node's point coordinate.

        :param node: the current node
        :type node: Node
        :param point: the point to add
        :type point: Point
        :param level: the level of the node
        :type level: int
        :return: a negative integer, zero, or a positive integer as the point coordinate is
        less than, equal to, or greater than the node's point coordinate determined by the level.
        :rtype: int
        """

        dim = self._dimByLevel(level)
        return point.coords[dim] - node.point.coords[dim]

    def search(self, point):
        """

        :param point: the point to look for
        :type point: Point
        :return: the point, if found, or None, if not found.
        """
        node = self._searchNode(point, self._root, 0)
        if node != None:
            return node.point
        else:
            return None

    def _searchNode(self, point, node, level):
        if node == None:
            return None
        elif node.point == point:
            return node

        ldist = self.leveled_distance(node, point, level)

        if ldist < 0 :
            found = self._searchNode(point, node.left, level + 1)
        else:
            found = self._searchNode(point, node.right, level + 1)

        return found

    def nearest(self, point):
        """
        the nearest neighbor in the set to point p; None if the set is empty.

        :param point: the point we want to find the nearest neigbour in the set
        :type point: Point
        :return: the nearest point found in the set or None if the set is empty.
        :rtype point: Point
        """
        if self.isEmpty():
            return None

        nnode = self._nearestNode(point, self._root, 0)
        return nnode.point

    def _nearestNode(self, point, node, level):
        if node == None:
            return None

        # Check most promising side
        ldist = self.leveled_distance(node, point, level)
        if ldist < 0 :
            nearest = self._nearestNode(point, node.left, level + 1)
        else:
            nearest = self._nearestNode(point, node.right, level + 1)

        # Update nearest from promising side
        if nearest == None:
            nearest = node
            sqrdnrst = point.squaredDistanceTo(nearest.point)
        else:
            sqrd = point.squaredDistanceTo(node.point)
            sqrdnrst = point.squaredDistanceTo(nearest.point)
            if sqrd < sqrdnrst:
                sqrdnrst = sqrd
                nearest = node

        # Evaluate if less promising side must be searched too
        sqrdldist = ldist * ldist
        if sqrdnrst > sqrdldist:
            if ldist < 0 :
                nearest2 = self._nearestNode(point, node.right, level + 1)
            else:
                nearest2 = self._nearestNode(point, node.left, level + 1)

            if nearest2 != None:
                sqrdnrst2 = point.squaredDistanceTo(nearest2.point)
                if sqrdnrst2 < sqrdnrst:
                    sqrdnrst = sqrdnrst2
                    nearest = nearest2

        return nearest
