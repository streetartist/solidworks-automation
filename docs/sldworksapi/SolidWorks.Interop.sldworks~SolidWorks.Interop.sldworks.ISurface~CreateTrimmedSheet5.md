# CreateTrimmedSheet5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet5`

Creates a trimmed sheet body from this surface.
Creates a trimmed sheet body from this surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTrimmedSheet5( _
   ByVal Curves As System.Object, _
   ByVal PreserveAnalyticCurves As System.Boolean, _
   ByVal Tolerance As System.Double _
) As System.Object
```

```

Dim instance As ISurface
Dim Curves As System.Object
Dim PreserveAnalyticCurves As System.Boolean
Dim Tolerance As System.Double
Dim value As System.Object
 
value = instance.CreateTrimmedSheet5(Curves, PreserveAnalyticCurves, Tolerance)
```

```

System.object CreateTrimmedSheet5( 
   System.object Curves,
   System.bool PreserveAnalyticCurves,
   System.double Tolerance
)
```

```

System.Object^ CreateTrimmedSheet5( 
   System.Object^ Curves,
   System.bool PreserveAnalyticCurves,
   System.double Tolerance
) 
```

#### Parameters

*Curves*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) that represent the boundary of the trimmed sheet (see **Remarks**)

*PreserveAnalyticCurves*
:   True to preserve analytic curves, false to store all trimming curves as SP-curves

*Tolerance*
:   Tolerance for gaps between edges (see **Remarks**)

#### Return Value

Temporary sheet [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

The Curves array contains all of the curves required to add the appropriate trimming loops to the surface. A null or Nothing entry in the array represents the separation between loops.

The trimming curves supplied are assumed to lie on the surface. If the curves are 2D curves, then they should be created using this surface.

If your application is creating a trimmed sheet body from a periodic surface without trimming curves, then the Curves array should contain only one entry: null or Nothing.

Tolerance sets the edge precision in PK\_SURF\_make\_sheet\_trimmed. The default parasolid tolerance is 0.00001. This parameter allows you to specify a looser tolerance for gaps between edges.

Before calling this method, trim the curves created by [IModeler::CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.md) and [IModeler::CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.md) by calling [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md). Elliptical curves created by [IModeler::CreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.md) do not need to be trimmed before calling this method.

Example

[Create Spherical Surface, Trimmed Sheet, and Feature from Body (VBA)](Create_Spherical_Surface_Trimmed_Sheet_and_Feature_From_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
