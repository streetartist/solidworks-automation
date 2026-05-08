# SetClass Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX~SetClass`

Sets the interface to this ActiveX control.
Sets the interface to this ActiveX control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetClass( _
   ByVal ClassID As System.String, _
   ByVal LicenseKey As System.String _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageActiveX
Dim ClassID As System.String
Dim LicenseKey As System.String
Dim value As System.Boolean
 
value = instance.SetClass(ClassID, LicenseKey)
```

```

System.bool SetClass( 
   System.string ClassID,
   System.string LicenseKey
)
```

```

System.bool SetClass( 
   System.String^ ClassID,
   System.String^ LicenseKey
) 
```

#### Parameters

*ClassID*
:   Class ID for the control

*LicenseKey*
:   License key for the control

#### Return Value

Always returns true

Remarks

This method sets the class ID and license key information for the ActiveX control when a PropertyManager page created using the API is shown and the ActiveX control is created. ClassId can be either the name of the control (ProgID) or the class ID (CLSID), for example, "MSCAL.calendar" or "{8E27C92B-1264-101C-8A2F-040224009C02}". Both provide the calendar protocol. You can obtain these strings using a combination of the Microsoft OLE/COM Object Viewer and the registry editor.

VBA example:

' ProgID

bRet = m\_pActiveXControl.SetClass("MSCAL.Calendar", "")

bRet = m\_pActiveXControl2.SetClass("MSComctlLib.ListViewCtrl", "")

' CLSID

bRet = m\_pActiveXControl.SetClass("{8E27C92B-1264-101C-8A2F-040224009C02}", "")

bRet = m\_pActiveXControl2.SetClass("{BDD1F04B-858B-11D1-B16A-00C0F0283628}", "")

This method does not check to determine if the creation of the control worked. Instead, the [IPropertyManagerPage2Handler5::OnActiveXControlCreated](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnActiveXControlCreated.md) sends notification when an attempt to create the ActiveX control occurs, regardless if it is created or not. Use the IPropertyManagerPage2Handler5::OnActiveXControlCreated method's return value to indicate what action to take if the creation of the control failed.

Example

See the [IPropertyManagerPageActiveX](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageActiveX Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX.md)  
[IPropertyManagerPageActiveX Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX_members.md)
