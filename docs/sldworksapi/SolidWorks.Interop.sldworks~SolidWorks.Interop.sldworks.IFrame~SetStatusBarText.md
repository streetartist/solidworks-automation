# SetStatusBarText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~SetStatusBarText`

Displays a text string in the main status bar area to the left of the status bar.
Displays a text string in the main status bar area to the left of the status bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetStatusBarText( _
   ByVal MessageString As System.String _
) 
```

```

Dim instance As IFrame
Dim MessageString As System.String
 
instance.SetStatusBarText(MessageString)
```

```

void SetStatusBarText( 
   System.string MessageString
)
```

```

void SetStatusBarText( 
   System.String^ MessageString
) 
```

#### Parameters

*MessageString*
:   Text to display in the status bar

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::GetStatusBarPane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetStatusBarPane.md)
