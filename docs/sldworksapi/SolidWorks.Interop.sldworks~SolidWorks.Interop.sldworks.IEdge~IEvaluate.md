# IEvaluate Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate`

Obsolete. Superseded by IEdge::IEvaluate2.
Obsolete. Superseded by [IEdge::IEvaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEvaluate( _
   ByVal Parameter As System.Double _
) As System.Double
```

```

Dim instance As IEdge
Dim Parameter As System.Double
Dim value As System.Double
 
value = instance.IEvaluate(Parameter)
```

```

System.double IEvaluate( 
   System.double Parameter
)
```

```

System.double IEvaluate( 
   System.double Parameter
) 
```

#### Parameters

*Parameter*
:   Value of the edge parameter

#### Return Value

Pointer to an array of doubles (see **Remarks**)

Remarks

Use [IEdge::GetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md) or [IEdge::IGetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate.md) to determine the valid parameter range for this method.

This OLE implementation of this method returns an array of doubles as follows:

[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ, Success ]

where the point values are in meters and Success is True if successful and false if not.

The return value for the COM implementation is different. To determine success, check the HRESULT return value. The array is as follows:

[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ ]

where the point values are specified in meters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::Evaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate.md)
