# GetCollisions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetCollisions`

Gets the collisions detected.
Gets the collisions detected.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCollisions( _
   ByVal TreatContactAsCollision As System.Boolean, _
   ByRef Collisions As System.Object _
) As System.Integer
```

```

Dim instance As ICollisionDetectionManager
Dim TreatContactAsCollision As System.Boolean
Dim Collisions As System.Object
Dim value As System.Integer
 
value = instance.GetCollisions(TreatContactAsCollision, Collisions)
```

```

System.int GetCollisions( 
   System.bool TreatContactAsCollision,
   out System.object Collisions
)
```

```

System.int GetCollisions( 
   System.bool TreatContactAsCollision,
   [Out] System.Object^ Collisions
) 
```

#### Parameters

*TreatContactAsCollision*
:   True to treat touching faces/edges/vertices as colliding, false to require solid bodies to overlap in a finite volume

*Collisions*
:   Array of [ICollision](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision.md)s

#### Return Value

Number of collisions found

Remarks

Use [ICollisionDetectionManager::IsCollisionPresent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~IsCollisionPresent.md) to determine whether to run this method.

This method can take significantly longer to execute than ICollisionDetectionManager::IsCollisionPresent, because this method might perform the collision detection calculation repeatedly.

Example

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md)  
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.md)
