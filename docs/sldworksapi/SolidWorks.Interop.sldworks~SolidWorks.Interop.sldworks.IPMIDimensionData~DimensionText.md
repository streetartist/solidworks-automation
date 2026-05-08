# DimensionText Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData~DimensionText`

Gets the text of this PMI dimension.
Gets the text of this PMI dimension.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DimensionText As System.String
```

```

Dim instance As IPMIDimensionData
Dim value As System.String
 
instance.DimensionText = value
 
value = instance.DimensionText
```

```

System.string DimensionText {get; set;}
```

```

property System.String^ DimensionText {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Dimension text

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDimensionData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.md)  
[IPMIDimensionData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData_members.md)
