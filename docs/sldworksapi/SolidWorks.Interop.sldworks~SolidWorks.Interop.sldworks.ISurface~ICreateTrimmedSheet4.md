# ICreateTrimmedSheet4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4`

Obsolete. Superseded by ISurface::CreateTrimmedSheet5.
Obsolete. Superseded by [ISurface::CreateTrimmedSheet5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateTrimmedSheet4( _
   ByVal NCurves As System.Integer, _
   ByRef Curves As Curve, _
   ByVal PreserveAnalyticCurves As System.Boolean _
) As Body
```

```

Dim instance As ISurface
Dim NCurves As System.Integer
Dim Curves As Curve
Dim PreserveAnalyticCurves As System.Boolean
Dim value As Body
 
value = instance.ICreateTrimmedSheet4(NCurves, Curves, PreserveAnalyticCurves)
```

```

Body ICreateTrimmedSheet4( 
   System.int NCurves,
   ref Curve Curves,
   System.bool PreserveAnalyticCurves
)
```

```

Body^ ICreateTrimmedSheet4( 
   System.int NCurves,
   Curve^% Curves,
   System.bool PreserveAnalyticCurves
) 
```

#### Parameters

*NCurves*
:   Number of curves in the array of curves

*Curves*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) that represent the boundary of the sheet

*PreserveAnalyticCurves*
:   True to preserve analytic curves, false to store all trimming curves as SP-curves

#### Return Value

Newly created sheet [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

The array of curves represents all of the curves required to add the appropriate trimming loops to the surface. A NULL entry in the array represents the separation between loops.

The curves supplied are assumed to lie on the surface. If the curves are 2D curves, then they should be created using this surface.

If your application is creating a trimmed sheet body from an input periodical surface without trimming curves, then the curve array may be empty.

Before calling this method, trim the curves created by [IModeler::ICreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.md) and [IModeler::ICreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.md) by calling [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md). Elliptical curves created by [IModeler::ICreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.md) do not need to be trimmed before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::CreateTrimmedSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet4.md)
