# DisplayStatusBar Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DisplayStatusBar`

Sets whether to display the status bar.
Sets whether to display the status bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DisplayStatusBar( _
   ByVal OnOff As System.Boolean _
) 
```

```

Dim instance As ISldWorks
Dim OnOff As System.Boolean
 
instance.DisplayStatusBar(OnOff)
```

```

void DisplayStatusBar( 
   System.bool OnOff
)
```

```

void DisplayStatusBar( 
   System.bool OnOff
) 
```

#### Parameters

*OnOff*
:   True if you want the status bar displayed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IModelDoc2::Lock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Lock.md)  
[IModelDoc2::UnLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UnLock.md)  
[IStatusBarPane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane.md)
