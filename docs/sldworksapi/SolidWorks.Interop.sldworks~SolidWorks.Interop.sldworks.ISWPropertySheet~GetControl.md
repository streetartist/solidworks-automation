# GetControl Method (ISWPropertySheet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~GetControl`

Gets the ActiveX control on the property sheet.
Gets the ActiveX control on the property sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetControl( _
   ByVal PageIndex As System.Integer _
) As System.Object
```

```

Dim instance As ISWPropertySheet
Dim PageIndex As System.Integer
Dim value As System.Object
 
value = instance.GetControl(PageIndex)
```

```

System.object GetControl( 
   System.int PageIndex
)
```

```

System.Object^ GetControl( 
   System.int PageIndex
) 
```

#### Parameters

*PageIndex*
:   Index of property sheet

#### Return Value

ActiveX control

Remarks

Typically, you would call this method from the ISWPropertySheet [OnOKNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_OnOKNotifyEventHandler.md) event handler to retrieve data from your ActiveX control.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.md)  
[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.md)
