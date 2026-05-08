# GetDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDimension`

Obsolete. Superseded by IDisplayDimension::GetDimension2.
Obsolete. Superseded by [IDisplayDimension::GetDimension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDimension2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDimension() As System.Object
```

```

Dim instance As IDisplayDimension
Dim value As System.Object
 
value = instance.GetDimension()
```

```

System.object GetDimension()
```

```

System.Object^ GetDimension(); 
```

#### Return Value

Dimension

Remarks

SOLIDWORKS can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) object in the SOLIDWORKS API. The original base-extrude dimension is represented by the [IDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md) object in the SOLIDWORKS API.

Example

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)  
[Get Component Via Display Dimension (VBA)](Get_Component_Via_Display_Dimension_Example_VB.htm)  
[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)  
[Iterate Through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)  
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)  
[Traverse Feature Dimensions (VBA)](Traverse_Feature_Dimensions_Example_VB.htm)  
[Unlink Dimensions (VBA)](Unlink_Dimensions_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IFeature::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Parameter.md)  
[IFeature::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IParameter.md)  
[IModelDoc2::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter.md)  
[IModelDoc2::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IParameter.md)  
[IDisplayDimension::IGetDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IGetDimension.md)
