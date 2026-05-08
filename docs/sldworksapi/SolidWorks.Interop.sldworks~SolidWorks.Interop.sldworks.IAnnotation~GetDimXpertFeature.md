# GetDimXpertFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDimXpertFeature`

Gets the DimXpert feature associated with this annotation.
Gets the DimXpert feature associated with this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDimXpertFeature() As System.Object
```

```

Dim instance As IAnnotation
Dim value As System.Object
 
value = instance.GetDimXpertFeature()
```

```

System.object GetDimXpertFeature()
```

```

System.Object^ GetDimXpertFeature(); 
```

#### Return Value

[DimXpert feature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.md)

Remarks

If an annotation is a display dimension, then use [IAnnotation::IsDimXpert](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IsDimXpert.md) to determine if it is a DimXpert annotation. If it is, then use IAnnotation::GetDimXpertFeature to access the DimXpert feature, which provides access to the display dimension information.

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
[IDisplayDimension::IsDimXpert Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsDimXpert.md)
