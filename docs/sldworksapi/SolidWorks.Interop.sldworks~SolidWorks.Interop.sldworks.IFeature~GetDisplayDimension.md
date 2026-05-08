# GetDisplayDimension Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDisplayDimension`

Gets the display dimension object for the specified pattern property.
Gets the display dimension object for the specified pattern property.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayDimension( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IFeature
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetDisplayDimension(Index)
```

```

System.object GetDisplayDimension( 
   System.int Index
)
```

```

System.Object^ GetDisplayDimension( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Pattern property as defined by [swFeatureDimensionParameter\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureDimensionParameter_e.html)

#### Return Value

[IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

Example

[Get Pattern Display Dimension (VBA)](Get_Pattern_Display_Dimension_Example_VB.htm)  
[Get Pattern Display Dimension (VB.NET)](Get_Pattern_Display_Dimension_Example_VBNET.htm)  
[Get Pattern Display Dimension (C#)](Get_Pattern_Display_Dimension_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::EnumDisplayDimensions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~EnumDisplayDimensions.md)  
[IFeature::GetFirstDisplayDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstDisplayDimension.md)  
[IFeature::GetNextDisplayDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextDisplayDimension.md)
