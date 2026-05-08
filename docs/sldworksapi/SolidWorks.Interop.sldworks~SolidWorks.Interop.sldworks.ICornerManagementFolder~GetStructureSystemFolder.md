# GetStructureSystemFolder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder~GetStructureSystemFolder`

Gets the structure system folder containing this corner management folder.
Gets the structure system folder containing this corner management folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetStructureSystemFolder() As System.Object
```

```

Dim instance As ICornerManagementFolder
Dim value As System.Object
 
value = instance.GetStructureSystemFolder()
```

```

System.object GetStructureSystemFolder()
```

```

System.Object^ GetStructureSystemFolder(); 
```

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

After calling this method to get the IFeature, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get an [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.md).

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerManagementFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md)  
[ICornerManagementFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder_members.md)
