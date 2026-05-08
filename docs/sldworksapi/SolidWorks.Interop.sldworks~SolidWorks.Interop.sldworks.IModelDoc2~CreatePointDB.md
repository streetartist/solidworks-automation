# CreatePointDB Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePointDB`

Obsolete. Superseded by IModelDoc2::CreatePoint2 and IModelDoc2::ICreatePoint2.
Obsolete. Superseded by [IModelDoc2::CreatePoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePoint2.md) and [IModelDoc2::ICreatePoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePoint2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePointDB( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.CreatePointDB(X, Y, Z)
```

```

System.bool CreatePointDB( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool CreatePointDB( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*

*Y*

*Z*

Remarks

**IMPORTANT:**  This method ignores the z value when adding a point to a 3D sketch. Thus, update your code to use the more current method, IModelDoc2::CreatePoint2 or IModelDoc2::ICreatePoint2.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
