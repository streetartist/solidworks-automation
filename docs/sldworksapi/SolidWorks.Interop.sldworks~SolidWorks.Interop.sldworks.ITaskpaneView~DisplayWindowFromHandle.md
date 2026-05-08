# DisplayWindowFromHandle Method (ITaskpaneView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandle`

Obsolete. Superseded by ITaskpaneView::DisplayWindowFromHandlex64.
Obsolete. Superseded by [ITaskpaneView::DisplayWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandlex64.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DisplayWindowFromHandle( _
   ByVal WindowHandle As System.Integer _
) As System.Boolean
```

```

Dim instance As ITaskpaneView
Dim WindowHandle As System.Integer
Dim value As System.Boolean
 
value = instance.DisplayWindowFromHandle(WindowHandle)
```

```

System.bool DisplayWindowFromHandle( 
   System.int WindowHandle
)
```

```

System.bool DisplayWindowFromHandle( 
   System.int WindowHandle
) 
```

#### Parameters

*WindowHandle*
:   Handle of .NET control

#### Return Value

True if .NET control is added, false if not

Remarks

Because this method is valid only for 32-bit applications, it is now obsolete.

To insert a Task Pane view window, create your Task Pane view window and pass its handle to SOLIDWORKS using ITaskpaneView::DisplayWindowFromHandlex64.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)  
[ITaskpaneView::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddControl.md)
