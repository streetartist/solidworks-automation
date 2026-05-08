# IAnnotation Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation`

Allows access to notes, weld symbols, datum tags, display dimensions, blocks, cosmetic threads, center marks, centerlines, and other annotation types.
Allows access to notes, weld symbols, datum tags, display dimensions, blocks, cosmetic threads, center marks, centerlines, and other annotation types.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IAnnotation 
```

```

Dim instance As IAnnotation
```

```

public interface IAnnotation 
```

```

public interface class IAnnotation 
```

Remarks

Because IAnnotation is a high-level representation of all annotation types, it provides functions that are generic to all types of annotations. For example, every annotation has a name and position, so IAnnotation provides functions that access this data.

Although IAnnotation has specific lower-level objects (such as [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)), it does not have any derived classes in the SOLIDWORKS API. This means that you cannot use an IAnnotation pointer to call functions in the lower-level objects. You also cannot use QueryInterface to obtain the underlying classes. Instead, SOLIDWORKS provides [IAnnotation::GetSpecificAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.md), which accesses underlying objects.

Similarly if you are holding onto a lower-level class, then you can obtain the corresponding IAnnotation object using the GetAnnotation method of that class (see the **Accessors** list in this topic).

Example

[Get Whether Note Contains Rich-embedded Text (VBA)](Get_Whether_Note_Contains_Rich-embedded_Text_Example_VB.htm)  
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)  
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)  
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)  
[Select Table Cells (C#)](Select_Table_Cells_Example_CSharp.htm)  
[Select Table Cells (VB.NET)](Select_Table_Cells_Example_VBNET.htm)  
[Select Table Cells (VBA)](Select_Table_Cells_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::GetObjectId Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectId.md)
