# IGeneralTableFeature Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature`

Allows access to the general table feature.
Allows access to the general table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IGeneralTableFeature 
```

```

Dim instance As IGeneralTableFeature
```

```

public interface IGeneralTableFeature 
```

```

public interface class IGeneralTableFeature 
```

Remarks

You can get this object using:

- [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) when a general table feature is selected in the FeatureManager design tree of the drawing.
- [ITableAnnotation::GeneralTableFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GeneralTableFeature.md).
- [IGeneralTableAnnotation::GeneralTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation~GeneralTable.md).

The filename extension for a general table is .sldtbt. Table templates are not supplied for general tables.

Example

[Hide and Show Row (VBA)](Hide_and_Show_Row_Example_VB.htm)  
[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)  
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)  
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGeneralTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IGeneralToleranceTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature.md)
