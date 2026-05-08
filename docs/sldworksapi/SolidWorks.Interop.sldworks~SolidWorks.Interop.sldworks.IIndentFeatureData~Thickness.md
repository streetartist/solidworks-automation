# Thickness Property (IIndentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Thickness`

Gets or sets the thickness of the indent feature.
Gets or sets the thickness of the indent feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Thickness As System.Double
```

```

Dim instance As IIndentFeatureData
Dim value As System.Double
 
instance.Thickness = value
 
value = instance.Thickness
```

```

System.double Thickness {get; set;}
```

```

property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Thickness

Remarks

This property applies to solid bodies only.

If [IIndentFeatureData::IsCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~IsCut.md) is set to true (i.e., remove the intersection area of the target body), then there is no thickness.

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
