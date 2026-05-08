# GetLineFontInfo2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2`

Gets the detailed information about the specified line font.
Gets the detailed information about the specified line font.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLineFontInfo2( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetLineFontInfo2(Index)
```

```

System.object GetLineFontInfo2( 
   System.int Index
)
```

```

System.Object^ GetLineFontInfo2( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index position of the line font which is within the index range returned by [IDrawingDoc::GetLineFontCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontCount2.md)

#### Return Value

Array containing the line font information (see **Remarks**)

Remarks

This method breaks down the line font into its individual segment lengths.

Lines are repeating patterns of space and solid segments. The segCount argument returns the number of segments that define the pattern, and segLengths[] specifies the length of each segment. A negative length value indicates space.

For example:

> Solid line: segCount = 1, segLenghts[] = {0.5}
>
> Dashed line: segCount = 2, segLengths[] = {0.25, -0.25}

VARIANT format:

> double segCount - Number of segments in the pattern
>
> double segLengths[segCount] - Length of each segment

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::GetLineFontId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontId.md)  
[IDrawingDoc::GetLineFontName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.md)  
[GetLineFontCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontCount2.md)  
[IDrawingDoc::SetLineColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineColor.md)  
[IDrawingDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineStyle.md)  
[IDrawingDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidth.md)
