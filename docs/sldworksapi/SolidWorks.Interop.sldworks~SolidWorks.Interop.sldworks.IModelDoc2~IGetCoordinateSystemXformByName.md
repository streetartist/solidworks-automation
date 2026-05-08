# IGetCoordinateSystemXformByName Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetCoordinateSystemXformByName`

Obsolete. Superseded by IModelDocExtension::GetCoordinateSystemTransformByName.
Obsolete. Superseded by [IModelDocExtension::GetCoordinateSystemTransformByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCoordinateSystemXformByName( _
   ByVal NameIn As System.String _
) As System.Double
```

```

Dim instance As IModelDoc2
Dim NameIn As System.String
Dim value As System.Double
 
value = instance.IGetCoordinateSystemXformByName(NameIn)
```

```

System.double IGetCoordinateSystemXformByName( 
   System.string NameIn
)
```

```

System.double IGetCoordinateSystemXformByName( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
