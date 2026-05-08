# AddActivePage Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddActivePage`

Adds a third-party CPropertyPage to ISWPropertySheet and adds an ActiveX control on top of the page.
Adds a third-party CPropertyPage to [ISWPropertySheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.md) and adds an ActiveX control on top of the page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddActivePage( _
   ByVal Title As System.String, _
   ByVal ProgId As System.String, _
   ByVal LicenseKey As System.String _
) As System.Integer
```

```

Dim instance As ISWPropertySheet
Dim Title As System.String
Dim ProgId As System.String
Dim LicenseKey As System.String
Dim value As System.Integer
 
value = instance.AddActivePage(Title, ProgId, LicenseKey)
```

```

System.int AddActivePage( 
   System.string Title,
   System.string ProgId,
   System.string LicenseKey
)
```

```

System.int AddActivePage( 
   System.String^ Title,
   System.String^ ProgId,
   System.String^ LicenseKey
) 
```

#### Parameters

*Title*
:   Title of CPropertyPage

*ProgId*
:   Name, ProgID, or CLSID of the ActiveX control (see Remarks)

*LicenseKey*
:   License key for the ActiveX control

#### Return Value

Index of CPropertyPage on ISWPropertySheet

Remarks

Typically, this method is called from the ISldWorks [PropertySheetCreateNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PropertySheetCreateNotifyEventHandler.md) event handler. See the Example section.

The ProgID argument accepts any of these values:

- OLE short name  or ProgID for the class; for example, "MSCAL.Calendar".  The name must match the name registered by the control.

- String form of a CLSID, contained within braces, for example, "{9DBAFCCF-592F-101B-85CE-00608CEC297B}".

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

Example

```

'VBA Main module
```

```

Dim swApp As SldWorks.SldWorks  
Option Explicit  
Sub main()  
    UserForm1.Show (swModeLess)  
End Sub
```

```

'Insert UserForm module to VBA application
```

```

Option Explicit
```

```

Public WithEvents swAppEvents As SldWorks.SldWorks  
Dim swApp As SldWorks.SldWorks
```

```

Private Function swAppEvents_PropertySheetCreateNotify(ByVal Sheet As Object, ByVal sheetType As Long) As Long  
    Dim msrcSWPropertySheet As SWPropertySheet  
    Set msrcSWPropertySheet = Sheet  
    Call msrcSWPropertySheet.AddActivePage("PropertySheetExample2", "", "")  
End Function
```

```

  
Private Sub UserForm_Initialize()  
    Set swApp = Application.SldWorks  
    Set swAppEvents = swApp  
End Sub
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.md)  
[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.md)
