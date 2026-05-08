# DeleteSnapShot Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteSnapShot`

Deletes the specified snapshot from an assembly.
Deletes the specified snapshot from an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteSnapShot( _
   ByVal SnapShotName As System.String _
) As System.Boolean
```

```

Dim instance As IModelViewManager
Dim SnapShotName As System.String
Dim value As System.Boolean
 
value = instance.DeleteSnapShot(SnapShotName)
```

```

System.bool DeleteSnapShot( 
   System.string SnapShotName
)
```

```

System.bool DeleteSnapShot( 
   System.String^ SnapShotName
) 
```

#### Parameters

*SnapShotName*
:   Name of snapshot to delete

#### Return Value

True if successful, false if not

Remarks

This method is valid only for assemblies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::AddSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddSnapShot.md)  
[IModelViewManager::GetSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShot.md)  
[IModelViewManager::GetSnapShots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShots.md)
