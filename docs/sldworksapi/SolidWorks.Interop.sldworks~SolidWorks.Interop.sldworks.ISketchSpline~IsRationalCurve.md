# IsRationalCurve Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsRationalCurve`

Gets whether this spline is rational or non-rational.
Gets whether this spline is rational or non-rational.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsRationalCurve As System.Boolean
```

```

Dim instance As ISketchSpline
Dim value As System.Boolean
 
value = instance.IsRationalCurve
```

```

System.bool IsRationalCurve {get;}
```

```

property System.bool IsRationalCurve {
   System.bool get();
}
```

#### Property Value

True if rational, false if non-rational

Example

[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::MakeRational Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~MakeRational.md)
