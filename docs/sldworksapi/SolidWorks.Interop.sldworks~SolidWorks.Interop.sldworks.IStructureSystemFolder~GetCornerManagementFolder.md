# GetCornerManagementFolder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder~GetCornerManagementFolder`

Gets the corner management folder in this structure system folder.
Gets the corner management folder in this structure system folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCornerManagementFolder() As System.Object
```

```

Dim instance As IStructureSystemFolder
Dim value As System.Object
 
value = instance.GetCornerManagementFolder()
```

```

System.object GetCornerManagementFolder()
```

```

System.Object^ GetCornerManagementFolder(); 
```

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

After calling this method to get the IFeature, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get an [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.md)  
[IStructureSystemFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder_members.md)
