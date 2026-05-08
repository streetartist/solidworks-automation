# DisplayWindowFromHandlex64 Method (ITaskpaneView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandlex64`

Adds a .NET control to the Task Pane view on 64-bit machines.
Adds a .NET control to the Task Pane view on 64-bit machines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DisplayWindowFromHandlex64( _
   ByVal WindowHandle As System.Long _
) As System.Boolean
```

```

Dim instance As ITaskpaneView
Dim WindowHandle As System.Long
Dim value As System.Boolean
 
value = instance.DisplayWindowFromHandlex64(WindowHandle)
```

```

System.bool DisplayWindowFromHandlex64( 
   System.long WindowHandle
)
```

```

System.bool DisplayWindowFromHandlex64( 
   System.int64 WindowHandle
) 
```

#### Parameters

*WindowHandle*
:   64-bit handle of .NET control

#### Return Value

True if .NET control is added, false if not

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

To insert a Task Pane view window, use this method to create your Task Pane view window and pass its handle to SOLIDWORKS.

Example

[Add .NET Controls to SOLIDWORKS using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)  
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)  
[ITaskpaneView::GetTaskpaneViewWndx64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetTaskpaneViewWndx64.md)
