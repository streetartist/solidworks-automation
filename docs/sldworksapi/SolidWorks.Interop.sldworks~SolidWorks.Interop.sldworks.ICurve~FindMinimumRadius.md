# FindMinimumRadius Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~FindMinimumRadius`

Finds the minimum radius of curvature of the selected curve and its position and u-v parameters.
Finds the minimum radius of curvature of the selected curve and its position and u-v parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FindMinimumRadius( _
   ByVal Bound As System.Object, _
   ByRef NumOfRadius As System.Integer, _
   ByRef Radius As System.Object, _
   ByRef Location As System.Object, _
   ByRef Parameter As System.Object _
) As System.Boolean
```

```

Dim instance As ICurve
Dim Bound As System.Object
Dim NumOfRadius As System.Integer
Dim Radius As System.Object
Dim Location As System.Object
Dim Parameter As System.Object
Dim value As System.Boolean
 
value = instance.FindMinimumRadius(Bound, NumOfRadius, Radius, Location, Parameter)
```

```

System.bool FindMinimumRadius( 
   System.object Bound,
   out System.int NumOfRadius,
   out System.object Radius,
   out System.object Location,
   out System.object Parameter
)
```

```

System.bool FindMinimumRadius( 
   System.Object^ Bound,
   [Out] System.int NumOfRadius,
   [Out] System.Object^ Radius,
   [Out] System.Object^ Location,
   [Out] System.Object^ Parameter
) 
```

#### Parameters

*Bound*
:   Array of doubles containing the start and end boundaries (see **Remarks**)

*NumOfRadius*
:   Number of radius returned; can be 0 or 1

*Radius*
:   Minimum radius of curvature (see **Remarks**)

*Location*
:   Position where minimum radius curvature occurred (see **Remarks**)

*Parameter*
:   Curve parameter (see **Remarks**)

#### Return Value

True if operation succeeds, false if it fails

Remarks

The search is confined to the portion of the selected curve lying inside of Bound.

COM returns these data types for these parameters:

- Radius: VARIANT of SafeDoubleArray
- Location: VARIANT of SafeDispatchArray of [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)
- Parameter: VARIANT of SafeDoubleArray

Example

[Find Minimum Radius of Curve (VBA)](Find_Minimum_Radius_of_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IFindMinimumRadius.md)  
[ISurface::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~FindMinimumRadius.md)  
[ISurface::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IFindMinimumRadius.md)  
[ICurve::GetEndParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEndParams.md)
