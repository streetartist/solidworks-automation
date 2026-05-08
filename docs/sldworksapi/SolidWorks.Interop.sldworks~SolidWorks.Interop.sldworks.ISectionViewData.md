# ISectionViewData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData`

Allows you to create and access section views in parts and assemblies.
Allows you to create and access section views in parts and assemblies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISectionViewData 
```

```

Dim instance As ISectionViewData
```

```

public interface ISectionViewData 
```

```

public interface class ISectionViewData 
```

Remarks

A section view is defined by multiple planes, colors, offsets, etc.

To create a section view in a part or assembly:

1. Use [IModelViewManager::CreateSectionViewData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionViewData.md) to create the ISectionViewData object.
2. Set the properties of ISectionViewData.
3. Use [IModelViewManager::CreateSectionView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateSectionView.md) to create the section view. IModelViewManager::CreateSectionView returns whether it successfully created the section view; it does not return whether it successfully created valid section bodies. Set [ISectionViewData::Redraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~Redraw.md) to true to have IModelViewManager::CreateSectionView validate and return a status for section bodies instead of section views.

Example

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)  
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)  
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)  
[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)  
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)  
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)  
[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)  
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)  
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)
