# AddControl Method (ITaskpaneView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddControl`

Adds an ActiveX control to the Task Pane view.
Adds an ActiveX control to the Task Pane view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddControl( _
   ByVal ClassName As System.String, _
   ByVal LicKey As System.String _
) As System.Object
```

```

Dim instance As ITaskpaneView
Dim ClassName As System.String
Dim LicKey As System.String
Dim value As System.Object
 
value = instance.AddControl(ClassName, LicKey)
```

```

System.object AddControl( 
   System.string ClassName,
   System.string LicKey
)
```

```

System.Object^ AddControl( 
   System.String^ ClassName,
   System.String^ LicKey
) 
```

#### Parameters

*ClassName*
:   Name or class ID for the ActiveX control

*LicKey*
:   License key for the ActiveX control

#### Return Value

Pointer to the IUnknown interface for this ActiveX control

Remarks

If the ActiveX control added is a dialog, then see [Microsoft KB Archive/92905](https://www.betaarchive.com/wiki/index.php/Microsoft_KB_Archive/92905), "DlgTab.exe - Infinite Loop Moving through Dialog Ctrl". Follow the instructions in this article, or turn off Control Parent in Extended Styles of Dialog for the dialog.

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

Example

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)  
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)  
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)  
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.md)
