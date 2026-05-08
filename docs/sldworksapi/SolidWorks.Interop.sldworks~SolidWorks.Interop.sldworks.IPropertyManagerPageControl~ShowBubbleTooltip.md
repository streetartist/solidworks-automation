# ShowBubbleTooltip Method (IPropertyManagerPageControl)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~ShowBubbleTooltip`

Displays a bubble ToolTip containing the specified title, message, and bitmap.
Displays a bubble ToolTip containing the specified title, message, and bitmap.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ShowBubbleTooltip( _
   ByVal Title As System.String, _
   ByVal Message As System.String, _
   ByVal BmpFile As System.String _
) 
```

```

Dim instance As IPropertyManagerPageControl
Dim Title As System.String
Dim Message As System.String
Dim BmpFile As System.String
 
instance.ShowBubbleTooltip(Title, Message, BmpFile)
```

```

void ShowBubbleTooltip( 
   System.string Title,
   System.string Message,
   System.string BmpFile
)
```

```

void ShowBubbleTooltip( 
   System.String^ Title,
   System.String^ Message,
   System.String^ BmpFile
) 
```

#### Parameters

*Title*
:   Title to display in bubble ToolTip

*Message*
:   Message to display in bubble ToolTip

*BmpFile*
:   Path and filename of bitmap to display in bubble ToolTip

Remarks

A bubble ToolTip is useful for validating data typed or selected by users in controls on a PropertyManager page.

Example

See the [IPropertyManagerPageControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.md)
