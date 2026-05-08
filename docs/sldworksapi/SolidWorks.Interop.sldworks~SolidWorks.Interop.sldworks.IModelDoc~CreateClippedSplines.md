# CreateClippedSplines Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateClippedSplines`

Obsolete. Superseded by IModelDoc2::CreateClippedSplines.
Obsolete. Superseded by [IModelDoc2::CreateClippedSplines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateClippedSplines.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateClippedSplines( _
   ByVal ParamsIn As System.Object, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double _
) As System.Object
```

```

Dim instance As IModelDoc
Dim ParamsIn As System.Object
Dim X1 As System.Double
Dim Y1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim value As System.Object
 
value = instance.CreateClippedSplines(ParamsIn, X1, Y1, X2, Y2)
```

```

System.object CreateClippedSplines( 
   System.object ParamsIn,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
)
```

```

System.Object^ CreateClippedSplines( 
   System.Object^ ParamsIn,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
) 
```

#### Parameters

*ParamsIn*

*X1*

*Y1*

*X2*

*Y2*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
