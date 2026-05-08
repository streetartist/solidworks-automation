# SetMaterialPropertyValues Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues`

Obsolete. Superseded by IFeature::SetMaterialPropertyValues2.
Obsolete. Superseded by [IFeature::SetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMaterialPropertyValues( _
   ByVal MaterialPropertyValues As System.Object _
) As System.Boolean
```

```

Dim instance As IFeature
Dim MaterialPropertyValues As System.Object
Dim value As System.Boolean
 
value = instance.SetMaterialPropertyValues(MaterialPropertyValues)
```

```

System.bool SetMaterialPropertyValues( 
   System.object MaterialPropertyValues
)
```

```

System.bool SetMaterialPropertyValues( 
   System.Object^ MaterialPropertyValues
) 
```

#### Parameters

*MaterialPropertyValues*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
