# GetType Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType`

Gets the type of the annotation.
Gets the type of the annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetType() As System.Integer
```

```

Dim instance As IAnnotation
Dim value As System.Integer
 
value = instance.GetType()
```

```

System.int GetType()
```

```

System.int GetType(); 
```

#### Return Value

Type of the annotation as defined in [swAnnotationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnnotationType_e.html)

Remarks

If this annotation contains only Product and Manufacturing Information (PMI), then this method returns swAnnotationType\_e.swPMIOnly. In that case, use [IAnnotation::GetPMIType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIType.md) and [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) to obtain the PMI data associated with this annotation.

This method is useful when the IAnnotation object is obtained with [IAnnotation::GetSpecificAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSpecificAnnotation.md) or [IAnnotation::IGetSpecificAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.md).

Example

[Change Text Format (VBA)](Change_Text_Format_Example_VB.htm)  
[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)  
[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)  
[Get Types of Entities for Selected Dimension (VBA)](Get_Types_of_Entities_for_Selected_Dimension_Example_VB.htm)  
[Show Dimensions in Drawing Sheet (VBA)](Show_Dimensions_in_Drawing_Sheet_Example_VB.htm)  
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)  
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)  
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
