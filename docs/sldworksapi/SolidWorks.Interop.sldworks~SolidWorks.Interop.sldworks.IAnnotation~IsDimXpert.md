# IsDimXpert Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IsDimXpert`

Gets whether the annotation is a DimXpert annotation.
Gets whether the annotation is a DimXpert annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsDimXpert() As System.Boolean
```

```

Dim instance As IAnnotation
Dim value As System.Boolean
 
value = instance.IsDimXpert()
```

```

System.bool IsDimXpert()
```

```

System.bool IsDimXpert(); 
```

#### Return Value

True if the annotation is a DimXpert annotation, false if not

Remarks

Use this method to determine if the annotation is a DimXpert display dimension. If it is, then use  [IAnnotation::GetDimXpertFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDimXpertFeature.md) to access the DimXpert feature, which provides access to the display dimension information.

DimXpert annotations such as datums and GTols can be hidden, shown, or hidden as a group, which can be important when exporting to a DXF/DWG file.

Example

[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)  
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)  
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetDimXpertFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDimXpertFeature.md)
