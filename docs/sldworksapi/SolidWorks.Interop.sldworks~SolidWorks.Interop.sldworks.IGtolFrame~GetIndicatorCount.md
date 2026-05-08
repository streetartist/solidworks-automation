# GetIndicatorCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicatorCount`

Gets the number of indicators in this Gtol frame.
Gets the number of indicators in this Gtol frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIndicatorCount() As System.Integer
```

```

Dim instance As IGtolFrame
Dim value As System.Integer
 
value = instance.GetIndicatorCount()
```

```

System.int GetIndicatorCount()
```

```

System.int GetIndicatorCount(); 
```

#### Return Value

Number of indicators in this Gtol frame

Remarks

Use this method to determine IndicatorIndex parameters before calling:

- [IGtolFrame::DeleteIndicator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~DeleteIndicator.md)
- [IGtolFrame::GetIndicator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicator.md)
- [IGtolFrame::SetIndicator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetIndicator.md)

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtolFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md)  
[IGtolFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame_members.md)
