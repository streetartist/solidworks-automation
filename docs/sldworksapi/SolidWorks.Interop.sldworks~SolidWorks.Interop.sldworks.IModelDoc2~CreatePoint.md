# CreatePoint Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePoint`

Obsolete. Superseded by IModelDoc2::CreatePoint2.
Obsolete. Superseded by [IModelDoc2::CreatePoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePoint2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePoint( _
   ByVal PointX As System.Double, _
   ByVal PointY As System.Double, _
   ByVal PointZ As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim PointX As System.Double
Dim PointY As System.Double
Dim PointZ As System.Double
Dim value As System.Boolean
 
value = instance.CreatePoint(PointX, PointY, PointZ)
```

```

System.bool CreatePoint( 
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

```

System.bool CreatePoint( 
   System.double PointX,
   System.double PointY,
   System.double PointZ
) 
```

#### Parameters

*PointX*

*PointY*

*PointZ*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
