# ICreateClippedSplines Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateClippedSplines`

Obsolete. Superseded by IModelDoc2::ICreateClippedSplines.
Obsolete. Superseded by [IModelDoc2::ICreateClippedSplines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateClippedSplines.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateClippedSplines( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double _
) As EnumSketchSegments
```

```

Dim instance As IModelDoc
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim value As EnumSketchSegments
 
value = instance.ICreateClippedSplines(PropArray, KnotsArray, CntrlPntCoordArray, X1, Y1, X2, Y2)
```

```

EnumSketchSegments ICreateClippedSplines( 
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
)
```

```

EnumSketchSegments^ ICreateClippedSplines( 
   System.int% PropArray,
   System.double% KnotsArray,
   System.double% CntrlPntCoordArray,
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2
) 
```

#### Parameters

*PropArray*

*KnotsArray*

*CntrlPntCoordArray*

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
