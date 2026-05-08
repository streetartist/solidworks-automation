# GetTextHeightAtIndex Method (IDisplayData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextHeightAtIndex`

Gets the text height for the specified piece of text .
Gets the text height for the specified piece of text .

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextHeightAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.GetTextHeightAtIndex(Index)
```

```

System.double GetTextHeightAtIndex( 
   System.int Index
)
```

```

System.double GetTextHeightAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Zero-based index of the desired piece of text

#### Return Value

Text height for the specified piece of text in meters

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAngleAtIndex.md)  
[IDisplayData::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAtIndex.md)  
[IDisplayData::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextCount.md)  
[IDisplayData::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextFontAtIndex.md)  
[IDisplayData::GetTextInBoxHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxHeightAtIndex.md)  
[IDisplayData::GetTextInBoxStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxStyleAtIndex.md)  
[IDisplayData::GetTextInBoxWidthAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxWidthAtIndex.md)  
[IDisplayData::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInvertAtIndex.md)  
[IDisplayData::GetTextLineSpacingAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextLineSpacingAtIndex.md)  
[IDisplayData::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPositionAtIndex.md)  
[IDisplayData::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextRefPositionAtIndex.md)  
[IDisplayData::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetTextPositionAtIndex.md)  
[IDisplayData::GetTextPlaneAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPlaneAtIndex.md)
