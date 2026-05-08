# GetLength2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength2`

Obsolete. Superseded by ICurve::GetLength3.
Obsolete. Superseded by [ICurve::GetLength3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLength2( _
   ByVal StartParam As System.Double, _
   ByVal EndParam As System.Double _
) As System.Double
```

```

Dim instance As ICurve
Dim StartParam As System.Double
Dim EndParam As System.Double
Dim value As System.Double
 
value = instance.GetLength2(StartParam, EndParam)
```

```

System.double GetLength2( 
   System.double StartParam,
   System.double EndParam
)
```

```

System.double GetLength2( 
   System.double StartParam,
   System.double EndParam
) 
```

#### Parameters

*StartParam*
:   Start parameter

*EndParam*
:   End parameter

#### Return Value

Length of the curve between the two parameters

Example

[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)  
[Get intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)  
[Get Length of Edge (VBA)](Get_Length_of_Edge_Example_VB.htm)  
[Get Reference Curve Information (VBA)](Get_Reference_Curve_Information_Example_VB.htm)  
[Get Start and End Points of Spline (VBA)](Get_Start_and_End_Points_of_Spline_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)
