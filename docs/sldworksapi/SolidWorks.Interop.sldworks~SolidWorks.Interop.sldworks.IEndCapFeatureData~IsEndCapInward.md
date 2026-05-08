# IsEndCapInward Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~IsEndCapInward`

Gets or sets the thickness direction of this end cap feature.
Gets or sets the thickness direction of this end cap feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsEndCapInward As System.Integer
```

```

Dim instance As IEndCapFeatureData
Dim value As System.Integer
 
instance.IsEndCapInward = value
 
value = instance.IsEndCapInward
```

```

System.int IsEndCapInward {get; set;}
```

```

property System.int IsEndCapInward {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Thickness direction as defined by [swEndCapThicknessDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndCapThicknessDirection_e.html)

Example

See the [IEndCapFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md)  
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.md)
