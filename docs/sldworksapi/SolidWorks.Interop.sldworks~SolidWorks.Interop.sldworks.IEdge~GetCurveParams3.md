# GetCurveParams3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams3`

Gets a data object containing the curve parameters for this edge.
Gets a data object containing the curve parameters for this edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurveParams3() As CurveParamData
```

```

Dim instance As IEdge
Dim value As CurveParamData
 
value = instance.GetCurveParams3()
```

```

CurveParamData GetCurveParams3()
```

```

CurveParamData^ GetCurveParams3(); 
```

#### Return Value

An [ICurveParamData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData.md) object

Remarks

Before calling this method, you must call [IEdge::GetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurve.md) to generate the underlying curve information.

You can use the data returned by this method to determine if a circular edge is a complete circle or an arc.

Example

[Get Edge Curve Parameterization (C#)](Get_Edge_Curve_Parameterization_Example_CSharp.htm)  
[Get Edge Curve Parameterization (VB.NET)](Get_Edge_Curve_Parameterization_Example_VBNET.htm)  
[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)  
[IEdge::IsParamReversed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsParamReversed.md)  
[ICurve::GetBCurveParams5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams5.md)  
[ICurve::GetPCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams2.md)
