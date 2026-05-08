# SetImportedFeatureParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters`

Sets the data object for this 3D Interconnect part or assembly.
Sets the data object for this 3D Interconnect part or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetImportedFeatureParameters( _
   ByVal DataObj As System.Object _
) As System.Integer
```

```

Dim instance As IFeature
Dim DataObj As System.Object
Dim value As System.Integer
 
value = instance.SetImportedFeatureParameters(DataObj)
```

```

System.int SetImportedFeatureParameters( 
   System.object DataObj
)
```

```

System.int SetImportedFeatureParameters( 
   System.Object^ DataObj
) 
```

#### Parameters

*DataObj*
:   [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md)

#### Return Value

Error codes as defined in [sw3DInterconnectImportErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DInterconnectImportErrors_e.html)

Remarks

Before calling this method, use [IFeature::Is3DInterconnectFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectFeature.md) to ensure that this is a 3D Interconnect feature.

Example

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
