# End Method (IUserProgressBar)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar~End`

Removes the progress indicator from the SOLIDWORKS status bar.
Removes the progress indicator from the SOLIDWORKS status bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function End() As System.Boolean
```

```

Dim instance As IUserProgressBar
Dim value As System.Boolean
 
value = instance.End()
```

```

System.bool End()
```

```

System.bool End(); 
```

#### Return Value

True if the progress indicator is removed, false if not

Remarks

This method does not immediately remove the progress bar from the status bar. Instead, a show-window event is posted to the message queue of the given window when this method is called. After Windows processes the message, the progress bar is removed  
from the status bar.

Example

See the [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserProgressBar Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.md)  
[IUserProgressBar Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar_members.md)
