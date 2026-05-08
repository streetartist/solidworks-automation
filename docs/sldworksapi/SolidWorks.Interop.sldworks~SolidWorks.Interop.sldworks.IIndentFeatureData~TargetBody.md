# TargetBody Property (IIndentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody`

Gets or sets the solid or surface body to indent.
Gets or sets the solid or surface body to indent.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TargetBody As System.Object
```

```

Dim instance As IIndentFeatureData
Dim value As System.Object
 
instance.TargetBody = value
 
value = instance.TargetBody
```

```

System.object TargetBody {get; set;}
```

```

property System.Object^ TargetBody {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Solid or surface [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to indent

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
[IIndentFeatureData::IsCut Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~IsCut.md)  
[IIndentFeatureData::SelectionState Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~SelectionState.md)  
[IIndentFeatureData::ToolBodyRegion Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion.md)
