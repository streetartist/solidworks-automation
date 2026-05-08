# Redraw Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~Redraw`

Gets or sets whether to have IModelViewManager::CreateSectionView validate and return a status for section bodies instead of section views.
Gets or sets whether to have [IModelViewManager::CreateSectionView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md) validate and return a status for section bodies instead of section views.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Redraw As System.Boolean
```

```

Dim instance As ISectionViewData
Dim value As System.Boolean
 
instance.Redraw = value
 
value = instance.Redraw
```

```

System.bool Redraw {get; set;}
```

```

property System.bool Redraw {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to validate and return a status for newly created section bodies, false to not

Remarks

By default, [IModelViewManager::CreateSectionView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md) returns whether it successfully created a section view. Set this property to true to have [IModelViewManager::CreateSectionView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md) check and return whether it successfully created the section bodies.

Example

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)  
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)  
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)  
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.md)
