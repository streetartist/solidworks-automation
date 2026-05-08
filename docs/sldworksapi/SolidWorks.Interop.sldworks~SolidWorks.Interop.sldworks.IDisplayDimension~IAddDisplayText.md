# IAddDisplayText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText`

Overrides the display text for this display dimension.
Overrides the display text for this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddDisplayText( _
   ByVal Text As System.String, _
   ByRef Position As System.Double, _
   ByVal Format As TextFormat, _
   ByVal Attachment As System.Integer, _
   ByVal WidthFactor As System.Double _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim Text As System.String
Dim Position As System.Double
Dim Format As TextFormat
Dim Attachment As System.Integer
Dim WidthFactor As System.Double
Dim value As System.Boolean
 
value = instance.IAddDisplayText(Text, Position, Format, Attachment, WidthFactor)
```

```

System.bool IAddDisplayText( 
   System.string Text,
   ref System.double Position,
   TextFormat Format,
   System.int Attachment,
   System.double WidthFactor
)
```

```

System.bool IAddDisplayText( 
   System.String^ Text,
   System.double% Position,
   TextFormat^ Format,
   System.int Attachment,
   System.double WidthFactor
) 
```

#### Parameters

*Text*
:   Text to display

*Position*
:   Location of the text; pointer to an array of 3 doubles

*Format*
:   Pointer to [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) object

*Attachment*
:   Justification of the text as defined in [swTextJustification\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextJustification_e.html)

*WidthFactor*
:   Horizontal scale factor of the text

#### Return Value

True if successful, false if not

Remarks

The new graphics displayed by this method are temporary. When the user changes the dimension, this display dimension reverts back to the SOLIDWORKS standard.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::AddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayText.md)
