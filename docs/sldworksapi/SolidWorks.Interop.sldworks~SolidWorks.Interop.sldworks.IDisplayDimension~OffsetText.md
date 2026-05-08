# OffsetText Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~OffsetText`

Gets or sets whether or not to offset the text of a dimension.
Gets or sets whether or not to offset the text of a dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OffsetText As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.OffsetText = value
 
value = instance.OffsetText
```

```

System.bool OffsetText {get; set;}
```

```

property System.bool OffsetText {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to offset the dimension text, false to not

Remarks

|  |  |
| --- | --- |
| **If this property is set to...** | **Then...** |
| True | - Dimension text is attached to the end of a leader that can be moved about freely. - Dimension line and extension lines to which the dimension text is associated do not move. |
| false | - Dimension text is displayed on the dimension line. - Dimension line and extension lines can move when the dimension text is moved. |

Because radial and diametric dimensions are already attached to the end of a leader, this property is not available for these types of dimensions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.md)  
[IDisplayDimension::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.md)
