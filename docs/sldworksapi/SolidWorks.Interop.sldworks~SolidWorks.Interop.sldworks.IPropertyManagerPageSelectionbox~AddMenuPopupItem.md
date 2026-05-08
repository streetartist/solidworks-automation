# AddMenuPopupItem Method (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~AddMenuPopupItem`

Adds a menu item to the pop-up menu for this selection box of the PropertyManager page.
Adds a menu item to the pop-up menu for this selection box of the PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenuPopupItem( _
   ByVal ID As System.Integer, _
   ByVal ItemText As System.String, _
   ByVal DocumentType As System.Integer, _
   ByVal HintText As System.String _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim ID As System.Integer
Dim ItemText As System.String
Dim DocumentType As System.Integer
Dim HintText As System.String
Dim value As System.Boolean
 
value = instance.AddMenuPopupItem(ID, ItemText, DocumentType, HintText)
```

```

System.bool AddMenuPopupItem( 
   System.int ID,
   System.string ItemText,
   System.int DocumentType,
   System.string HintText
)
```

```

System.bool AddMenuPopupItem( 
   System.int ID,
   System.String^ ItemText,
   System.int DocumentType,
   System.String^ HintText
) 
```

#### Parameters

*ID*
:   Unique user-defined value for this pop-up menu item

*ItemText*
:   Text for pop-up menu item

*DocumentType*
:   Document types for which this pop-up menu item is displayed as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*HintText*
:   Text displayed in the SOLIDWORKS status bar when the user moves the cursor over this pop-up menu item

#### Return Value

True if the pop-up menu item is added, false if not

Remarks

This method requires that you implement these [IPropertyManagerPage2Handler5](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5.md) methods:

- [IPropertyManagerPage2Handler5::OnPopupMenuItem](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnPopupMenuItem.md). When the user selects a pop-up menu item, this method determines which item was selected. The add-in should then perform the appropriate action.

- [IPropertyManagerPage2Handler5::OnPopupMenuItemUpdate](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnPopupMenuItemUpdate.md). When Windows attempts to select or deselect and enable or disable the pop-up menu item, SOLIDWORKS calls IPropertyManagerPage2Handler5::OnPopupMenuItemUpdate to get the state of the pop-up menu item from the add-in. Thus, IPropertyManagerPage2Handler5::OnPopupMenuItemUpdate:

  - Processes a request for the state of the specified pop-up menu item associated with the PropertyManager page.
  - Passes the state back to SOLIDWORKS.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
