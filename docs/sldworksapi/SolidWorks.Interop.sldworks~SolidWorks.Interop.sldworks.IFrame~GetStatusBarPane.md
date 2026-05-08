# GetStatusBarPane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetStatusBarPane`

Gets a pointer to one of up to five panes on the right side of the status bar.
Gets a pointer to one of up to five panes on the right side of the status bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetStatusBarPane() As StatusBarPane
```

```

Dim instance As IFrame
Dim value As StatusBarPane
 
value = instance.GetStatusBarPane()
```

```

StatusBarPane GetStatusBarPane()
```

```

StatusBarPane^ GetStatusBarPane(); 
```

#### Return Value

Pointer to a [status bar pane object](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane.md)

Remarks

There are only 5 panes available starting from the right of the screen to the existing SOLIDWORKS panes.

This method returns a null pointer to a pane when you have used all possible panes.

These objects appear on the status bar until they go out of scope. To use them in a project, they should be declared globally in the Visual Basic project and managed during the life cycle of the client application.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)  
[IFrame::SetStatusBarText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~SetStatusBarText.md)
