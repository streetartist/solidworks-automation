# ITableAnchor Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor`

Allows access to the data that defines a table anchor feature.
Allows access to the data that defines a table anchor feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ITableAnchor 
```

```

Dim instance As ITableAnchor
```

```

public interface ITableAnchor 
```

```

public interface class ITableAnchor 
```

Remarks

If a table anchor is selected, then it can be retrieved with [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). If the selected object type is swSelBOMTEMPS, then getting the selected object is a [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object. Use [IFeature::GetSpecifiedFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to return a TableAnchor object.

If you traverse the features and subfeatures of a drawing, then the table anchors display as subfeatures of the sheet format. When [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md) returns GeneralTableAnchor, HoleTableAnchor, WeldmentCutListAnchor, RevisionTableAnchor, or BomTemplate, use IFeature::GetSpecificFeature2 to return a ITableAnchor object.

NOTE: Weld table anchors are not currently supported.

You can also retrieve a ITableAnchor object from the [ISheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md) object using [ISheet::TableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TableAnchor.md). There is only one anchor of each type on a sheet format.

Example

[Get Table Anchor (VBA)](Get_Table_Anchor_Example_VB.htm)  
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)  
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)  
[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnchor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
