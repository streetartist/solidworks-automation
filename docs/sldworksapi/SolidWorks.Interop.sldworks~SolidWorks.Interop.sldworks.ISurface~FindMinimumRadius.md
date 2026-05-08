# FindMinimumRadius Method (ISurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~FindMinimumRadius`

Gets the minimum radius of curvature for the selected surface.
Gets the minimum radius of curvature for the selected surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FindMinimumRadius( _
   ByVal UBound As System.Object, _
   ByVal VBound As System.Object, _
   ByRef NumOfRadius As System.Integer, _
   ByRef Radius As System.Object, _
   ByRef Location As System.Object, _
   ByRef UVParameter As System.Object _
) As System.Boolean
```

```

Dim instance As ISurface
Dim UBound As System.Object
Dim VBound As System.Object
Dim NumOfRadius As System.Integer
Dim Radius As System.Object
Dim Location As System.Object
Dim UVParameter As System.Object
Dim value As System.Boolean
 
value = instance.FindMinimumRadius(UBound, VBound, NumOfRadius, Radius, Location, UVParameter)
```

```

System.bool FindMinimumRadius( 
   System.object UBound,
   System.object VBound,
   out System.int NumOfRadius,
   out System.object Radius,
   out System.object Location,
   out System.object UVParameter
)
```

```

System.bool FindMinimumRadius( 
   System.Object^ UBound,
   System.Object^ VBound,
   [Out] System.int NumOfRadius,
   [Out] System.Object^ Radius,
   [Out] System.Object^ Location,
   [Out] System.Object^ UVParameter
) 
```

#### Parameters

*UBound*
:   MinMax UParameter

*VBound*
:   MinMax VParameter

*NumOfRadius*
:   Number of radius; can be 0, 1, or 2

*Radius*
:   Minimum radius of curvature (see **Remarks**)

*Location*
:   [Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) where the minimum radius curvature occurred (see **Remarks**)

*UVParameter*
:   [UV parameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md); because points are UV, third ordinates are 0 (see **Remarks**)

#### Return Value

True if operation succeeds, false if it fails

Remarks

The search is confined to the portion of the selected curve lying inside of UBound and VBound.

COM returns these data types for these parameters:

- Radius: VARIANT of SafeDoubleArray
- Location: VARIANT of SafeDispatchArray of [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)
- UVParameter: VARIANT of SafeDispatchArray of [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

Example

[Find Minimum Radius Curvature of Surface (VBA)](Find_Minimum_Radius_Curvature_of_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IFindMinimumRadius.md)  
[ISurface::Parameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.md)  
[ISurface::IParameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.md)  
[ICurve::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~FindMinimumRadius.md)  
[ICurve::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IFindMinimumRadius.md)  
[IFace2::GetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetUVBounds.md)  
[IFace2::IGetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetUVBounds.md)
