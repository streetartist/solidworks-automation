# Parameter Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter`

Gets the specified parameter.
Gets the specified parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Parameter( _
   ByVal StringIn As System.String _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim StringIn As System.String
Dim value As System.Object
 
value = instance.Parameter(StringIn)
```

```

System.object Parameter( 
   System.string StringIn
)
```

```

System.Object^ Parameter( 
   System.String^ StringIn
) 
```

#### Parameters

*StringIn*
:   Name of parameter (for example, "D1@Base-Revolve")

#### Return Value

Parameter (see **Remarks**)

Remarks

Most parameters are [dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md).

The StringIn argument must be the fully qualified dimension name (for example, "D1@Base-Extrude") for this method. However, the full dimension name is not needed if you use [IFeature::IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IParameter.md) or [IFeature::Parameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Parameter.md).

Some characters are recognized as special characters. The use of these characters in names or parts or features can cause this method to fail to return a dimension. These special characters are not recognized in names of parts or features:

- at sign ( @ )
- period ( . )
- backslash ( / )

Example

[Change Dimension (VBA)](Change_Dimension_Example_VB.htm)  
[Get Depth of Extrusion (VBA)](Get_Depth_of_Extrusion_Example_VB.htm)  
[Modify Plane By Changing System Value (VBA)](Modify_Plane_by_Changing_System_Value_Example_VB.htm)  
[Recalculate Bounding Box (C#)](Recalculate_Bounding_Box_Example_CSharp.htm)  
[Recalculate Bounding Box (VB.NET)](Recalculate_Bounding_Box_Example_VBNET.htm)  
[Recalculate Bounding Box (VBA)](Recalculate_Bounding_Box_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IParameter.md)  
[IModelDoc2::SetParamValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetParamValue.md)
