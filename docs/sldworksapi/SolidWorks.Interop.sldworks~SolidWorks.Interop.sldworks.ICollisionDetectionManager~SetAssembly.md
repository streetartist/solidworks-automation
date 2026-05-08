# SetAssembly Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~SetAssembly`

Sets the active assembly for this collision detection manager.
Sets the active assembly for this collision detection manager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAssembly( _
   ByVal OwnerAssem As System.Object _
) As System.Integer
```

```

Dim instance As ICollisionDetectionManager
Dim OwnerAssem As System.Object
Dim value As System.Integer
 
value = instance.SetAssembly(OwnerAssem)
```

```

System.int SetAssembly( 
   System.object OwnerAssem
)
```

```

System.int SetAssembly( 
   System.Object^ OwnerAssem
) 
```

#### Parameters

*OwnerAssem*
:   [IAssemblyDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)

#### Return Value

Error code as defined in [swCollisionManagerSetAssemblyErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCollisionManagerSetAssemblyErrors_e.html)

Example

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md)  
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.md)  
[ICollisionDetectionManager::GetAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetAssembly.md)
