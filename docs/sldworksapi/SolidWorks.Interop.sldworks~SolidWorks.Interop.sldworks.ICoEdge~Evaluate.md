# Evaluate Method (ICoEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~Evaluate`

Obsolete. Superseded by ICoEdge::Evaluate2.
Obsolete. Superseded by [ICoEdge::Evaluate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~Evaluate2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Evaluate( _
   ByVal Param As System.Double _
) As System.Object
```

```

Dim instance As ICoEdge
Dim Param As System.Double
Dim value As System.Object
 
value = instance.Evaluate(Param)
```

```

System.object Evaluate( 
   System.double Param
)
```

```

System.Object^ Evaluate( 
   System.double Param
) 
```

#### Parameters

*Param*
:   Curve parameter desired (U value desired for evaluation)

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The tangency vector is defined to be in the direction of the coedge.

The format of the return value is an array of 6 doubles:

- retval[0] x location on the curve
- retval[1] y location on the curve
- retval[2] z location on the curve
- retval[3] x vector describing the tangency at the parameter location on the coedge
- retval[4] y vector describing the tangency at the parameter location on the coedge
- retval[5] z vector describing the tangency at the parameter location on the coedge

Example

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)  
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)  
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.md)  
[ICoEdge::IEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IEvaluate.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)  
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md)
