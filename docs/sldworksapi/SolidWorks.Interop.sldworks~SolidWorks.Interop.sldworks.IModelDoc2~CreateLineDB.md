# CreateLineDB Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateLineDB`

Obsolete. Superseded by IModelDoc2::CreateLine2.
Obsolete. Superseded by [IModelDoc2::CreateLine2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateLine2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateLineDB( _
   ByVal Sx As System.Double, _
   ByVal Sy As System.Double, _
   ByVal Sz As System.Double, _
   ByVal Ex As System.Double, _
   ByVal Ey As System.Double, _
   ByVal Ez As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Sx As System.Double
Dim Sy As System.Double
Dim Sz As System.Double
Dim Ex As System.Double
Dim Ey As System.Double
Dim Ez As System.Double
Dim value As System.Boolean
 
value = instance.CreateLineDB(Sx, Sy, Sz, Ex, Ey, Ez)
```

```

System.bool CreateLineDB( 
   System.double Sx,
   System.double Sy,
   System.double Sz,
   System.double Ex,
   System.double Ey,
   System.double Ez
)
```

```

System.bool CreateLineDB( 
   System.double Sx,
   System.double Sy,
   System.double Sz,
   System.double Ex,
   System.double Ey,
   System.double Ez
) 
```

#### Parameters

*Sx*

*Sy*

*Sz*

*Ex*

*Ey*

*Ez*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
