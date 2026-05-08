# Update3DInterconnectModel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Update3DInterconnectModel`

Updates the model for this 3D Interconnect part or assembly.
Updates the model for this 3D Interconnect part or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Update3DInterconnectModel() As System.Boolean
```

```

Dim instance As IFeature
Dim value As System.Boolean
 
value = instance.Update3DInterconnectModel()
```

```

System.bool Update3DInterconnectModel()
```

```

System.bool Update3DInterconnectModel(); 
```

#### Return Value

True if model updated successfully, false if not

Remarks

Before calling this method, use [IFeature::Is3DInterconnectUpdateAvailable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectUpdateAvailable.md) to determine whether an update is available.

Example

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md)
