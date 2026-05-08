# GetLineCount2 Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetLineCount2`

Gets the number of lines in the sketch with an option to exclude or include crosshatch lines.
Gets the number of lines in the sketch with an option to exclude or include crosshatch lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLineCount2( _
   ByVal CrossHatchOption As System.Short _
) As System.Integer
```

```

Dim instance As ISketch
Dim CrossHatchOption As System.Short
Dim value As System.Integer
 
value = instance.GetLineCount2(CrossHatchOption)
```

```

System.int GetLineCount2( 
   System.short CrossHatchOption
)
```

```

System.int GetLineCount2( 
   System.short CrossHatchOption
) 
```

#### Parameters

*CrossHatchOption*
:   Crosshatch option as defined in [swCrossHatchFilter\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCrossHatchFilter_e.html)

#### Return Value

Number of lines

Remarks

Call this method before calling [ISketch::IGetLines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetLines2.md) to determine the size of the array for that method.

Example

[Get Lines in Sketch (VBA)](Get_Lines_in_Sketch_Example_VB.htm)  
[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)
