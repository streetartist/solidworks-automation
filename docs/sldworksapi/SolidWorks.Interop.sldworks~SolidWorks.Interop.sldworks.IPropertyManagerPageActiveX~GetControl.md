# GetControl Method (IPropertyManagerPageActiveX)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX~GetControl`

Gets the interface to this ActiveX control.
Gets the interface to this ActiveX control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetControl() As System.Object
```

```

Dim instance As IPropertyManagerPageActiveX
Dim value As System.Object
 
value = instance.GetControl()
```

```

System.object GetControl()
```

```

System.Object^ GetControl(); 
```

#### Return Value

ActiveX control

Remarks

Do not call this method until the PropertyManager page is displayed. If you call this method before the PropertyManager page is displayed, then the method will fails and retval is NULL.

When the ActiveX control is created, the program creating the PropertyManager page should receive notification from the IPropertyManagerPage2Handler5::OnActiveXControlCreated method. Your program should not call IPropertyManagerPageActiveX::GetControl or [IPropertyManagerPageActiveX::IGetControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX~IGetControl.md) to get the interface object for this ActiveX control, because the PropertyManager page is not displayed when this notification is sent.

When the page is displayed, your program can now initialize the control properties so that the control looks how you want it to appear when it the PropertyManager page is initially displayed. You can set up the event sink for the control so that you receive notification when certain events happen to the control.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageActiveX Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX.md)  
[IPropertyManagerPageActiveX Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX_members.md)
