# ISetMaterialPropertyValues Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues`

Obsolete. Superseded by IFeature::ISetMaterialPropertyValues2.
Obsolete. Superseded by [IFeature::ISetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetMaterialPropertyValues( _
   ByRef MaterialPropertyValues As System.Double _
) As System.Boolean
```

```

Dim instance As IFeature
Dim MaterialPropertyValues As System.Double
Dim value As System.Boolean
 
value = instance.ISetMaterialPropertyValues(MaterialPropertyValues)
```

```

System.bool ISetMaterialPropertyValues( 
   ref System.double MaterialPropertyValues
)
```

```

System.bool ISetMaterialPropertyValues( 
   System.double% MaterialPropertyValues
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
