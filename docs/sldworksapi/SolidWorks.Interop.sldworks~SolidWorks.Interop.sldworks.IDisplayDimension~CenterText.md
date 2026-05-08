# CenterText Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~CenterText`

Gets or sets whether the text of this display dimension should be automatically centered.
Gets or sets whether the text of this display dimension should be automatically centered.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CenterText As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.CenterText = value
 
value = instance.CenterText
```

```

System.bool CenterText {get; set;}
```

```

property System.bool CenterText {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True centers the text, false does not center the text

Remarks

Dimension text must be positioned somewhere between the two dimensioned points in order to be centered.

|  |  |
| --- | --- |
| **In a...** | **The two points are the...** |
| linear dimension | the end points of the dimension |
| diameter dimension | the end points of the dimension line lying on the arc. |
| radius dimension | the center point and the dimension line end point lying on the arc |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.md)  
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.md)
