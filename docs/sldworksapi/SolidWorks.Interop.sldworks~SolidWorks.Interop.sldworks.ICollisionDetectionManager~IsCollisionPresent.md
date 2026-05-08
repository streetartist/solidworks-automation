# IsCollisionPresent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~IsCollisionPresent`

Performs collision detection analysis between all groups of components.
Performs collision detection analysis between all groups of components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsCollisionPresent( _
   ByVal TreatContactAsCollision As System.Boolean _
) As System.Integer
```

```

Dim instance As ICollisionDetectionManager
Dim TreatContactAsCollision As System.Boolean
Dim value As System.Integer
 
value = instance.IsCollisionPresent(TreatContactAsCollision)
```

```

System.int IsCollisionPresent( 
   System.bool TreatContactAsCollision
)
```

```

System.int IsCollisionPresent( 
   System.bool TreatContactAsCollision
) 
```

#### Parameters

*TreatContactAsCollision*
:   True to treat touching faces/edges/vertices as colliding, false to require solid bodies to overlap in a finite volume

#### Return Value

Return code as defined in [swCollisionDetectionResults\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionDetectionResults_e.html)

Remarks

This method takes less time to run than [ICollisionDetectionManager::GetCollisions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetCollisions.md).

Example

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md)  
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.md)
