# Depth Property (IBrokenOutSectionFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~Depth`

Gets or sets the depth of exposure of inner details of the model in the broken-out section feature.
Gets or sets the depth of exposure of inner details of the model in the broken-out section feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Depth As System.Double
```

```

Dim instance As IBrokenOutSectionFeatureData
Dim value As System.Double
 
instance.Depth = value
 
value = instance.Depth
```

```

System.double Depth {get; set;}
```

```

property System.double Depth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Depth exposure of inner details (see **Remarks**)

Remarks

Before setting this property, you must set [IBrokenOutSectionFeatureData::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch.md) to false.

This property is valid only if [IBrokenOutSectionFeatureData::DepthReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~DepthReference.md) is null and the selection list is empty.

Example

[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)  
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)  
[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.md)  
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.md)
