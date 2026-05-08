# RemoveGroup Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~RemoveGroup`

Removes the specified collision detection group from collision detection.
Removes the specified collision detection group from collision detection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveGroup( _
   ByVal GroupIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As ICollisionDetectionManager
Dim GroupIndex As System.Integer
Dim value As System.Boolean
 
value = instance.RemoveGroup(GroupIndex)
```

```

System.bool RemoveGroup( 
   System.int GroupIndex
)
```

```

System.bool RemoveGroup( 
   System.int GroupIndex
) 
```

#### Parameters

*GroupIndex*
:   Zero-based index of the collision detection group to remove from collision detection

#### Return Value

True if collision detection group successfully removed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md)  
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.md)
