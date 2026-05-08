# ISketchSplineByEqnParams Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ISketchSplineByEqnParams`

Obsolete. Superseded by IModelDoc2::ISketchSplineByEqnParams.
Obsolete. Superseded by [IModelDoc2::ISketchSplineByEqnParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISketchSplineByEqnParams.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISketchSplineByEqnParams( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim value As System.Integer
 
value = instance.ISketchSplineByEqnParams(PropArray, KnotsArray, CntrlPntCoordArray)
```

```

System.int ISketchSplineByEqnParams( 
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray
)
```

```

System.int ISketchSplineByEqnParams( 
   System.int% PropArray,
   System.double% KnotsArray,
   System.double% CntrlPntCoordArray
) 
```

#### Parameters

*PropArray*

*KnotsArray*

*CntrlPntCoordArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
