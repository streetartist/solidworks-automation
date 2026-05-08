# SketchConvertIsoCurves Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConvertIsoCurves`

Converts ISO-parametric curves on a selected surface into a sketch entity.
Converts ISO-parametric curves on a selected surface into a sketch entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchConvertIsoCurves( _
   ByVal PercentRatio As System.Double, _
   ByVal VORuDir As System.Boolean, _
   ByVal DoConstrain As System.Boolean, _
   ByVal SkipHoles As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim PercentRatio As System.Double
Dim VORuDir As System.Boolean
Dim DoConstrain As System.Boolean
Dim SkipHoles As System.Boolean
 
instance.SketchConvertIsoCurves(PercentRatio, VORuDir, DoConstrain, SkipHoles)
```

```

void SketchConvertIsoCurves( 
   System.double PercentRatio,
   System.bool VORuDir,
   System.bool DoConstrain,
   System.bool SkipHoles
)
```

```

void SketchConvertIsoCurves( 
   System.double PercentRatio,
   System.bool VORuDir,
   System.bool DoConstrain,
   System.bool SkipHoles
) 
```

#### Parameters

*PercentRatio*
:   Value for percent ratio

*VORuDir*
:   True for V direction, false for UDirection

*DoConstrain*
:   True if you want to constrain these new sketch entities, false if not

*SkipHoles*
:   True if you want to skip the holes in this surface, false if not

Example

[Divide Surface into 3D Sketches (VBA)](Divide_Surface_into_3D_Sketches_Example_VB.htm)  
[Convert Curves into 3D Sketches (C#)](Convert_Curves_into_3D_Sketches_Example_CSharp.htm)  
[Convert Curves into 3D Sketches (VB.NET)](Convert_Curves_into_3D_Sketches_Example_VBNET.htm)  
[Convert Curves into 3D Sketches (VBA)](Convert_Curves_into_3D_Sketches_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
