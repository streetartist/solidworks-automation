# IDisplayDimension Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension`

Represents instances of dimensions displayed in parts, assemblies, drawings and sensors.
Represents instances of dimensions displayed in [parts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md), [assemblies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md), [drawings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md) and [sensors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IDisplayDimension 
```

```

Dim instance As IDisplayDimension
```

```

public interface IDisplayDimension 
```

```

public interface class IDisplayDimension 
```

Remarks

You can display a SOLIDWORKS dimension more than once. For example, you can bring the base-extrude dimension into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SOLIDWORKS API. The original base-extrude dimension is represented by the [Dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md) object in the SOLIDWORKS API.

SOLIDWORKS stores many of the properties associated with a dimension with the underlying Dimension object. For example, you must get the Dimension object using [IDisplayDimension::GetDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDimension.md) to access or modify the underlying dimension value.

Example

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)  
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)  
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)  
[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)  
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)  
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)  
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)  
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)  
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)  
[Set Properties of Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)  
[Set Properties of Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)  
[Set Properties of Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.md)  
[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)
