# GetSketchSegmentCount Method (IBrokenOutSectionFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~GetSketchSegmentCount`

Gets the number of sketch segments that form the border of this broken-out section feature.
Gets the number of sketch segments that form the border of this broken-out section feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchSegmentCount() As System.Integer
```

```

Dim instance As IBrokenOutSectionFeatureData
Dim value As System.Integer
 
value = instance.GetSketchSegmentCount()
```

```

System.int GetSketchSegmentCount()
```

```

System.int GetSketchSegmentCount(); 
```

#### Return Value

Number of sketch segments

Remarks

Before calling this method you must set [IBrokenOutSectionFeatureData::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch.md) to true.

Call this method to set the Count parameter of [IBrokenOutSectionFeatureData::IGetSketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~IGetSketchSegment.md).

Example

[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)  
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)  
[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.md)  
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.md)  
[IBrokenOutSectionFeatureData::SketchSegment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~SketchSegment.md)
