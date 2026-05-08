# AddSnapShot Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddSnapShot`

Creates a snapshot with the specified name of an assembly.
Creates a snapshot with the specified name of an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSnapShot( _
   ByVal SnapShotName As System.String _
) As SnapShot
```

```

Dim instance As IModelViewManager
Dim SnapShotName As System.String
Dim value As SnapShot
 
value = instance.AddSnapShot(SnapShotName)
```

```

SnapShot AddSnapShot( 
   System.string SnapShotName
)
```

```

SnapShot^ AddSnapShot( 
   System.String^ SnapShotName
) 
```

#### Parameters

*SnapShotName*
:   - Name of the snapshot

        - or -

    - "" to give a default name of "Snap*n*"

        - or -

    - "?" to open the Name Snapshot dialog box

#### Return Value

[ISnapShot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot.md)

Remarks

This method is valid only for assemblies.

Example

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)  
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)  
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::DeleteSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteSnapShot.md)  
[IModelViewManager::GetSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShot.md)  
[IModelViewManager::GetSnapShots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShots.md)
