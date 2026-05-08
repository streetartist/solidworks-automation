# GetLineCount2 Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetLineCount2`

Gets the number of lines in this view with an option to include or exclude crosshatch lines.
Gets the number of lines in this view with an option to include or exclude crosshatch lines.

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

Dim instance As IView
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

Call this method before calling [IView::IGetLines4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetLines4.md) to get the size of the array for that method.

Example

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetLines4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetLines4.md)  
[IView::IGetLines4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetLines4.md)
