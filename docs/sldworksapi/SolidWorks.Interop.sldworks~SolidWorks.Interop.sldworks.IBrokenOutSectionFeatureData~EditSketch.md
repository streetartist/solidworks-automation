# EditSketch Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch`

Gets or sets whether to place this broken-out section feature in edit sketch mode.
Gets or sets whether to place this broken-out section feature in edit sketch mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EditSketch As System.Boolean
```

```

Dim instance As IBrokenOutSectionFeatureData
Dim value As System.Boolean
 
instance.EditSketch = value
 
value = instance.EditSketch
```

```

System.bool EditSketch {get; set;}
```

```

property System.bool EditSketch {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to place this feature in edit sketch mode, false to not (see **Remarks**)

Remarks

To get the sketch segments that circumscribe this broken-out section feature:

1. Set this property to true.
2. Call [IBrokenOutSectionFeatureData::SketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~SketchSegment.md) or [IBrokenOutSectionFeatureData::IGetSketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~IGetSketchSegment.md).

To set the depth or depth reference for this broken-out section feature:

1. Set this property to false.
2. Call [IBrokenOutSectionFeatureData::Depth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~Depth.md) or [IBrokenOutSectionFeatureData::DepthReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~DepthReference.md).

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
