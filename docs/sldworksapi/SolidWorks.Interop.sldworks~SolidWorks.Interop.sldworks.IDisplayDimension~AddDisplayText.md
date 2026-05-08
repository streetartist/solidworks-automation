# AddDisplayText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayText`

Overrides the display text.
Overrides the display text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddDisplayText( _
   ByVal Text As System.String, _
   ByVal Position As System.Object, _
   ByVal Format As System.Object, _
   ByVal Attachment As System.Integer, _
   ByVal WidthFactor As System.Double _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim Text As System.String
Dim Position As System.Object
Dim Format As System.Object
Dim Attachment As System.Integer
Dim WidthFactor As System.Double
Dim value As System.Boolean
 
value = instance.AddDisplayText(Text, Position, Format, Attachment, WidthFactor)
```

```

System.bool AddDisplayText( 
   System.string Text,
   System.object Position,
   System.object Format,
   System.int Attachment,
   System.double WidthFactor
)
```

```

System.bool AddDisplayText( 
   System.String^ Text,
   System.Object^ Position,
   System.Object^ Format,
   System.int Attachment,
   System.double WidthFactor
) 
```

#### Parameters

*Text*
:   Text to display

*Position*
:   Location of the text; array of 3 doubles

*Format*
:   Object for the text format

*Attachment*
:   Justification of the text as defined in [swTextJustification\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextJustification_e.html)

*WidthFactor*
:   Horizontal scale factor of the text

#### Return Value

True if successful, false if not

Remarks

The new graphics displayed by this method are temporary. When the user changes the dimension, this display dimension reverts back to the SOLIDWORKS standard.

Example

[Replace Dimension with Text (VBA)](Replace_Dimension_with_Text_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::IAddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText.md)  
[IDisplayDimension::HorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~HorizontalJustification.md)  
[IDisplayDimension::VerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~VerticalJustification.md)
