# Is3DInterconnectUpdateAvailable Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectUpdateAvailable`

Gets whether an update is available for this 3D Interconnect part or assembly.
Gets whether an update is available for this 3D Interconnect part or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Is3DInterconnectUpdateAvailable As System.Boolean
```

```

Dim instance As IFeature
Dim value As System.Boolean
 
value = instance.Is3DInterconnectUpdateAvailable
```

```

System.bool Is3DInterconnectUpdateAvailable {get;}
```

```

property System.bool Is3DInterconnectUpdateAvailable {
   System.bool get();
}
```

#### Property Value

True if an update is available, false if not

Remarks

If this property is true, use [IFeature::Update3DInterconnectModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Update3DInterconnectModel.md) to update the imported feature or component.

Example

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md)
