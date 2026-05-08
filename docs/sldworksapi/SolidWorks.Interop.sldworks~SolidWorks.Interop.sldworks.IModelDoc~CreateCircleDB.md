# CreateCircleDB Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCircleDB`

Obsolete. Superseded by IModelDoc2::CreateCircleDB.
Obsolete. Superseded by [IModelDoc2::CreateCircleDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCircleDB.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCircleDB( _
   ByVal Cx As System.Double, _
   ByVal Cy As System.Double, _
   ByVal Cz As System.Double, _
   ByVal Radius As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim Cx As System.Double
Dim Cy As System.Double
Dim Cz As System.Double
Dim Radius As System.Double
Dim value As System.Boolean
 
value = instance.CreateCircleDB(Cx, Cy, Cz, Radius)
```

```

System.bool CreateCircleDB( 
   System.double Cx,
   System.double Cy,
   System.double Cz,
   System.double Radius
)
```

```

System.bool CreateCircleDB( 
   System.double Cx,
   System.double Cy,
   System.double Cz,
   System.double Radius
) 
```

#### Parameters

*Cx*

*Cy*

*Cz*

*Radius*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
