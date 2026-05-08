# ICollisionDetection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ICollisionDetection`

Sets the collision detection parameters.
Sets the collision detection parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICollisionDetection( _
   ByVal Count As System.Integer, _
   ByRef ComponentArray As Component2, _
   ByVal PartOnly As System.Boolean, _
   ByVal StopAt As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDragOperator
Dim Count As System.Integer
Dim ComponentArray As Component2
Dim PartOnly As System.Boolean
Dim StopAt As System.Boolean
Dim value As System.Boolean
 
value = instance.ICollisionDetection(Count, ComponentArray, PartOnly, StopAt)
```

```

System.bool ICollisionDetection( 
   System.int Count,
   ref Component2 ComponentArray,
   System.bool PartOnly,
   System.bool StopAt
)
```

```

System.bool ICollisionDetection( 
   System.int Count,
   Component2^% ComponentArray,
   System.bool PartOnly,
   System.bool StopAt
) 
```

#### Parameters

*Count*
:   Number of components for collision detection

*ComponentArray*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) for collision detection

*PartOnly*
:   True checks for collisions with only the components that you selected to move, false check for collisions in all affected components

*StopAt*
:   True stops the motion of the component when it touches any other entity, false does not

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::CollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetection.md)  
[IDragOperator::CollisionDetectionEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetectionEnabled.md)
