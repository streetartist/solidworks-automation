# ShowSmartMessage Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowSmartMessage`

Displays a SOLIDWORKS-style message as a ToolTip in the graphics area and on the status bar.
Displays a SOLIDWORKS-style message as a ToolTip in the graphics area and on the status bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ShowSmartMessage( _
   ByVal Name As System.String, _
   ByVal TimeInMillSec As System.Integer, _
   ByVal ShowInStatusBar As System.Boolean, _
   ByVal RemoveDefaultTip As System.Boolean _
) 
```

```

Dim instance As IModelDocExtension
Dim Name As System.String
Dim TimeInMillSec As System.Integer
Dim ShowInStatusBar As System.Boolean
Dim RemoveDefaultTip As System.Boolean
 
instance.ShowSmartMessage(Name, TimeInMillSec, ShowInStatusBar, RemoveDefaultTip)
```

```

void ShowSmartMessage( 
   System.string Name,
   System.int TimeInMillSec,
   System.bool ShowInStatusBar,
   System.bool RemoveDefaultTip
)
```

```

void ShowSmartMessage( 
   System.String^ Name,
   System.int TimeInMillSec,
   System.bool ShowInStatusBar,
   System.bool RemoveDefaultTip
) 
```

#### Parameters

*Name*
:   Message to display in the ToolTip

*TimeInMillSec*
:   Time, in milliseconds, to display the message

*ShowInStatusBar*
:   True to show the message on the SOLIDWORKS status bar, false to not

*RemoveDefaultTip*
:   True to replace the default SOLIDWORKS ToolTip with this message for TimeInMillSec, false to not

Example

**Visual Basic for Applications (VBA):**

Option Explicit

Dim swApp As SldWorks.SldWorks  
Dim swModelDocExt As SldWorks.ModelDocExtension  
Dim swModel As SldWorks.ModelDoc2  
Dim swSelMgr As SldWorks.SelectionMgr

Sub main()

Set swApp = Application.SldWorks  
Set swModel = swApp.**ActiveDoc**  
swModel.**ClearSelection2** True  
Set swSelMgr = swModel.**SelectionManager**  
Set swModelDocExt = swModel.**Extension**  
While 1

' Loops until you select an entity in the graphics area

While swSelMgr.**GetSelectedObjectCount** = 0  
DoEvents  
Wend

swModelDocExt.**ShowSmartMessage** "This is the message.", 500, True, True  
DoEvents  
Wend

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
