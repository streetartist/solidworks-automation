# ICreateSplinesByEqnParams Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateSplinesByEqnParams`

Obsolete. Superseded by IModelDoc2::ICreateSplinesByEqnParams.
Obsolete. Superseded by [IModelDoc2::ICreateSplinesByEqnParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSplinesByEqnParams( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double _
) As EnumSketchSegments
```

```

Dim instance As IModelDoc
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim value As EnumSketchSegments
 
value = instance.ICreateSplinesByEqnParams(PropArray, KnotsArray, CntrlPntCoordArray)
```

```

EnumSketchSegments ICreateSplinesByEqnParams( 
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray
)
```

```

EnumSketchSegments^ ICreateSplinesByEqnParams( 
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
