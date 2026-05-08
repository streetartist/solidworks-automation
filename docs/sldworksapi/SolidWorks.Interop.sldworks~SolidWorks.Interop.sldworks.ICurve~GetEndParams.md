# GetEndParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEndParams`

Gets the end conditions of this curve.
Gets the end conditions of this curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEndParams( _
   ByRef Start As System.Double, _
   ByRef End As System.Double, _
   ByRef IsClosed As System.Boolean, _
   ByRef IsPeriodic As System.Boolean _
) As System.Boolean
```

```

Dim instance As ICurve
Dim Start As System.Double
Dim End As System.Double
Dim IsClosed As System.Boolean
Dim IsPeriodic As System.Boolean
Dim value As System.Boolean
 
value = instance.GetEndParams(Start, End, IsClosed, IsPeriodic)
```

```

System.bool GetEndParams( 
   out System.double Start,
   out System.double End,
   out System.bool IsClosed,
   out System.bool IsPeriodic
)
```

```

System.bool GetEndParams( 
   [Out] System.double Start,
   [Out] System.double End,
   [Out] System.bool IsClosed,
   [Out] System.bool IsPeriodic
) 
```

#### Parameters

*Start*
:   Start parameter value

*End*
:   End parameter value

*IsClosed*
:   True for closed curves, false for other types

*IsPeriodic*
:   True for periodic curves, false for other types

#### Return Value

True if the operation was successful, false if not

Remarks

The parametric range is the valid range for the curve. If the curve is infinite (such as a line), then the parametric maximum is the largest permissible value in the parametric space.

Example

[Create Space Parameter Curve on Surface (VBA)](Create_Space_Parameter_Curve_on_Surface_Example_VB.htm)  
[Evaluate Curves Defined in Sketch Space (VBA)](Evaluate_Curves_Defined_in_Sketch_Space_Example_VB.htm)  
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)  
[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)  
[Get Sketch Segment and Curve Data (VBA)](Get_Sketch_Segment_and_Curve_Data_Example_VB.htm)  
[Get Start and End Points of Spline (VBA)](Get_Start_and_End_Points_of_Spline_Example_VB.htm)  
[Create Trimmed Curve (VBA)](Return_Untrimmed_Curve_Example_VB.htm)  
[Create Trimmed Curve (VB.NET)](Return_Untrimmed_Curve_Example_VBNET.htm)  
[Create Trimmed Curve (C#)](Return_Untrimmed_Curve_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)
