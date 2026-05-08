# BorderLineWeight Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~BorderLineWeight`

Gets or sets the line weight of the border lines to the specified SOLIDWORKS-supplied weight for this table.
Gets or sets the line weight of the border lines to the specified SOLIDWORKS-supplied weight for this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BorderLineWeight As System.Integer
```

```

Dim instance As ITableAnnotation
Dim value As System.Integer
 
instance.BorderLineWeight = value
 
value = instance.BorderLineWeight
```

```

System.int BorderLineWeight {get; set;}
```

```

property System.int BorderLineWeight {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Weight of border lines for this table as defined by [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

Example

[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)  
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)  
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::ITableAnnotation::GridLineWeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GridLineWeight.md)  
[ITableAnnotation::BorderLineWeightCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~BorderLineWeightCustom.md)  
[ITableAnnotation::GridLineWeightCustom Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GridLineWeightCustom.md)
