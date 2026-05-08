# GetTextInBoxWidthAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxWidthAtIndex`

Gets the text-in-box width of the specified text and table cell in the table annotation.
Gets the text-in-box width of the specified text and table cell in the table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextInBoxWidthAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.GetTextInBoxWidthAtIndex(Index)
```

```

System.double GetTextInBoxWidthAtIndex( 
   System.int Index
)
```

```

System.double GetTextInBoxWidthAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Zero-based index of the text and table cell to examine

#### Return Value

Width of the text-in-box in system units

Remarks

Text-in-box refers to a fixed-size area slightly smaller than the table cell.

If [IDisplayData::GetTextInBoxStyleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxStyleAtIndex.md) returns swTextInBoxStyleNone, then this method returns 0 as well.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[DisplayData::IGetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAngleAtIndex.md)  
[DisplayData::IGetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAtIndex.md)  
[DisplayData::IGetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextCount.md)  
[DisplayData::IGetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextFontAtIndex.md)  
[DisplayData::IGetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextHeightAtIndex.md)  
[DisplayData::IGetTextInBoxHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxHeightAtIndex.md)  
[DisplayData::IGetTextInBoxStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxStyleAtIndex.md)  
[DisplayData::IGetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInvertAtIndex.md)  
[DisplayData::IGetTextLineSpacingAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextLineSpacingAtIndex.md)  
[DisplayData::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPositionAtIndex.md)  
[DisplayData::IGetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextRefPositionAtIndex.md)  
[DisplayData::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetTextPositionAtIndex.md)  
[IDisplayData::GetTextPlaneAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPlaneAtIndex.md)
