# IPropertyManagerPage2 Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2`

Provides add-in applications the ability to display and use views that have the look and feel of SOLIDWORKS PropertyManager pages.
Provides add-in applications the ability to display and use views that have the look and feel of SOLIDWORKS PropertyManager pages.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPropertyManagerPage2 
```

```

Dim instance As IPropertyManagerPage2
```

```

public interface IPropertyManagerPage2 
```

```

public interface class IPropertyManagerPage2 
```

Remarks

OK and Cancel buttons are optional for IPropertyManagerPage2 objects, but a Help button is always displayed. If you do not want to implement help for your add-in, return false on help notification to display SOLIDWORKS Help.

PropertyManager controls are displayed in a single, left-aligned column. Slight vertical spacing adjustment is available with the [IPropertyManagerPageGroup::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~AddControl.md) or [IPropertyManagerPageGroup::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~IAddControl.md) or the [PropertyManagerPage2::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.md) or [IPropertyManagerPage2::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddControl.md) Options argument.

Use [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md)(swPropertyManagerColorDivider,UserPrefOption) to get the color of the PropertyManager divider box backgrounds for custom bitmap color blending purposes. The returned integer value is the COLORREF value.

The add-in application must implement the [IPropertyManagerPage2Handler8](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8.md) interface for data to be exchanged with the add-in application. The add-in application owns the IPropertyManagerPage2 object, which owns the IPropertyManagerPage2Handler8 for that page.

The limits on the number of controls on a PropertyManager page are:

- Total number of controls = 300 (This number does not include group and selection boxes.)
- Total number of group boxes = 20
- Total number of selection boxes = 15

NOTE: Number boxes count as 2 controls. All other controls count as 1 control.

SOLIDWORKS does not allow suppressing components or features while a PropertyManager page is open.

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

Example

To create a .NET add-in that implements this interface, start with one of these Visual Studio projects:

- Visual Basic - SwVBAddin
- Visual C# - SwCSharpAddin

Example

[Create PropertyManager Page (VBA)](Create_PropertyManager_Page_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IPropertyManagerPageActiveX Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX.md)  
[IPropertyManagerPageBitmap Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap.md)  
[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.md)  
[IPropertyManagerPageButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton.md)  
[IPropertyManagerPageCheckbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox.md)  
[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.md)  
[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md)  
[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.md)  
[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.md)  
[IPropertyManagerPageOption Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageOption.md)  
[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.md)  
[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.md)  
[IPropertyManagerPageTextbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTextbox.md)  
[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.md)  
[IModelDocExtension::GetActivePropertyManagerPage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetActivePropertyManagerPage.md)
