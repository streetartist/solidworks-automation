# IGetBendLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBendLines`

Gets the bendlines in a flat-pattern drawing view.
Gets the bendlines in a [flat-pattern drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsFlatPatternView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBendLines( _
   ByVal NumberOfBendLine As System.Integer _
) As SketchSegment
```

```

Dim instance As IView
Dim NumberOfBendLine As System.Integer
Dim value As SketchSegment
 
value = instance.IGetBendLines(NumberOfBendLine)
```

```

SketchSegment IGetBendLines( 
   System.int NumberOfBendLine
)
```

```

SketchSegment^ IGetBendLines( 
   System.int NumberOfBendLine
) 
```

#### Parameters

*NumberOfBendLine*
:   Number of [bendlines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) in a flat-pattern drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of bendlines in a flat-pattern view

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IView::GetBendLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLineCount.md) to get NumberOfBendLine.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLines.md)  
[ISketchSegment::IsBendLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IsBendLine.md)
