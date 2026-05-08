# ISWPropertySheet Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet`

Allows applications to add pages to certain property sheets that are exported by the SOLIDWORKS application.
Allows applications to add pages to certain property sheets that are exported by the SOLIDWORKS application.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISWPropertySheet 
```

```

Dim instance As ISWPropertySheet
```

```

public interface ISWPropertySheet 
```

```

public interface class ISWPropertySheet 
```

Remarks

See [swPropSheetType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropSheetType_e.html) for a list of the property sheets that support this functionality.

An example of a property sheet is the dialog that is displayed when you click Tools > Options. This dialog consists of a base property sheet and property pages stacked on top of it. To display a specific property page, click its tab.

The MFC class that implements a property sheet is CPropertysheet, and the MFC class that implements a property page is CPropertyPage. ISWPropertySheet is a OLE wrapper class over the SOLIDWORKS CPropertysheet class. This means that SOLIDWORKS API programmers can add their own CPropertyPages to a SOLIDWORKS property sheet.

A SOLIDWORKS property sheet is different from a SOLIDWORKS [IPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md) page. A PropertyManager page is displayed when the PropertyManager tab is selected on the left-side panel. PropertyManager pages have replaced numerous dialogs.

**Creating PropertyPages**

When a property sheet is created that can have pages added to it, the notification swAppPropertySheetCreateNotify is sent via the [ISldWorks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md) interface. This notification is sent as swAppPropertySheetCreateNotify( LPDISPATCH sheet, long type) where sheet is the IDispatch interface of a ISWPropertySheet object and type is an enumerated constant of type swPropSheetType\_e.

When the application receives this notification, it can check the type of the sheet from the type argument. If pages are to be added, then the sequence of operations is:

- Ensure that the application resources will be used to make the page (for example by calling AfxSetResourceHandle())
- Create the CPropertyPage-derived class
- For 32-bit applications, pass the CPropertyPage object to [ISWPropertySheet::AddPage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddPage.md), casting the CPropertyPage\* to a long
- For 64-bit applications, pass the CPropertyPage object to [ISWPropertySheet::AddPagex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddPagex64.md), casting the CPropertyPage\* to a long long
- Reset the resources to their previous state

**Destroying PropertyPages**

The CPropertyPage PostNcDestroy function is called by the SOLIDWORKS application when the property sheet is being destroyed. At this point, the application should delete any objects (for example the CPropertyPage object.)

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md) topic for a list of delegates for this interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
