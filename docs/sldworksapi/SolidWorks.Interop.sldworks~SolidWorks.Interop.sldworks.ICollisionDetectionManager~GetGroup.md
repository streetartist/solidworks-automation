# GetGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetGroup`

Gets the specified collision detection group.
Gets the specified collision detection group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGroup( _
   ByVal GroupIndex As System.Integer _
) As System.Object
```

```

Dim instance As ICollisionDetectionManager
Dim GroupIndex As System.Integer
Dim value As System.Object
 
value = instance.GetGroup(GroupIndex)
```

```

System.object GetGroup( 
   System.int GroupIndex
)
```

```

System.Object^ GetGroup( 
   System.int GroupIndex
) 
```

#### Parameters

*GroupIndex*
:   Zero-based index of collision detection group

#### Return Value

[ICollisionDetectionGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md)  
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.md)
