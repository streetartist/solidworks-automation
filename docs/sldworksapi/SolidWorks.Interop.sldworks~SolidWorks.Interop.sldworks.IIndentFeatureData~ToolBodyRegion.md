# ToolBodyRegion Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion`

Gets or sets the tool body region for the indent feature.
Gets or sets the tool body region for the indent feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ToolBodyRegion As System.Object
```

```

Dim instance As IIndentFeatureData
Dim value As System.Object
 
instance.ToolBodyRegion = value
 
value = instance.ToolBodyRegion
```

```

System.object ToolBodyRegion {get; set;}
```

```

property System.Object^ ToolBodyRegion {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Tool body region, which can be an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Example

[Insert Indent Feature (C#)](Insert_Indent_Feature_Example_CSharp.htm)  
[Insert Indent Feature (VB.NET)](Insert_Indent_Feature_Example_VBNET.htm)  
[Insert Indent Feature (VBA)](Insert_Indent_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md)  
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.md)  
[IIndentFeatureData::GetBodiesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~GetBodiesCount.md)  
[IIndentFeatureData::TargetBody Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.md)
