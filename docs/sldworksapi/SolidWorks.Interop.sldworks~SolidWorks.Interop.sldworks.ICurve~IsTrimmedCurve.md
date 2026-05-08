# IsTrimmedCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsTrimmedCurve`

Gets whether the curve is trimmed.
Gets whether the curve is trimmed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsTrimmedCurve() As System.Boolean
```

```

Dim instance As ICurve
Dim value As System.Boolean
 
value = instance.IsTrimmedCurve()
```

```

System.bool IsTrimmedCurve()
```

```

System.bool IsTrimmedCurve(); 
```

#### Return Value

True if this curve is a trimmed curve, false if other curve type

Example

[Create Space Parameter Curve on Surface (VBA)](Create_Space_Parameter_Curve_on_Surface_Example_VB.htm)  
[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)  
[Get Sketch Segment and Curve Data (VBA)](Get_Sketch_Segment_and_Curve_Data_Example_VB.htm)  
[Get Whether Sketch Segment is Trimmed (VBA)](Get_Whether_Sketch_Segment_is_Trimmed_or_Not_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.md)  
[ICurve::CreateTrimmedCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md)  
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md)
