# GetSnapShots Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShots`

Gets the snapshots of an assembly.
Gets the snapshots of an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSnapShots() As System.Object
```

```

Dim instance As IModelViewManager
Dim value As System.Object
 
value = instance.GetSnapShots()
```

```

System.object GetSnapShots()
```

```

System.Object^ GetSnapShots(); 
```

#### Return Value

Array of [ISnapShot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot.md)s

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
[IModelViewManager::AddSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddSnapShot.md)  
[IModelViewManager::DeleteSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteSnapShot.md)  
[IModelViewManager::GetSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShot.md)
