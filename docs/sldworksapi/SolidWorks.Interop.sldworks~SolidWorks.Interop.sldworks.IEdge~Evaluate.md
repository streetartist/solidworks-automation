# Evaluate Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate`

Obsolete. Superseded by IEdge::Evaluate2.
Obsolete. Superseded by [IEdge::Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Evaluate2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Evaluate( _
   ByVal Parameter As System.Double _
) As System.Object
```

```

Dim instance As IEdge
Dim Parameter As System.Double
Dim value As System.Object
 
value = instance.Evaluate(Parameter)
```

```

System.object Evaluate( 
   System.double Parameter
)
```

```

System.Object^ Evaluate( 
   System.double Parameter
) 
```

#### Parameters

*Parameter*
:   Value of the edge parameter

#### Return Value

Array values containing the x,y,z value and derivative of the edge (see **Remarks**)

Remarks

Use [IEdge::GetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md) or [IEdge::IGetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate.md) to determine the valid parameter range for this method.

This OLE implementation of this method returns an array of doubles as follows:

[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ, Success ]

where the point values are in meters and Success is True if successful and false if not.

The return value for the COM implementation is different. To determine success, check the HRESULT return value. The array is as follows:

[ PointX, PointY, PointZ, TangentX, TangentY, TangentZ ]

where the point values are specified in meters.

Example

[Select Tangent Edges Via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::IEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IEvaluate.md)
